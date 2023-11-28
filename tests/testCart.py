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

    def test_add_firstSingleCartItem_success(self):
        # given
        # refer to setup
        self.expectedArticlesQuantity = 1
        self.expectedArticles = ArticleGenerator.generate(self.expectedArticlesQuantity)

        self.expectedArticleInCartItem = 1
        self.expectedCartItem = CartItem(self.expectedArticles[0], self.expectedArticleInCartItem)
        self.expectedCartItems = self.expectedCartItem
        self.assertEqual(0, len(self.__cart.cartitems))

        # when
        self.__cart.cartitems.append(self.expectedCartItem)

        # then
        self.assertEqual(self.expectedArticlesQuantity, len(self.__cart.cartitems))
        self.assertEqual([self.expectedCartItem], self.__cart.cartitems)

    def test_add_multipleSingleCartItems_success(self):
        # given
        # refer to setup
        self.expectedArticlesQuantity: int = 2
        self.expectedArticles = ArticleGenerator.generate(self.expectedArticlesQuantity)

        self.expectedQuantity1 = 1
        self.expectedCartItem1 = CartItem(self.expectedArticles[0], self.expectedQuantity1)

        self.expectedQuantity2 = 1
        self.expectedCartItem2 = CartItem(self.expectedArticles[1], self.expectedQuantity2)

        self.expectedCartItems = [self.expectedCartItem1, self.expectedCartItem2]
        self.assertEqual(0, len(self.__cart.cartitems))

        # when
        self.__cart.cartitems.append(self.expectedCartItems)

        # then
        self.assertEqual(self.expectedArticlesQuantity, len(self.__cart.cartitems))
        self.assertEqual([self.expectedCartItems], self.__cart.cartitems)

    # def test_add_onemultiplecartitems_success(self):

    # def test_price_emptycart_getprice(self):
    #    expectedprice = 0.00

    # def test_price_notemptycart_getprice(self):

    # def test_priceaverage_uniquevalue_getaverage(self):

    # def test_doesexist_byid_true(self):

    # def test_doesexist_byid_false(self):

    # def test_cheapest_uniquevalue_getarticleid(self):

    # def test_mostexpensive_uniquevalue_getarticleid(self):
