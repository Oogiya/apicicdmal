import sys
sys.path.append(".")

from deploy import get_top_anime, get_api_link, Anime
from unittest.mock import Mock, patch, MagicMock
import unittest


class get_top_anime_test(unittest.TestCase):
    @patch('deploy.get_top_anime')
    def test_anime_in_top(self, get_mock):
        get_mock.return_value = Mock(ok=True)
        get_mock.return_value.json.return_value = get_api_link() + "top/anime/1/?page=1"

        expected = "Fullmetal"

        self.assertIn(expected, get_top_anime(1)[0].name)

    @patch('deploy.get_top_anime')
    def test_anime_not_in_top(self, get_mock):
        get_mock.return_value = MagicMock(ok=True)
        get_mock.return_value.json.return_value = get_api_link() + "top/anime/1/?page=1"

        expected = "one piece"

        self.assertNotIn(expected, get_top_anime(1)[0].name)

    @patch('deploy.get_top_anime')
    def test_first_rating_higer_than_last(self, get_mock):
        get_mock.return_value = Mock(ok=True)
        get_mock.return_value.json.return_value = get_api_link() + "top/anime/1/?page=1"

        stub_list = get_top_anime(1)

        self.assertGreater(stub_list[0].rating, stub_list[len(stub_list)-1].rating)

    @patch('deploy.get_top_anime')
    def test_last_rating_lower_than_first(self, get_mock):
        get_mock.return_value = MagicMock(ok=True)
        get_mock.return_value.json.return_value = get_api_link() + "top/anime/1/?page=1"

        stub_list = get_top_anime(1)

        self.assertLess(stub_list[49].rating, stub_list[0].rating)

    @patch('deploy.get_top_anime')
    def test_negative_top(self, get_mock):
        get_mock.return_value = Mock(ok=False)
        get_mock.return_value.json.return_value = get_api_link() + "top/anime/1/?page=-1"

        self.assertEqual("error", get_top_anime(-1))


if __name__ == '__main__':
    unittest.main()

