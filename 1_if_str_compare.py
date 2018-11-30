row1 = input('type smth ')
row2 = input('type smth ')
if type (row1) is not str and type(row2) is not str:
    print('0')
elif row1 is row2:
    print('1')
elif len(row1) > len(row2):
    print('2')
elif row2 is 'learn':
    print('3')
