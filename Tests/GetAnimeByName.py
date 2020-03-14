from deploy import GetAnimeByName, get_api_link
import unittest
from unittest.mock import Mock, patch

# TODO
#   Unit testing from 'GetAnimeByName'
#   - lower letters
#   - upper
#   - combination
#   - numbers
#   - null

class GetAnimeByNameTest(unittest.TestCase):
    @patch('deploy.GetAnimeByName')
    def test_lowercase(self, mock_get):
        result = "Name: Made in Abyss\nEpisodes: 13"

        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = get_api_link() + "search/anime?q=made%20in%20abyss&page=1"

        stub = "made in abyss"
        expected = "Name: Made in Abyss\nEpisodes: 13"
        true_result = GetAnimeByName(stub)

        self.assertEqual(true_result, expected)

if __name__ == '__main__':
    unittest.main()