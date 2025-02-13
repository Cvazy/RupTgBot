import requests

from rup_bot.core.consts import URL_API

def check_user_into_students(tg_id):
    return requests.get(f'{URL_API}/students/?tg_id={tg_id}').json()


def insert_data_into_students(data, tg_id) -> int:
    data.update({'tg_id': tg_id})
    response = requests.post(f'{URL_API}/students/', data = data)
    return response.status_code


def get_file_from_rup_files(tg_id):
    return requests.get(f'{URL_API}/rup-files/?student={check_user_into_students(tg_id)[0]["id"]}').json()


def upload_file_into_rup_files(file_info, file_bytes, tg_id, file_id) -> int:
    files = {'file': (file_info.file_name, file_bytes)}

    response = requests.post(
        f'{URL_API}/rup-files/',
        files = files,
        data = {
            'student' : check_user_into_students(tg_id)[0]['id'],
            'tg_file_id' : file_id,
        }
    )

    return response.status_code
