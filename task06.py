# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def cap_all_ascii_words():
    """
    Запрашивает ввод слов, возвращает только слова из маленьких латинских букв. Первую букву делает большой.

    Функция запрашивает у пользователя слова через пробел.
    Возвращает только те слова, которые состоят из маленьких латинских букв.
    В возвращаемых словах первая буква будет большой.
    """
    result = []
    sentence = input('Введите слова из маленьких букв. Слова разделяйте пробелами: ')
    list_from_sen = sentence.split()
    for word in list_from_sen:
        for letter in word:  # В цикле проверяем каждую букву на вхождение в диапазон маленьких латинских букв
            if ord(letter) < 97 or ord(letter) > 122:
                break  # Если в слове есть неподходящая буква, выходим из цикла, переходим к следующему слову
        else:
            result.append(word.capitalize())  # Добавляем слово в итоговый список, только если вышли из цикла без break

    return ' '.join(result)


print(cap_all_ascii_words())
