responses = {
    'start' : 'Привет, {}! 👋\n\nДобро пожаловать в систему управления РУПами. '
             'Я помогу тебе загрузить и управлять информацией по твоим РУПам.',

    'get_data' : '📊Просмотреть данные по РУПам',

    'upload_data' : '⬆️Загрузить данные по РУПам',

    'sign_up' : 'Зарегистрироваться в боте',

    'pass_auth' : 'Пройдите сначала регистрацию',

    'rup_file_not_found' : 'Вы еще не загрузили документы',

    'fsm_input_last_name' : 'Введи свою фамилию',

    'fsm_input_first_name' : 'А теперь свое имя',

    'about_middle_name' : 'У тебя есть отчество?',

    'answer_yes' : 'Да',

    'answer_no' : 'Нет',

    'fsm_input_middle_name' : 'Введи свое отчество',

    'fsm_input_faculty' : 'На каком ты факультете',

    'fsm_input_group_number' : 'Какой у тебя номер группы?',

    'fsm_want_input_email' : 'Хотите указать свою почту?',

    'fsm_input_email' : 'Укажи свою почту',

    'fsm_want_input_phone' : 'Хотите указать свой номер телефона?',

    'fsm_input_phone' : 'Укажи свой номер телефона',

    'is_total_info_correct' : 'Указанная информация верная?',

    'refill_info_about_user' : 'Давай попробуем еще раз',

    'success_auth' : 'Авторизация прошла успешно ✅',

    'contact_info_by_faculty' : 'Контактная информация по твоему факультету:',

    'request_data' : 'Пожалуйста, загрузи файл с информацией по твоим РУПам. 📁\n'
                     'Поддерживаются следующие форматы: .docx, .pdf, .xls, .png, .jpeg.',

    'success_upload' : 'Спасибо, файл успешно загружен и информация обновлена! ✅',

    'unsuccessful_upload' : 'Похоже, загруженный файл не содержит данных по РУПам. Попробуй еще раз.\n'
         'Поддерживаются следующие форматы: .docx, .pdf, .xls, .png, .jpeg.',

    'uploaded_other_format' : 'Файл должен быть в одном из следующих форматов: .docx, .pdf, .xls, .png, .jpeg.\n'
                         'Попробуй снова загрузить файл в правильном формате.',

    'help' : 'Ты в разделе помощи. Вот список команд, которые ты можешь использовать:\n\n'
            '1️⃣ /upload – Эта команда позволяет загрузить файл с твоими РУПами. Поддерживаются форматы .docx, .pdf, .xls, .png, .jpeg.\n'
            '2️⃣ /get – Эта команда покажет текущий статус твоих РУПов, если они уже загружены в базу.\n\n'
            'Декан факультета: к.т.н., доцент\n'
            'Моргунов Юрий Алексеевич,\n'
            '+7 (495) 223-05-23, доб. 3305\n'
            '+7 (495) 686–08-06, ауд. ПК 224',

    'exception' : 'К сожалению, не понял тебя. Попробуй еще раз.'
}


matching_init_user_field = {
    'surname' : 'Фамилия',
    'name' : 'Имя',
    'patronymic' : 'Отчество',
    'faculty' : 'Факультет',
    'group' : 'Номер группы',
    'email' : 'Почта',
    'phone_number' : 'Номер телефона'
}

