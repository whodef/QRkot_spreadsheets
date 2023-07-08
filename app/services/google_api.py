import copy
from datetime import datetime as dt
from typing import Tuple
from aiogoogle import Aiogoogle

from app.core.config import settings
from . import constants as c


async def spreadsheets_create(
        wrapper_services: Aiogoogle
) -> Tuple[str, str]:
    """
    Создаёт таблицу.
    """
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = copy.deepcopy(c.SPREADSHEET_BODY)
    spreadsheet_body['properties']['title'] = c.SPREADSHEET_TITLE.format(
        now_date_time=dt.now().strftime(c.FORMAT)
    )
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )

    return response['spreadsheetId'], response['spreadsheetUrl']


async def set_user_permissions(
    spreadsheet_id: str, wrapper_services: Aiogoogle
) -> None:
    """
    Устанавливает права доступа к таблице.
    """
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email,
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id, json=permissions_body, fields='id'
        )
    )


async def spreadsheets_update_value(
    spreadsheet_id: str, charity_projects: list, wrapper_services: Aiogoogle
) -> None:
    """
    Записывает данные в таблицу.
    """
    service = await wrapper_services.discover('sheets', 'v4')
    table_header = copy.deepcopy(c.TABLE_HEADER)
    table_header[0][1] = dt.now().strftime(c.FORMAT)
    table_values = [
        *table_header,
        *[list(map(str, project.values())) for project in charity_projects],
    ]
    row_count = len(table_values)
    column_count = len(max(table_values, key=len))

    if row_count > c.ROW_COUNT:
        raise ValueError(
            'Количество строк превышает допустимое значение: '
            f'Максимально: {c.ROW_COUNT}, передано: {row_count}'
        )

    if column_count > c.COLUMN_COUNT:
        raise ValueError(
            'Количество столбцов превышает допустимое значение:'
            f'Максимально: {c.COLUMN_COUNT}, передано: {column_count}'
        )

    total_cells = row_count * column_count

    if total_cells > c.TOTAL_CELL_COUNT:
        raise ValueError(
            'Количество ячеек превышает допустимое значение: '
            f'Максимально: {c.TOTAL_CELL_COUNT}, передано: {total_cells}'
        )

    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=(
                f'R1C1:R{row_count}C{column_count}'
            ),
            valueInputOption=c.INPUT_OPTION,
            json={'majorDimension': c.MAJOR_DIMENSION, 'values': table_values},
        )
    )
