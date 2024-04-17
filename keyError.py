users = {
    'name': 'Dilshod',
    'email': '<EMAIL>',
    'password': '<PASSWORD>',
    'phone': '+9112345678'
}
keyError = True
key = 'pdsd'

try:
    print(users[key])
except KeyError:
    print('User mavjud emas')

