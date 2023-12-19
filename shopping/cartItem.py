from shopping.article import Article


class CartItem:

    # region private attributes
    __article: Article = Article
    __quantity: int = 0
    __foradultonly: bool
    # endregion private attributes

    # region public methods
    def __init__(self, article: Article, quantity: int, foradultonly: bool = False):
        self.__article: Article = article
        self.__quantity: int = quantity
        self.__foradultonly: bool = foradultonly

    @property
    def article(self) -> Article:
        return self.__article

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 1:
            raise WrongQuantityException
        self.__quantity: int = value
    # endregion public methods

    @property
    def for_adult_only(self) -> bool:
        return self.__foradultonly

    @for_adult_only.setter
    def for_adult_only(self, value) -> None:
        self.__foradultonly = value


class CartItemException(Exception):
    pass


class WrongQuantityException(CartItemException):
    pass
