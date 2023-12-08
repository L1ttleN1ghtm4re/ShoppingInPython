import this
from shopping.cartItem import CartItem


class Cart:
    # region private attributes
    __cartItems = []

    # endregion private attributes

    def __init__(self):
        self.__cartItems = []

    def add(self, cartitems_to_add):
        for cartItem in cartitems_to_add:
            self.__cartItems.append(cartItem)

    def remove(self):
        raise NotImplementedError

    @property
    def cartitems(self):
        return self.__cartItems

    def price(self, average: bool = False):
        currentcartprice = 0.00
        currentcartiemlen = len(self.__cartItems)
        for self.cartItem in self.__cartItems:
            currentcartprice = self.__cartItems[0].article.price
        if average:
            return currentcartprice / currentcartiemlen
        return currentcartprice

    def doesexist(self, articleid):
        if self.getarticlebyid(articleid) is None:
            return False
        return True

    def cheapest(self):
        currentchepeastarticleid = self.__cartItems[0].article.id
        for cartItem in self.__cartItems:
            if cartItem.article.price < this.getarticlebyid(currentchepeastarticleid).price:
                currentchepeastarticleid = cartItem.article.id
        return currentchepeastarticleid

    def mostexpensive(self):
        currentchepeastarticleid = self.__cartItems[0].article.id
        for cartItem in self.__cartItems:
            if cartItem.article.price > this.getarticlebyid(currentchepeastarticleid).price:
                currentchepeastarticleid = cartItem.article.id
        return currentchepeastarticleid

    def getarticlebyid(self, articleid):
        for cartItem in self.__cartItems:
            if cartItem.article.id == articleid:
                return cartItem.article
        return None


class CartException(Exception):
    pass


class ArticleNotFoundException(CartException):
    pass
