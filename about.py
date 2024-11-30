import random
import string


def generate_password(length: int = 12,
                      use_lowercase: bool = True,
                      use_uppercase: bool = True,
                      use_digits: bool = True,
                      use_special_chars: bool = True) -> str:
    """
    Генерируем пароль с нужными параметрами.

    Тут можно выбрать, какого размера будет пароль и какие символы в нём использовать:
    - длина задаётся числом
    - можно включить или выключить строчные и заглавные буквы, цифры и спецсимволы

    Параметры:
    length (int): Длина пароля (по умолчанию 12 символов).
    use_lowercase (bool): Включить строчные буквы? (True или False).
    use_uppercase (bool): Включить заглавные буквы? (True или False).
    use_digits (bool): Включить цифры? (True или False).
    use_special_chars (bool): Включить спецсимволы? (True или False).

    Возвращает:
    str: Случайный пароль, который соответствует заданным настройкам.

    Если ничего не выбрано (все флаги False), ругнётся ошибкой.
    """
    chars = ""

    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    if not chars:
        raise ValueError("Ну и что ты хочешь? Ты же ничего не выбрал!")

    return ''.join(random.choice(chars) for _ in range(length))


if __name__ == "__main__":
    try:
        password_length = int(input('Введите длину пароля: '))
        use_lowercase = input('Использовать строчные буквы? (y/n): ').lower() == 'y'
        use_uppercase = input('Использовать заглавные буквы? (y/n): ').lower() == 'y'
        use_digits = input('Использовать цифры? (y/n): ').lower() == 'y'
        use_special_chars = input('Использовать специальные символы? (y/n): ').lower() == 'y'

        password = generate_password(password_length, use_lowercase, use_uppercase, use_digits, use_special_chars)

        print(f'Сгенерированный пароль: {password}')

    except ValueError as e:
        print(e)