FROM python:3.9

WORKDIR /urs/src/app

## Установка netcat
#RUN apt-get update && apt-get install -y netcat-openbsd
#
#COPY wait-for-it.sh /usr/local/bin/
#
## Делаем его исполняемым
#RUN chmod +x /usr/local/bin/wait-for-it.sh

COPY requirements.txt ./
COPY bot.py ./
COPY create_table.py ./
COPY etl.py ./
COPY input.xlsx ./

RUN pip install -r requirements.txt

RUN sleep 10

CMD ["python3","bot.py"]