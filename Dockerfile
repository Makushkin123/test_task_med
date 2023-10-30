FROM python:3.9

RUN sleep 15

WORKDIR /urs/src/app

COPY requirements.txt ./
COPY bot.py ./
COPY create_table.py ./
COPY etl.py ./
COPY input.xlsx ./

RUN pip install -r requirements.txt



CMD ["python3","bot.py"]