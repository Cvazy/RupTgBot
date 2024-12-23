import io

from modules.read_exel_files.main import read_exel_file_headers
from modules.read_pdf_files.main import read_pdf_file_headers

correct_exel_headers = [
    '№', 'ФИО (контакты)', 'Контакты', 'Приказ (наименование, номер дата)',
    'Дисциплина', 'Учебный год, семестр', 'Номер ведомость на ликвидацию расхождений',
    'Кафедра', 'Срок сдачи', 'Вид нагрузки'
]

correct_pdf_headers = [
    '№', 'Наименование дисциплины', 'Кол- во часов (з.е.)', 'Вид промежуточной аттестации',
    'Семестр', 'Учебный год дисциплины', 'Кафедра дисциплины', 'Контакты кафедры'
]


def validator_exel_files(file: io.BytesIO) -> bool:
    return all(header in correct_exel_headers for header in read_exel_file_headers(file))


def validator_pdf_files(file: io.BytesIO) -> bool:
    headers_array = read_pdf_file_headers(file)

    if headers_array is not None:
        return all(header in correct_pdf_headers for header in headers_array)

    return False