class User:
    def __init__(self):
        self.username = None
        self.phone_number = None

    @property
    def username(self):
        return self.__username.lower()

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, number):
        self.__phone_number = number



