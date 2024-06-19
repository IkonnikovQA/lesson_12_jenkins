from tests.path import path_for_picture as path


class UserStudent:
    def __init__(self,
                 first_name: str = 'Alexey',
                 last_name: str = 'Ivanov',
                 gender: str = 'Male',
                 year_birthday: str = '1990',
                 month_birthday: str = 'February',
                 day_birthday: str = '006',
                 subject: str = 'Maths',
                 hobby: str = 'Sports',
                 path_for_picture: str = path,
                 phone: str = '1234567890',
                 address: str = 'my_address',
                 state: str = 'NCR',
                 city: str = 'Noida',
                 ):
        self.name_image = 'meme.jpg'
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{self.first_name.lower()}_{self.last_name.lower()}@mail.com'
        self.gender = gender
        self.year_birthday = year_birthday
        self.month_birthday = month_birthday
        self.day_birthday = day_birthday
        self.subject = subject
        self.hobby = hobby
        self.path_for_picture = path_for_picture
        self.phone = phone
        self.address = address
        self.state = state
        self.city = city