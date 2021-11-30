userData = {'name': input('Введите ваше имя: '),
            'surname': input('Введите вашу фамилию: '),
            'year': input('Введите ваш год рождения: '),
            'city': input('Введите название города в котором вы живете: '),
            'email': input('Введите ваше email: '),
            'phone': input('Введите ваш номер телефона: ')}

def printUserData(**kwargs):
  print(f"{'-' * 30}\nИмя: {kwargs['name']};\nФамилия: {kwargs['surname']};\nГод рождения: {kwargs['year']};\nМесто проживания: {kwargs['city']};\nEmail: {kwargs['email']};\nНомер телефона: {kwargs['phone']};")
printUserData(name=userData['name'], surname=userData['surname'], year=userData['year'], city=userData['city'], email=userData['email'], phone=userData['phone'] )