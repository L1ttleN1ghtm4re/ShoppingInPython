
class Article:

    # region private attributes
    __id = 0
    __description = ""
    __price = 0.0
    # TODO: attributes indicate type ex: __price:float =0.0

    # endregion private attributes

    def __init__(self, id_, description, price):
        self.__id = id_
        self.__description = description
        self.__price = price

    @property
    def id(self):
        return self.__id
    # TODO : indicate return type ex: def id(self) -> int:

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value
    # NOTE : could indicate there's none to return ex : -> none:


class ArticleException(Exception):
    pass
# should have his own page for any exception


class SpecialCharInDescriptionException(ArticleException):
    pass


class TooShortDescriptionException(ArticleException):
    pass


class TooLongDescriptionException(ArticleException):
    pass


# TODO : change place
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
