from shopping.cartItem import CartItem


class Cart:
    # region private attributes
    _cartItems = CartItem
    # endregion private attributes

    def add(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError

    def cartitems(self):
        raise NotImplementedError

    def doesexist(self):
        raise NotImplementedError

    def cheapest(self):
        raise NotImplementedError

    def mostexpensive(self):
        raise NotImplementedError
