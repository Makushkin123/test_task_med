from sqlalchemy import MetaData, Table, Integer, String, Column, Text, DateTime, Boolean, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


def get_engine(user, password, host, port, db):
    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    return create_engine(url)


metadata = MetaData()

#пострегс не любит русское название колонок, решил переименовать
rename_table_column = {
    "Субъект РФ": "SUBJECT_OF_THE_RUSSIAN_FEDERATION",
    "МО": "MO",
    "ИНН": "INN",
    "Статус": "STATUS",
    "Тип вывода из оборота": "TYPE_OF_WITHDRAWAL_FROM_CIRCULATION",
    "ГТИН": "GTIN",
    "Серия": "SERIES",
    "Дозы (количество доз в упаковке (флаконе))": "DOSE",
    "Количество Упаковок": "NUMBER_OF_PACKAGES",
    "Количество Доз": "COUNT_DOSE",
    "Срок годности": "EXPIRATION_DATE",
    "Просрочено дней": "DAYS_OVERDUE"

}



ETL = Table("public.overdue", metadata,
    Column('SUBJECT_OF_THE_RUSSIAN_FEDERATION', Text(), nullable=False),
    Column('MO', Text(), nullable=False),
    Column('INN', Text(), nullable=False),
    Column('STATUS', Text(), nullable=False),
    Column('TYPE_OF_WITHDRAWAL_FROM_CIRCULATION', Text(), nullable=False),
    Column('GTIN', Text(), nullable=False),
    Column('SERIES', Text(), nullable=False),
    Column('DOSE', Integer(), nullable=False),
    Column('NUMBER_OF_PACKAGES', Integer(), nullable=False),
    Column('COUNT_DOSE', Integer(), nullable=False),
    Column('EXPIRATION_DATE', Text(), nullable=False),
    Column('DAYS_OVERDUE', Integer(), nullable=False)
)