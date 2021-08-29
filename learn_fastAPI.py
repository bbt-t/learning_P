from fastapi import FastAPI
from fastapi.responses import Response


app = FastAPI()

@app.get('/') #декоратор fastapi: функция будет запускать когда придёт GET-запрос
              #(http-метод GET) на адрес '/' (корневая страница н/р: some.com/)
def index_page():
    """
    Фукция (название может быть ЛЮБОЕ!) будет обрабатывать http-запрос
    :return: в Response "хранится" http-ответ (инкапсулируется)
    """
    return Response("Привет", media_type="text/html") #обязательно указывать media_type!

#запуск сервера ювикорн:
# uvicorn learn_fastAPI:app --reload

#запускается для указанного файла -> ищет глобальную переменную 'app'
#'--reload' означает что если мы изменим, указанный при запуске, файл uvicorn перезагрузит
#приложение чтобы "подтянуть" изменения.

# ПОИТОГУ: Намного легче поднимать сокет через fastAPI чем писать вручную!


