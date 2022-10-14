import datetime
import utilities
# import database


class Post:
    def __init__(self):
        self.__user = None
        self.__creation_time = datetime.datetime.now()
        self.__text = None

    @property
    def user(self):
        return self.__user.lower()

    @user.setter
    def user(self, value):

        user_record = utilities.search_user("person", value)
        if not user_record:
            raise TypeError("User not found.")
        self.__user = user_record[1]  # --> 1st index represents phone number from person class

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
