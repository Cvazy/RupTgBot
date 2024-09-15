import pandas as pd

pd.set_option('display.max_colwidth', None)


def read_exel_table(path):
    data = pd.read_excel(path, sheet_name = None)

    for _, df in data.items():
        columnNames = list(df.columns.ravel())

        for i in range(1, 4):
            print(df[columnNames[i]].to_list()[0])
        
        print('\n')

        struct = list()

        for i in range(4, len(columnNames)):
            struct.append(df[columnNames[i]].to_list())

        for rows in range(len(struct[0])):
            for cols in range(len(struct)):
                print(struct[cols][rows], end = ' ')
            print('\n')


read_exel_table('doc.xlsx')