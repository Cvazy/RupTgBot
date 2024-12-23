import io
import pandas as pd

pd.set_option('display.max_colwidth', None)


def read_exel_file_headers(file: io.BytesIO) -> list:
    for _, df in pd.read_excel(file, sheet_name = None).items():
        return list(df.columns.to_list())


def read_exel_file_content(file):
    for _, df in pd.read_excel(file, sheet_name = None).items():
        column_names = list(df.columns.ravel())

        for i in range(1, 4):
            print(df[column_names[i]].to_list()[0])

        print('\n')

        struct = list()

        for i in range(4, len(column_names)):
            struct.append(df[column_names[i]].to_list())

        for rows in range(len(struct[0])):
            for cols in range(len(struct)):
                print(struct[cols][rows], end = ' ')
            print('\n')
