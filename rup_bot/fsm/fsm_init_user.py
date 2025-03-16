import re

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from rup_bot.phrases import responses, matching_init_user_field
from rup_bot.db.db_queries import insert_data_into_students, get_list_faculties
from rup_bot.utils.keyboard_builder import make_keyboard_yes_or_no, \
    make_keyboard_get_data_and_upload_data, make_keyboard_list_faculties

fsm_init_user_router = Router()


class UserInfo(StatesGroup):
    input_last_name = State()
    input_first_name = State()
    have_middle_name = State()
    input_middle_name = State()
    input_faculty = State()
    input_group_number = State()
    want_input_email = State()
    input_email = State()
    want_input_phone = State()
    input_phone = State()
    is_total_info_correct = State()


def remove_spaces(message: str) -> str:
    return message.strip()


@fsm_init_user_router.message(F.text == responses.get('sign_up'))
async def sign_up_handler(message: Message, state: FSMContext) -> None:
    await message.answer(
        text = responses.get('fsm_input_last_name'),
        reply_markup = ReplyKeyboardRemove()
    )
    await state.set_state(UserInfo.input_last_name)


@fsm_init_user_router.message(
    UserInfo.input_last_name,
    F.text.func(lambda message: all(char.isalpha() for char in message))
)
async def waiting_input_last_name(message: Message, state: FSMContext) -> None:
    await message.answer(
        text = responses.get('fsm_input_first_name'),
        reply_markup = ReplyKeyboardRemove()
    )
    await state.update_data(surname = remove_spaces(message.text))
    await state.set_state(UserInfo.input_first_name)


@fsm_init_user_router.message(
    UserInfo.input_first_name,
    F.text.func(lambda message: all(char.isalpha() for char in message))
)
async def waiting_input_first_name(message: Message, state: FSMContext) -> None:
    await message.answer(
        text = responses.get('about_middle_name'),
        reply_markup = await make_keyboard_yes_or_no()
    )
    await state.update_data(name = remove_spaces(message.text))
    await state.set_state(UserInfo.have_middle_name)


@fsm_init_user_router.message(
    UserInfo.have_middle_name,
    F.text.in_(
        [responses.get('answer_yes'), responses.get('answer_no')]
    )
)
async def waiting_have_middle_name(message: Message, state: FSMContext) -> None:
    if message.text == responses.get('answer_yes'):
        await message.answer(
            text = responses.get('fsm_input_middle_name'),
            reply_markup = ReplyKeyboardRemove()
        )
        await state.set_state(UserInfo.input_middle_name)
    else:
        await message.answer(
            text = responses.get('fsm_input_group_number'),
            reply_markup = ReplyKeyboardRemove()
        )
        await state.set_state(UserInfo.input_group_number)


@fsm_init_user_router.message(
    UserInfo.input_middle_name,
    F.text.func(lambda message: all(char.isalpha() for char in message))
)
async def waiting_input_middle_name(message: Message, state: FSMContext) -> None:
    await message.answer(
        text = responses.get('fsm_input_faculty'),
        reply_markup = await make_keyboard_list_faculties()
    )
    await state.update_data(patronymic = remove_spaces(message.text))
    await state.set_state(UserInfo.input_faculty)


@fsm_init_user_router.message(
    UserInfo.input_faculty,
    F.text.in_([item.get('name') for item in get_list_faculties()])
)
async def waiting_input_faculty(message: Message, state: FSMContext) -> None:
    await message.answer(
        text = responses.get('fsm_input_group_number'),
        reply_markup = ReplyKeyboardRemove()
    )
    await state.update_data(faculty = remove_spaces(message.text))
    await state.set_state(UserInfo.input_group_number)


@fsm_init_user_router.message(
    UserInfo.input_group_number,
    F.text.func(lambda message: all(char.isdigit() or char == '-' for char in message))
)
async def waiting_input_group_number(message: Message, state: FSMContext) -> None:
    await message.answer(
        text = responses.get('fsm_want_input_email'),
        reply_markup = await make_keyboard_yes_or_no()
    )
    await state.update_data(group = remove_spaces(message.text))
    await state.set_state(UserInfo.want_input_email)


@fsm_init_user_router.message(
    UserInfo.want_input_email,
    F.text.in_(
        [responses.get('answer_yes'), responses.get('answer_no')]
    )
)
async def waiting_want_input_email(message: Message, state: FSMContext) -> None:
    if message.text == responses.get('answer_yes'):
        await message.answer(
            text = responses.get('fsm_input_email'),
            reply_markup = ReplyKeyboardRemove()
        )
        await state.set_state(UserInfo.input_email)
    else:
        await message.answer(
            text = responses.get('fsm_want_input_phone'),
            reply_markup = await make_keyboard_yes_or_no()
        )
        await state.set_state(UserInfo.want_input_phone)


@fsm_init_user_router.message(
    UserInfo.input_email,
    F.text.func(lambda message: re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$").match(message))
)
async def waiting_input_email(message: Message, state: FSMContext) -> None:
    await message.answer(
        text = responses.get('fsm_want_input_phone'),
        reply_markup = await make_keyboard_yes_or_no()
    )
    await state.update_data(email = remove_spaces(message.text))
    await state.set_state(UserInfo.want_input_phone)


async def show_total_info(message: Message, state: FSMContext):
    await message.answer(
        text = responses.get('is_total_info_correct'),
        reply_markup = await make_keyboard_yes_or_no()
    )
    await message.answer(
        '\n'.join(f'{matching_init_user_field[key]}: {value}' for key, value in (await state.get_data()).items())
    )
    await state.set_state(UserInfo.is_total_info_correct)


@fsm_init_user_router.message(
    UserInfo.want_input_phone,
    F.text.in_(
        [responses.get('answer_yes'), responses.get('answer_no')]
    )
)
async def waiting_want_input_phone(message: Message, state: FSMContext) -> None:
    if message.text == responses.get('answer_yes'):
        await message.answer(
            text = responses.get('fsm_input_phone'),
            reply_markup = ReplyKeyboardRemove()
        )
        await state.set_state(UserInfo.input_phone)
    else:
        await show_total_info(message = message, state = state)


@fsm_init_user_router.message(
    UserInfo.input_phone,
    F.text.func(lambda message: re.compile(r"^(?:\+7|8)\d{10}$").match(message))
)
async def waiting_input_phone(message: Message, state: FSMContext) -> None:
    await state.update_data(phone_number = remove_spaces(message.text))
    await show_total_info(message = message, state = state)


@fsm_init_user_router.message(
    UserInfo.is_total_info_correct,
    F.text.in_(
        [responses.get('answer_yes'), responses.get('answer_no')]
    )
)
async def waiting_is_total_info_correct(message: Message, state: FSMContext) -> None:
    if message.text == responses.get('answer_yes'):
        status = insert_data_into_students(await state.get_data(), message.from_user.id)
        await state.clear()

        match status:
            case 201:
                await message.answer(
                    text = responses.get('success_auth'),
                    reply_markup = await make_keyboard_get_data_and_upload_data()
                )
            case _:
                pass

    else:
        await message.answer(text = responses.get('refill_info_about_user'))
        await message.answer(
            text = responses.get('fsm_input_last_name'),
            reply_markup = ReplyKeyboardRemove()
        )
        await state.clear()
        await state.set_state(UserInfo.input_last_name)