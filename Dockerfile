FROM python:3.10
WORKDIR /usr/app/src
RUN pip install pyTelegramBotAPI && pip install aiohttp

COPY ./bot.py ./

CMD ["python",  "./bot.py"]
