from create_table import get_engine, metadata, rename_table_column
import pandas as pd


def replace_char(element):
    return element.replace('\n', ' ')


# функция для преобразования данных из xlsx
def xlsx_to_database(user, password, host, port, db):
    conn = get_engine(user, password, host, port, db)
    metadata.create_all(conn)

    with pd.ExcelFile("input.xlsx") as xlsx:
        df = pd.read_excel(xlsx)
        result = df.rename(columns=df.iloc[2].apply(replace_char)).drop(index=[0, 1, 2, 3]).rename(
            columns=rename_table_column)
        # print(result["DOSE"])
        result.to_sql(name='public.overdue', con=conn, if_exists='replace', index=False)
