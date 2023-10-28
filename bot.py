import telebot
from etl import xlsx_to_database
from create_table import get_engine, ETL
from sqlalchemy import select, func
import pandas as pd


BOT_TOKEN = "6501903351:AAGBuLSZX_kRUR782BXJqyZWrdYEphboHsw"


bot = telebot.TeleBot(BOT_TOKEN)

database_parameter = ["postgres", "usubop", "localhost", "5432", "etl"]


@bot.message_handler(commands=['report'])
def send_document(message):
    print(f"{message.from_user.username} попросил файл")

    with get_engine(*database_parameter).connect() as conn:
        count_dose_sum = func.sum(ETL.c["COUNT_DOSE"]).label("КОЛИЧЕСТВО ДОЗ")
        days_overdue_avg = func.round(func.avg(ETL.c["DAYS_OVERDUE"])).label("ПРОСРОЧЕНО ДНЕЙ")
        subject_of_the_federation = ETL.c["SUBJECT_OF_THE_RUSSIAN_FEDERATION"].label("СУБЪЕКТ РФ")

        query = select(subject_of_the_federation, count_dose_sum, days_overdue_avg).group_by(
            subject_of_the_federation).order_by(subject_of_the_federation)

        df_result = pd.read_sql_query(query, conn)

    with pd.ExcelWriter(path='output.xlsx', mode="w") as writer:
        df_result.to_excel(writer, sheet_name='result', index=False)
    with open("output.xlsx", "rb") as file:
        doc = file.read()
    bot.send_document(message.from_user.id, doc, visible_file_name="result.xlsx")


if __name__ == "__main__":
    xlsx_to_database(*database_parameter)
    try:
        bot.polling()
    finally:
        bot.stop_polling()



