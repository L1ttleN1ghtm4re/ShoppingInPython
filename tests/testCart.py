import unittest
from tests.articleGenerator import ArticleGenerator
from shopping.cart import *


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

    def test_add_oneMultipleCartItems_success(self):
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

        self.expectedPrice = 0.00

        self.assertEqual(self.expectedPrice, self.__cart.price())

    def test_price_notEmptyCart_getPrice(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(5)
        self.cartItems = CartItem

        for articles in self.expectedArticles:
            self.__cart.add([self.cartItems(articles, 1)])
        self.expectedPrice = 30.00
        self.__cart.add([self.expectedPrice])
        # when

        # then

        self.assertEqual(self.expectedPrice, self.__cart.price())

    def test_priceAverage_uniqueValue_getAverage(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(5)
        self.cartItems = CartItem
        for articles in self.expectedArticles:
            self.__cart.add([self.cartItems(articles, 1)])
        self.__cart.add([self.cartItems])
        # when

        # then
        self.assertEqual(6, self.__cart.price(True))

    def test_doesExist_byid_true(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(10)
        self.cartItems = []
        for articles in self.expectedArticles:
            self.__cart.add([self.cartItems(articles, 1)])
        self.__cart.add([self.cartItems])
        # when

        # then
        self.assertTrue(self.__cart.doesexist(10))

    def test_doesExist_byid_false(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(10)
        self.cartItems = []
        for article in self.expectedArticles:
            cartitem = CartItem(article, 1)
            self.cartItems.append(cartitem)
        self.__cart.add(self.cartItems)
        # when

        # then
        self.assertFalse(self.__cart.doesexist(999))

    def test_cheapest_uniqueValue_getArticleId(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(10)
        self.cartItems = []
        for articles in self.expectedArticles:
            self.__cart.add([self.cartItems(articles, 1)])
        self.__cart.add([self.cartItems])
        # when

        # then
        self.assertEqual(1, self.__cart.cheapest())

    def test_mostExpensive_uniqueValue_getArticleId(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(10)
        self.cartItems = []
        for articles in self.expectedArticles:
            self.__cart.add([self.cartItems(articles, 1)])
        self.__cart.add([self.cartItems])
        # when

        # then
        self.assertEqual(10, self.__cart.mostexpensive())

    def ApplyDiscountById_ArticleExists_PriceUpdated(self):
        # given
        self.discountToApply = 0.1
        self.articleToApplyDiscount = 45
        self.expectedArticles = ArticleGenerator.generate(5)
        self.cartItems = []
        for articles in self.expectedArticles:
            self.__cart.add([self.cartItems(articles, 1)])
        self.__cart.add([self.cartItems])
        # when
        self.assertEqual(29.60, self.__cart.price())
        # then
        # throw exception

    def ApplyDiscountById_ArticleDoesNotExist_ThrowException(self):
        # given
        self.discountToApply = 0.1
        self.articleToApplyDiscount = 45
        self.expectedArticles = ArticleGenerator.generate(5)
        self.cartItems = []
        for articles in self.expectedArticles:
            self.__cart.add([self.cartItems(articles, 1)])
        self.__cart.add([self.cartItems])
        # when
        self.assertRaises(ArticleNotFoundException)
        # then
        # throw exception
