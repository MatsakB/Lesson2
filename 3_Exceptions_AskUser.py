conversation = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую'}
try:
    while True:
        ask_user = input('Задай вопрос: ')
        if ask_user == 'Как дела':
            print(conversation['Как дела?'])
        if ask_user == 'Что делаешь?':
            print(conversation['Что делаешь?'])
            break 
except KeyboardInterrupt:
    print('Пока')