contact_info = {
    "Информационных технологий" : 'Осьмин Владимир Вячеславович (учебно-методическая работа) пр1215\n'
    'Копылов Григорий Николаевич (взаимодействие с партнёрами факультета) пр 1222\n'
    'Даньшина Марина Владимировна (по специальным вопросам, прием на ул. Б. Семёновская, 38, кабинет Н-326)\n'
    'Чернова Вера Михайловна (по общим вопросам) пр1215\n'
    'Телефон: +7 (495) 223-05-23, доб. 1709 – приёмная факультета.\n'
    'E-mail: isu@mospolytech.ru\n'
    'Группа Вконтакте — https://vk.com/fit.mospolytech',


    'Транспортный' : 'Декан факультета:\n'
    'Рыбакова Маргарита Романовна\n'
    '+7 (495) 223-05-23 доб. 1157\n'
    'Заместители декана:\n'
    'Лукьянов Михаил Николаевич\n'
    '+7 (495) 223-05-23 доб. 1457\n'
    'Помощники декана:\n'
    'Ануфриев Илья Алексеевич\n'
    '+7 (495) 223-05-23 доб. 1608\n'
    'Цибизова Полина Дмитриевна\n'
    '+7 (495) 223-05-23 доб. 1608\n'
    'Telegram: t.me/transport_faculty\n'
    'Вконтакте: vk.com/transportfaculty\n'
    'Телефон: +7(495) 223-05-23.\n'
    'E-mail: tr.facultet@mospolytech.ru',


    'Машиностроения' : 'Декан факультета:\n'
    'Евгений Владимирович Сафонов\n'
    'кандидат технических наук\n'
    '+7 (495) 223-05-23 доб. 2231\n'
    'fm@mospolytech.ru\n'
    'Заместитель декана по научной работе:\n'
    'Типалин Сергей Александрович\n'
    'кандидат технический наук, доцент\n'
    '+7 (495) 223-05-23 доб. 2317\n'
    'tsa_mami@mail.ru\n'
    'Заместитель декана по учебной работе: Васильев Александр Николаевич\n'
    'кандидат технический наук, доцент\n'
    '+7 (495) 223-05-23 доб. 2232\n'
    'anvasilyev2009@yandex.ru\n'
    'Заместитель декана по воспитательной и внеучебной работе:\n'
    'Бородкина Инга Ревазовна\n'
    '+7 (495) 223-05-23 доб. 2222\n'
    'i.r.borodkina@mospolytech.ru\n'
    'Заместитель декана по работе с предприятиями и образовательными учреждениями:\n'
    'Левина Татьяна Анатольевна\n'
    'кандидат экономических наук, доцент\n'
    '+7 (495) 223-05-23 доб. 2311\n'
    't.a.levina@mospolytech.ru\n'
    'Факультет в соцсетях:\n'
    'Вконтакте — https://vk.com/fm.mospolytech',


    'Химических технологий и биотехнологий' : 'Декан факультета:\n'
    'Соколов Андрей Сергеевич, кандидат технических наук\n'
    '+7 (495) 223-05-23, доб. 2228\n'
    'a.s.sokolov@mospolytech.ru\n'
    'Заместитель декана:\n'
    'Ермолаев Андрей Евгеньевич\n' 
    'erand@yandex.ru\n'
    'ул. Автозаводская, 16, ауд. АВ-1705\n'
    'Заместитель декана:\n'
    'Некрасов Дмитрий Анатольевич\n'    
    'nekrasov55@yandex.ru\n'
    'ул. Автозаводская, 16, ауд. АВ-1705\n'
    'Заместитель декана:\n'
    'Буздалина Ирина Александровна\n'
    'i.a.buzdalina@mospolytech.ru\n'
    'ул. Автозаводская, 16, ауд. АВ-1613\n'
    'Помощник декана:\n'
    'Юрицына Анастасия Михайловна\n'
    'nastyaoffender@mail.ru\n'
    'ул. Автозаводская, 16, ауд. АВ-1610\n'
    'E-mail: him.bio.tech@mospolytech.ru\n'
    'Группы Вконтакте:\n'
    'https://vk.com/himbiotech\n'
    'https://vk.com/htibmp',


    'Урбанистики и городского хозяйства' : 'Декан факультета:\n'
    'Лушин Кирилл Игоревич, к.т.н.\n'
    'Телефон: +7 (495) 223-05-23 доб. 2369\n'
    'E-mail: fuud@mospolytech.ru\n'
    'Адрес: ул. Автозаводская, 16, ауд. АВ-1609',


    'Экономики и управления' : 'Декан факультета:\n'
    'Назаренко Антон Владимирович, д.э.н., доцент\n'
    'Приемная: Аверкина Виктория Алексеевна, Бацина Дарья Александровна\n'
    'ул. Павла Корчагина, 22, ауд. ПК225\n'
    'Тел.: +7 (495) 223-05-23 доб. 3301\n'
    'Заместитель декана по учебной работе:\n'
    'Агопян Нина Эдуардовна\n'
    'ул. Павла Корчагина, 22, ауд. ПК225\n'
    'Тел.: +7 (495) 223-05-23 доб. 3410\n'
    'E-mail: n.e.agopyan@mospolytech.ru\n'
    'Заместитель декана по воспитательной и социальной работе:\n'
    'Фролова Наталья Николаевна\n'
    'ул. Павла Корчагина, 22, ауд. ПК210\n'
    'Тел.: +7 (495) 223-05-23 доб. 3304\n'
    'E-mail: n.n.frolova@mospolytech.ru\n'
    'Деканат: Дуданец Анастасия Дмитриевна\n'
    'ул. Павла Корчагина, 22, ауд. ПК210\n'
    'Тел.: +7 (495) 223-05-23 доб. 3310\n'
    'E-mail: fem@mospolytech.ru'
}
