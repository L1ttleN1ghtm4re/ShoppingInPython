import unittest
from tests.articleGenerator import ArticleGenerator
from shopping.cartItem import CartItem
from shopping.cart import Cart


class TestCart(unittest.TestCase):
    # region private attributes
    __cart = Cart
    # endregion private attributes

    def setUp(self):
        self.__cart = Cart()

    def test_add_firstsinglecartitem_success(self):
        # given
        # refer to setup
        self.expected_articles_quantity: int = 1
        self.expected_articles: list = [ArticleGenerator.generate(self.expected_articles_quantity)]

        self.expected_article_in_cartitem: int = 1
        self.expected_cartitem: CartItem = CartItem(self.expected_articles[0], self.expected_article_in_cartitem)
        self.expected_cartitems: [CartItem] = self.expected_cartitem
        self.assertEqual(0, len(self.__cart.cartitems))

        # when
        self.__cart.cartitems.append(self.expected_cartitems)
        # then
        self.assertEqual(self.expected_articles_quantity, len(self.__cart.cartitems))
        self.assertEqual(self.__cart.cartitems, self.expected_cartitems)

    # def test_add_multipleSingleCartItems_success(self):

    # def test_add_onemultiplecartitems_success(self):

    # def test_price_emptycart_getprice(self):
    #    expectedprice = 0.00

    # def test_price_notemptycart_getprice(self):

    # def test_priceaverage_uniquevalue_getaverage(self):

    # def test_doesexist_byid_true(self):

    # def test_doesexist_byid_false(self):

    # def test_cheapest_uniquevalue_getarticleid(self):

    # def test_mostexpensive_uniquevalue_getarticleid(self):
