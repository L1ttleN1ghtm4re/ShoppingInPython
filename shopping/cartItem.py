from shopping.article import Article


class CartItem:

    def __init__(self, article_, quantity_):
        self.__article = Article
        self.__quantity = quantity_

    @property
    def article(self):
        return self.__article

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value


class CartItemException(Exception):
    pass


class WrongQuantityException(CartItemException):
    pass
