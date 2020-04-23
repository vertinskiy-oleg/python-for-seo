data = input('Enter data: ')


if type(data) is int:
    print('Data in Integer')

elif type(data) == str:
    print('You enter string')


if data:
    print(f'You enter this data: {data}')
else:
    quit()


if data.isdigit():
    print('This is digit')

elif 'http' in data:
    print('This is URL')

elif '.com' in data:
    print('This is domain')

else:
    print("I don't know this sh#t type...")
