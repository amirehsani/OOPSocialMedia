class User:

    def __init__(self, username, phone_number, age):
        self.username = None
        self.phone_number = None
        self.age = age

    @property
    @ageVerification.getter
    def ageVerification(self):

        return self.__age = age

    @ageVerification.setter
    def ageVerification(self, a):

        if self.age < 18:
            raise ValueError("Sorry, your age is below our eligibility policies.")

        self.age = age

    @property
    def username(self):
        return self.__username.lower()

    @username.setter
    def username(self, value):
        self.__username = username

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, number):
        self.__phone_number = number
