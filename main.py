def get_unicode_from_smiley(smiley):
    """Получает Unicode-код из смайлика."""
    return ord(smiley)


def get_smiley_from_unicode(unicode_code):
    """Получает смайлик из Unicode-кода."""
    return chr(unicode_code)


def main():
    # Список смайлов
    smileys = ['😀', '😂', '🤣']

    # Перебираем смайлы и выводим их Unicode-коды
    for smiley in smileys:
        unicode_code = get_unicode_from_smiley(smiley)
        print(f"Смайлик: {smiley}, Unicode: {unicode_code}")

        # Преобразуем Unicode-код обратно в смайлик
        smiley_from_unicode = get_smiley_from_unicode(unicode_code)
        print(f"Смайлик из Unicode: {smiley_from_unicode}\n")


if __name__ == "__main__":
    main()
