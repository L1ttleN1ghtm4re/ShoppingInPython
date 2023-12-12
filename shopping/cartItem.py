from shopping.article import Article


class CartItem:

    # region private attributes
    __article: Article = Article
    __quantity: int = 0
    # endregion private attributes

    def __init__(self, article, quantity):
        self.__article = article
        self.__quantity = quantity

    @property
    def article(self) -> Article:
        return self.__article

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, value) -> None:
        self.__quantity = value


class CartItemException(Exception):
    pass


class WrongQuantityException(CartItemException):
    pass
