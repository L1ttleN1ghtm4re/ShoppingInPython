
class Article:
    def __init__(self, id_, description, price):
        self.__id = id_
        self.__description = description
        self.__price = price

    @property
    def id(self):
        return self.__id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def price(self):
        return self.__price


class ArticleException(Exception):
    pass


class SpecialCharInDescriptionException(ArticleException):
    pass


class TooShortDescriptionException(ArticleException):
    pass


class TooLongDescriptionException(ArticleException):
    pass


def check_description(description_to_check):

    special_chars = ['!', '*', '+', '/']

    for special_char in special_chars:
        if special_char in description_to_check:
            raise SpecialCharInDescriptionException()

    if len(description_to_check.split(' ')) == 1:
        raise TooShortDescriptionException()

    if len(description_to_check) > 50:
        raise TooLongDescriptionException()

    return True


# Appel de la fonction avec gestion des exceptions
try:
    check_description("Description à vérifier")
except SpecialCharInDescriptionException:
    print("Caractère spécial trouvé dans la description.")
except TooShortDescriptionException:
    print("La description est trop courte.")
except TooLongDescriptionException:
    print("La description est trop longue.")
