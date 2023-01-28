from datetime import date


def iin_to_datetime(iin: str) -> date:
    if not (len(iin) == 12):
        raise AttributeError('Длина ИИН должна быть 12 символов') 
    if not iin.isnumeric():
        raise AttributeError('ИИН должен содержать только цифры')

    birth_date = iin[:6]
    year = birth_date[:2]
    month = int(birth_date[2:4])
    day = int(birth_date[4:6])

    if int(year) < 25:
        year = int(f'{20}{year}')
    else:
        year = int(f'{19}{year}')

    result = date(year, month, day)
    return result