from shopping.cartItem import CartItem


class Cart:
    # region private attributes
    __cartItems: [CartItem] = []
    # endregion private attributes

    # region public methods
    def __init__(self):
        self.__cartItems: [CartItem] = []

    def add(self, cart_items_to_add: [CartItem]) -> None:
        for cartItem in cart_items_to_add:
            self.__cartItems.append(cartItem)

    def remove(self) -> None:
        raise NotImplementedError

    @property
    def cart_items(self) -> [CartItem]:
        return self.__cartItems

    def price(self, average: bool = False) -> float:
        current_cart_price = 0.00
        for cartItem in self.__cartItems:
            current_cart_price += cartItem.article.price * cartItem.quantity
        if average:
            return current_cart_price / len(self.__cartItems)
        return current_cart_price

    def does_exist(self, article_id: int) -> bool:
        if self.get_article_by_id(article_id) is None:
            return False
        return True

    def cheapest(self) -> int:
        current_cheapest_article_id = self.__cartItems[0].article.id
        for cartItem in self.__cartItems:
            if cartItem.article.price < self.get_article_by_id(current_cheapest_article_id).price:
                current_cheapest_article_id = cartItem.article.id
        return current_cheapest_article_id

    def most_expensive(self):
        current_cheapest_article_id = self.__cartItems[0].article.id
        for cartItem in self.__cartItems:
            if cartItem.article.price > self.get_article_by_id(current_cheapest_article_id).price:
                current_cheapest_article_id = cartItem.article.id
        return current_cheapest_article_id

    def get_article_by_id(self, article_id):
        for cartItem in self.__cartItems:
            if cartItem.article.id == article_id:
                return cartItem.article
        return None
    # endregion public methods


class CartException(Exception):
    pass


class ArticleNotFoundException(CartException):
    pass
