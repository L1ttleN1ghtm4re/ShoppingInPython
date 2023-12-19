import unittest

from tests.articleGenerator import ArticleGenerator
from shopping.cart import *
from shopping.cartItem import *


class TestCart(unittest.TestCase):
    # region private attributes

    __cart: Cart = Cart
    # endregion private attributes

    def setUp(self):
        self.__cart: Cart = Cart()

    _cart: Cart
    # endregion private attributes

    def test_add_firstSingleCartItem_success(self):
        # given
        # refer to setup
        self.expectedArticlesQuantity: int = 1
        self.expectedArticles: [Article] = ArticleGenerator.generate(self.expectedArticlesQuantity)

        self.expectedArticleInCartItem: int = 1
        self.expectedCartItem: CartItem = CartItem(self.expectedArticles[0], self.expectedArticleInCartItem)
        self.expectedCartItems: [CartItem] = [self.expectedCartItem]
        self.assertEqual(0, len(self.__cart.cart_items))

        # when
        self.__cart.add(self.expectedCartItems)

        # then
        self.assertEqual(self.expectedArticlesQuantity, len(self.__cart.cart_items))
        self.assertEqual(self.expectedCartItem, self.__cart.cart_items[0])

    def test_add_multipleSingleCartItems_success(self):
        # given
        # refer to setup
        self.expectedArticlesQuantity: int = 2
        self.expectedArticles: [Article] = ArticleGenerator.generate(self.expectedArticlesQuantity)

        self.expectedQuantity1: int = 1
        self.expectedCartItem1: CartItem = CartItem(self.expectedArticles[0], self.expectedQuantity1)

        self.expectedQuantity2: int = 1
        self.expectedCartItem2: CartItem = CartItem(self.expectedArticles[1], self.expectedQuantity2)

        self.expectedCartItems: [CartItem] = [self.expectedCartItem1, self.expectedCartItem2]
        self.assertEqual(0, len(self.__cart.cart_items))

        # when
        self.__cart.add(self.expectedCartItems)

        # then
        self.assertEqual(self.expectedArticlesQuantity, len(self.__cart.cart_items))
        self.assertEqual(self.expectedCartItems, self.__cart.cart_items)

    def test_add_oneMultipleCartItems_success(self):
        # given
        # refer to Setup
        self.expectedArticlesQuantity: int = 1
        self.expectedArticles: [Article] = ArticleGenerator.generate(self.expectedArticlesQuantity)

        self.expectedArticleInCartItem: int = 2
        self.expectedCartItem: CartItem = CartItem(self.expectedArticles[0], self.expectedArticleInCartItem)
        self.expectedCartItems: [CartItem] = [self.expectedCartItem]
        self.assertEqual(0, len(self.__cart.cart_items))

        # when
        self.__cart.add(self.expectedCartItems)

        # then
        self.assertEqual(self.expectedArticlesQuantity, len(self.__cart.cart_items))
        self.assertEqual(self.expectedCartItems, self.__cart.cart_items)

    def test_price_emptyCart_getPrice(self):

        self.expectedPrice: float = 0.00

        self.assertEqual(self.expectedPrice, self.__cart.price())

    def test_price_notEmptyCart_getPrice(self):
        # given
        self.expectedArticles = ArticleGenerator.generate(5)
        self.cartItems: [CartItem] = []

        for article in self.expectedArticles:
            cart_item: CartItem = CartItem(article, 1)
            self.cartItems.append(cart_item)
        self.expectedPrice: float = 30.00
        self.__cart.add(self.cartItems)

        # when

        # then

        self.assertEqual(self.expectedPrice, self.__cart.price())

    def test_priceAverage_uniqueValue_getAverage(self):
        # given
        self.expectedArticles: [Article] = ArticleGenerator.generate(5)
        self.cartItems: [CartItem] = []
        for article in self.expectedArticles:
            cart_item: CartItem = CartItem(article, 1)
            self.cartItems.append(cart_item)
        self.__cart.add(self.cartItems)
        # when

        # then
        self.assertEqual(6, self.__cart.price(True))

    def test_doesExist_byid_true(self):
        # given
        self.expectedArticles: [Article] = ArticleGenerator.generate(10)
        self.cartItems: [CartItem] = []
        for article in self.expectedArticles:
            cart_item: CartItem = CartItem(article, 1)
            self.cartItems.append(cart_item)
        self.__cart.add(self.cartItems)
        # when

        # then
        self.assertTrue(self.__cart.does_exist(10))

    def test_doesExist_byid_false(self):
        # given
        self.expectedArticles: [Article] = ArticleGenerator.generate(10)
        self.cartItems: [CartItem] = []
        for article in self.expectedArticles:
            cart_item: CartItem = CartItem(article, 1)
            self.cartItems.append(cart_item)
        self.__cart.add(self.cartItems)
        # when

        # then
        self.assertFalse(self.__cart.does_exist(999))

    def test_cheapest_uniqueValue_getArticleId(self):
        # given
        self.expectedArticles: [Article] = ArticleGenerator.generate(10)
        self.cartItems: [CartItem] = []
        for article in self.expectedArticles:
            cart_item: CartItem = CartItem(article, 1)
            self.cartItems.append(cart_item)
        self.__cart.add(self.cartItems)
        # when

        # then
        self.assertEqual(1, self.__cart.cheapest())

    def test_mostExpensive_uniqueValue_getArticleId(self):
        # given
        self.expectedArticles: [Article] = ArticleGenerator.generate(10)
        self.cartItems: [CartItem] = []
        for article in self.expectedArticles:
            cart_item: CartItem = CartItem(article, 1)
            self.cartItems.append(cart_item)
        self.__cart.add(self.cartItems)
        # when

        # then
        self.assertEqual(10, self.__cart.most_expensive())

    def test_ApplyDiscountById_ArticleExists_PriceUpdated(self):
        # given
        self.discountToApply: float = 0.1
        self.articleToApplyDiscount: int = 45
        self.expectedArticles: [Article] = ArticleGenerator.generate(5)
        self.cartItems: [CartItem] = []
        for articles in self.expectedArticles:
            self.__cart.add(self.cartItems(articles, 1))
        self.__cart.add([self.cartItems])
        # when
        self.assertEqual(29.60, self.__cart.price())
        # then
        # throw exception

    def test_ApplyDiscountById_ArticleDoesNotExist_ThrowException(self):
        # given
        self.discountToApply: float = 0.1
        self.articleToApplyDiscount: int = 45
        self.expectedArticles: [Article] = ArticleGenerator.generate(5)
        self.cartItems: [CartItem] = []
        for articles in self.expectedArticles:
            self.__cart.add(self.cartItems(articles, 1))
        self.__cart.add([self.cartItems])
        # when
        self.assertRaises(ArticleNotFoundException)
        # then
        # throw exception
