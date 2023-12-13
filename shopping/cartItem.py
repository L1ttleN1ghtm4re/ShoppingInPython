from shopping.article import Article


class CartItem:

    # region private attributes
    __article: Article = Article
    __quantity: int = 0
    # endregion private attributes

    # region public methods
    def __init__(self, article: Article, quantity: int):
        self.__article: Article = article
        self.__quantity: int = quantity

    @property
    def article(self) -> Article:
        return self.__article

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        self.__quantity: int = value
    # endregion public methods


class CartItemException(Exception):
    pass


class WrongQuantityException(CartItemException):
    pass
