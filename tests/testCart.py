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
        self.expectedCartItems = [self.expectedCartItem]
        self.assertEqual(0, len(self.__cart.cartitems))

        # when
        self.__cart.add(self.expectedCartItems)

        # then
        self.assertEqual(self.expectedArticlesQuantity, len(self.__cart.cartitems))
        self.assertEqual(self.expectedCartItem, self.__cart.cartitems[0])

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
        self.__cart.add(self.expectedCartItems)

        # then
        self.assertEqual(self.expectedArticlesQuantity, len(self.__cart.cartitems))
        self.assertEqual(self.expectedCartItems, self.__cart.cartitems)

    def test_add_onemultiplecartitems_success(self):
        # given
        # refer to Setup
        self.expectedArticlesQuantity: int = 1
        self.expectedArticles = ArticleGenerator.generate(self.expectedArticlesQuantity)

        self.expectedArticleInCartItem: int = 2
        self.expectedCartItem = CartItem(self.expectedArticles[0], self.expectedArticleInCartItem)
        self.expectedCartItems = [self.expectedCartItem]
        self.assertEqual(0, len(self.__cart.cartitems))

        # when
        self.__cart.add(self.expectedCartItems)

        # then
        self.assertEqual(self.expectedArticlesQuantity, len(self.__cart.cartitems))
        self.assertEqual(self.expectedCartItems, self.__cart.cartitems)

    def test_price_emptyCart_getPrice(self):

        self.expectedprice = 0.00

        self.assertEqual(self.expectedprice, self.__cart.price())

    def test_price_notEmptyCart_getPrice(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(5)
        self.cartitems = CartItem

        for articles in self.expectedArticles:
            self.__cart.add([self.cartitems(articles, 1)])
        self.expectedPrice = 30.00
        self.__cart.add([self.expectedPrice])
        # when

        # then

        self.assertEqual(self.expectedPrice, self.__cart.price())

    def test_priceaverage_uniquevalue_getaverage(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(5)
        self.cartitems = CartItem
        for articles in self.expectedArticles:
            self.__cart.add([self.cartitems(articles, 1)])
        self.__cart.add([self.cartitems])
        # when

        # then
        self.assertEqual(6, self.__cart.price(True))

    def test_doesexist_byid_true(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(10)
        self.cartitems = CartItem
        for articles in self.expectedArticles:
            self.__cart.add([self.cartitems(articles, 1)])
        self.__cart.add([self.cartitems])
        # when

        # then
        self.assertTrue(self.__cart.doesexist(10))

    def test_doesexist_byid_false(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(10)
        self.cartitems = CartItem
        for articles in self.expectedArticles:
            self.__cart.add([self.cartitems(articles, 1)])
        self.__cart.add([self.cartitems])
        # when

        # then
        self.assertTrue(self.__cart.doesexist(999))

    def test_cheapest_uniquevalue_getarticleid(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(10)
        self.cartitems = CartItem
        for articles in self.expectedArticles:
            self.__cart.add([self.cartitems(articles, 1)])
        self.__cart.add([self.cartitems])
        # when

        # then
        self.assertEqual(1, self.__cart.cheapest())
    # def test_mostexpensive_uniquevalue_getarticleid(self):
