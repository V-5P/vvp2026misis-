while True:
    choice = input('Введите номер уровня (1-5) или exit для выхода: ')
    if choice.lower() == 'exit':
        print("До свидания!")
        break
    if choice == '1':
        print('Уровень 1: методы upper, lower, capitalize')
        method = input('Введите метод (lower / upper / capitalize) или exit: ').lower()
        if method == 'exit':
            break
        if method not in ('lower', 'upper', 'capitalize'):
            print("Неверный метод.")
            continue
        word = input('Введите строку: ')
        if method == 'lower':
            print(word.lower())
        elif method == 'upper':
            print(word.upper())
        elif method == 'capitalize':
            print(word.capitalize())
    elif choice == '2':
        print('Уровень 2: методы find, replace, count')
        method = input('Введите метод (find / replace / count) или exit: ').lower()
        if method == 'exit':
            break
        if method not in ('find', 'replace', 'count'):
            print("Неверный метод.")
            continue
        word = input('Введите строку: ')
        sub_word = input('Введите подстроку: ')
        if method == 'find':
            if sub_word not in word: 
                print('Подстрока не найдена.')
            else:
                print(word.find(sub_word))
        elif method == 'replace':
            new_sub = input('Введите подстроку для замены: ')
            print(word.replace(sub_word, new_sub))
        elif method == 'count':
            print(word.count(sub_word))
    elif choice == '3':
        print('Уровень 3: методы split, join')
        method = input('Введите метод (split / join) или exit: ').lower()
        if method == 'exit':
            break
        if method not in ('split', 'join'):
            print("Неверный метод.")
            continue
        if method == 'split':
            word = input('Введите строку: ')
            sub_word = input('Введите разделитель: ')
            if sub_word not in word:
                print("Разделитель в строке отсутствует.")
            else:
                print(word.split(sub_word))
        elif method == 'join':
            word = input('Введите строку: ')
            sub_word = input('Введите разделитель: ')
            print(sub_word.join(word))
    elif choice == '4':
        print('Уровень 4: методы isdigit, isalpha, strip, format')
        method = input('Введите метод (isdigit / isalpha / strip / format) или exit: ').lower()
        if method == 'exit':
            break
        if method not in ('isdigit', 'isalpha', 'strip', 'format'):
            print("Неверный метод.")
            continue
        word = input('Введите строку: ')
        if method == 'isdigit':
            print(word.isdigit())
        elif method == 'isalpha':
            print(word.isalpha())
        elif method == 'strip':
            print(word.strip())
        elif method == 'format':
            clean = word.strip()
            dot_count = clean.count('.')
            is_valid = dot_count <= 1 and clean.replace('.', '').isdigit() and len(clean) > 0
            if is_valid:
                num = float(clean)
                print("{:.2f}".format(num))
            else:
                print("Ошибка: введено не число, невозможно отформатировать как {:.2f}.")
    elif choice == '5':
        result = ' pYtHon;is;AWESome '.strip().replace(';', ' ').upper().capitalize()
        print(result)
        print("Разбор: strip → убрать пробелы; replace → заменить ';' на пробел; upper → всё в верхний регистр; capitalize → первая буква заглавная, остальные строчные.")

    else:
        print("Неверный номер уровня. Введите число от 1 до 5.")

          
