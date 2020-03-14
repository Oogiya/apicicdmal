import sys
sys.path.append(".")

from deploy import get_top_anime
from unittest.mock import Mock, patch, MagicMock
import unittest


class get_top_anime_test(unittest.TestCase):

    @patch('deploy.get_top_anime')
    def anime_in_top(self, get_mock):
        pass

    @patch('deploy.get_top_anime')
    def anime_not_in_top(self, get_mock):
        pass

    @patch('deploy.get_top_anime')
    def first_rating_higer_than_last(self, get_mock):
        pass

    @patch('deploy.get_top_anime')
    def last_rating_lower_than_first(self, get_mock):
        pass

    @patch('deploy.get_top_anime')
    def negative_top(self, get_mock):
        pass


if __name__ == '__main__':
    unittest.main()

