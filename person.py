class User:

    def __init__(self, username, phone_number, age):

        self.username = username
        self.phone_number = phone_number
        self.age = age

    # USERNAME VALIDATION
    # GETTER
    @property
    def username(self):

        return self._username

    # SETTER
    @username.setter
    def username(self, username_value):

        self._username = username_value.lower()

    # AGE VERIFICATION
    # GETTER
    @property
    def age(self):

        return self._age

    # SETTER
    @age.setter
    def age(self, age_value):

        if type(age_value) is not int:
            raise TypeError('Age must be a valid number!')

        if age_value > 0:
            raise ValueError('Your age cannot be a negative number!')

        elif 13 >= age >= 0:
            raise ValueError(
                "Sorry, your age is below our eligibility policies")

        else:
            self._age = age_value

    # PHONE NUMBER VALIDATION BASED ON +989123456789
    # GETTER

    @property
    def phone_number(self):

        return self._phone_number

    # SETTER
    @phone_number.setter
    def phone_number(self, phone_number_value):

        phone_number = [x for x in str(phone_number_value)]

        if len(phone_number_value) != 13:

            if phone_number[0] == '+' and phone_number[1] == '9' and phone_number[2] == '8':

                self._phone_number = phone_number_value

            raise ValueError("Please enter a valid number!")

        raise ValueError("Please enter a valid number!")
