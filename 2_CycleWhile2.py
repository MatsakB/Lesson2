conversation = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую'}

while True:
    ask_user = input('Задай вопрос: ')
    if ask_user == 'Что делаешь?':
        print(conversation['Что делаешь?'])
    if ask_user == 'Как дела':
            print(conversation['Как дела?'])
            break
   