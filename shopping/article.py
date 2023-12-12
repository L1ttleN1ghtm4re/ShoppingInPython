
class Article:

    # region private attributes
    __id_: int = 0
    __description: str = ""
    __price: float = 0.0
    # endregion private attributes

    def __init__(self, id_: int, description: str, price: float) -> None:
        self.__id_: int = id_
        self.__description: str = description
        self.__price: float = price

    @property
    def id(self) -> int:
        return self.__id_

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        self.__description: str = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        self.__price: float = value


def check_description(description_to_check: str) -> bool:

    special_chars: [str] = ['!', '*', '+', '/']

    for special_char in special_chars:
        if special_char in description_to_check:
            raise ErrorSpecialCharInDescriptionException()

    if len(description_to_check.split(' ')) == 1:
        raise ErrorTooShortDescriptionException()

    if len(description_to_check) > 50:
        raise ErrorTooLongDescriptionException()

    return True


class ArticleException(Exception):
    pass
# should have his own page for any exception


class ErrorSpecialCharInDescriptionException(ArticleException):
    pass


class ErrorTooShortDescriptionException(ArticleException):
    pass


class ErrorTooLongDescriptionException(ArticleException):
    pass


try:
    check_description("Description to check.")
except ErrorSpecialCharInDescriptionException:
    print("Special character founded in description.")
except ErrorTooShortDescriptionException:
    print("This description is to short.")
except ErrorTooLongDescriptionException:
    print("This description is to long.")
