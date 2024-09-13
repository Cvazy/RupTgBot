import pdfplumber

from modules.clean_text.main import clean_text


def read_pdf_table(file_name):
    try:
        with pdfplumber.open(file_name) as pdf:
            for page_num, page in enumerate(pdf.pages):
                print(f'--- Страница {page_num + 1} ---\n')
                tables = page.extract_tables()

                if tables:
                    for table_num, table in enumerate(tables):
                        print(f'--- Таблица {table_num + 1} ---\n')

                        for row in table[2:]:
                            cleaned_row = [clean_text(i) for i in row]
                            print(cleaned_row)
                else:
                    print(f'Таблицы на странице {page_num + 1} не найдены.')
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")


read_pdf_table('doc.pdf')