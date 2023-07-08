
# JWT

JWT_LIFETIME_SECONDS = 3600


# User settings

TOKEN_URL = 'auth/jwt/login'

PASSWORD_GE_THREE = 'Password should be at least 3 characters'

PASSWORD_NE_EMAIL = 'Password should not contain e-mail'


# Model constants

DEFAULT_INVESTED_AMOUNT = 0

CHARITY_PROJECT_NAME_MAX = 100

CHARITY_PROJECT_MIN = 1


# Error messages

PROJECT_NAME_ALREADY_EXISTS = 'Проект с таким именем уже существует!'

PROJECT_NOT_FOUND = 'Проект не найден'

DELETION_NOT_ALLOWED = 'В проект были внесены средства, не подлежит удалению!'

PATCH_NOT_ALLOWED = 'Закрытый проект нельзя редактировать!'

INVALID_FULL_AMOUNT = 'Нельзя установить новую целевую сумму меньше уже внесенной'


# For Google Sheets API

FORMAT = '%Y/%m/%d %H:%M:%S'

SPREADSHEET_TITLE = 'Отчет на {now_date_time}'

MAJOR_DIMENSION = 'ROWS'

INPUT_OPTION = 'USER_ENTERED'

ROW_COUNT = 100

COLUMN_COUNT = 11

TOTAL_CELL_COUNT = 5000

TABLE_HEADER = [
    ['Отчет от', ''],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание'],
]

SPREADSHEET_BODY = dict(
    properties=dict(title='', locale='ru_RU'),
    sheets=[dict(properties=dict(
        sheetType='GRID',
        sheetId=0,
        title='Лист1',
        gridProperties=dict(
            rowCount=ROW_COUNT, columnCount=COLUMN_COUNT
        ),
    ))],
)
