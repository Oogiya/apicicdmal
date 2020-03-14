from deploy import get_anime_by_name, get_api_link
import unittest
from unittest.mock import Mock, patch


class get_anime_by_name_test(unittest.TestCase):
    @patch('deploy.get_anime_by_name')
    def test_lowercase(self, mock_get):
        result = "Name: Made in Abyss\nEpisodes: 13"

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = get_api_link() + "search/anime?q=made%20in%20abyss&page=1"

        stub = "made in abyss"
        expected = "Name: Made in Abyss\nEpisodes: 13"
        true_result = get_anime_by_name(stub)

        self.assertIn(expected, true_result)

    @patch('deploy.get_anime_by_name')
    def test_uppercase(self, mock_get):
        result = "Name: Made in Abyss\nEpisodes: 13"

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = get_api_link() + "search/anime?q=made%20in%20abyss&page=1"

        stub = "MADE IN ABYSS"
        expected = "Name: Made in Abyss\nEpisodes: 13"
        true_result = get_anime_by_name(stub)

        self.assertIn(expected, true_result)

    @patch('deploy.get_anime_by_name')
    def test_ongoing_anime(self, mock_get):
        result = "Episodes: 0"

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = get_api_link() + "search/anime?q=one%20piece&page=1"

        stub = "One Piece"
        expected = "Episodes: 0"
        true_result = get_anime_by_name(stub)

        self.assertIn(expected, true_result)

    @patch('deploy.get_anime_by_name')
    def test_finished_anime(self, mock_get):
        result = "Is Airing: No"

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = get_api_link() + "search/anime?q=Parasyte&page=1"

        stub = "Parasyte"
        expected = "Is Airing: No"
        true_result = get_anime_by_name(stub)

        self.assertIn(expected, true_result)

    @patch('deploy.get_anime_by_name')
    def test_fixed_episodes(self, mock_get):
        result = "Episodes: 11"

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = get_api_link() + "search/anime?q=Parasyte&page=1"

        stub = "Ano Hi Mita Hana no Namae wo Bokutachi wa Mada Shiranai"
        expected = "Episodes: 11"
        true_result = get_anime_by_name(stub)

        self.assertIn(expected, true_result)


if __name__ == '__main__':
    unittest.main()