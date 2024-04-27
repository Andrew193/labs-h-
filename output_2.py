class PhoneNumber:
    def __init__(self, phone, phone_code):
        self.phone = phone
        self.phone_code = phone_code

    def get_full_number(self):
        return self.phone_code + self.phone

class User:
    type_engineer = 1
    type_manager = 2

    def __init__(self, name, age, type, phone_number):
        self.name = name
        self.age = age
        self.type = type
        self.phone_number = phone_number

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.type)
        print("Phone:", self.phone_number.get_full_number())

# Приклад використання класу
user = User("John", 25, User.type_engineer, PhoneNumber("9379992", "050"))
user.print_details()