import socket

# создаём сокет, прослушиваем порт > 1024
server = socket.create_server(("127.0.0.1", 5000))
# освобождение порта после выхода из приложения
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# длина очереди (сколько соединений будем слушать)
server.listen(10)
#чтобы получать запросы "бесконечно" ожидать подключения клиентов необходим цикл:
while True:
    # Принимаем сетевые запросы
    client_socket, address = server.accept()  # приходит кортеж, распаковывается в 2 переменные
    # читаем что пришло в клинский сокет, декодируем т.к приходят данные (1024 байта) в байтовом виде
    # если придёт больше указанного обьёма (1024 байта) , то излишек "отсеится" !
    received_date = client_socket.recv(1024).decode('utf-8')
    print(f"Получили данные:\n{received_date}")
    # При попытке "зайти" на созданный веб-сервер будет получена строка "GET / HTTP/1.1", которую необходимо
    # модифицировать:
    path = received_date.split()[1]
    # формируем ответ: (минимальный набор заголовков)
    response = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n" \ # 2'\n' указывает что заголовки конч.
               f"Привет!<br />Path: {path}" #<br /> это перенос стркоки в html
    # отправляем в клиенский сокет
    client_socket.send(response.encode('utf-8'))
    # закрываем сокет, завершаем работу веб-сервера
    client_socket.shutdown(socket.SHUT_RDWR)

server.shutdown(socket.SHUT_RDWR)
server.close()

# В итоге, если перейти на http://localhost:5000/(ЛЮБОЙ АДРЕС ДАЛЕЕ), то мы будет получать ответ:
# Привет!
# Path: /(тот адрес на который перешли)