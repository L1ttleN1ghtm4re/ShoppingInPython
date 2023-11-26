import unittest
from shopping.article import *


class TestArticle(unittest.TestCase):

    # region private attributes
    __article = Article
    __id = 0
    __description = ""
    __price = 0.0
    # endregion private attributes

    # region public methods
    def setUp(self):
        self.__id = 1
        self.__description = "product description"
        self.__price = 20.45
        self.__article = Article(self.__id, self.__description, self.__price)

    def test_allProperties_afterInstantiation_success(self):
        # given
        # then
        self.assertEqual(self.__article.id, self.__id)
        self.assertEqual(self.__article.description, self.__description)
        self.assertEqual(self.__article.price, self.__price)

    # region description
    def test_description_shortDescription_returnNewValue(self):
        # given
        self.expected_description = "After Shave"
        # when
        self.__article.description = self.expected_description
        # then
        self.assertEqual(self.__article.description, self.expected_description)

    def test_description_longDescription_returnNewValue(self):
        # given
        self.expected_description = "A very long long long long long long description"
        # when
        self.__article.description = self.expected_description
        # then
        self.assertEqual(self.__article.description, self.expected_description)

    def test_description_singleWordDescription_throwException(self):
        # given

        # when
        with self.assertRaises(TooShortDescriptionException):
            check_description("TooShort")
        # then
        # throw exception

    def test_description_descriptionContainingSpecialChars_throwException(self):
        # given

        # when
        with self.assertRaises(SpecialCharInDescriptionException):
            check_description("Jacques+Daniel")
        # then
        # throw exception

    def test_description_tooLongDescription_throwException(self):
        # given
        # when
        with self.assertRaises(TooLongDescriptionException):
            check_description("A very very very very very looonnng descriptioooooon")
        # then
        # throw exception

    # endregion description

    # region price
    def test_price_updatePrice_getNewValue(self):
        # given
        self.expected_price = 12.20
        # when
        self.__article.price = self.expected_price
        # then
        self.assertEqual(self.__article.price, self.expected_price)

    # TODO: Add PriceUpdateWithNegativeValue => WrongPriceException
    # TODO: Add PriceUpdateSameValue => WrongPriceException
    # endregion price
    # endregion public methods


if __name__ == '__main__':
    unittest.main()
