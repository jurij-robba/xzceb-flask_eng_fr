import translator
import unittest

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french(None), None)
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
        self.assertEqual(translator.english_to_french('Never gonna give you up'),
        'Ne vous abandonnez jamais')
        self.assertEqual(translator.english_to_french('Never gonna let you down'),
        'Ne vous laisserez jamais tomber')

    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english(None), None)
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
        self.assertEqual(translator.french_to_english(
        'Ne va jamais t\'engueule et te déserter'),
        'Never go out and desert you.')
        self.assertEqual(translator.french_to_english('Ne te fera jamais pleurer'),
        'Will never make you cry')

if __name__ == '__main__':
    unittest.main()