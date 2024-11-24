import unittest
from ..functions import note, midi, midi_to_pitch, pitch_to_midi, Node, get_prob, create_trie, generate

class test_midi(unittest.TestCase):
    def test_case_1(self):
        input_data = "C#"
        expected_result = 1
        self.assertEqual(midi(input_data), expected_result)

    def test_case_2(self):
        input_data = 128
        with self.assertRaises(ValueError) as context:
            midi(input_data)
        self.assertEqual(str(context.exception), "Invalid note")

    def test_case_3(self):
        input_data = 'C17'
        with self.assertRaises(ValueError) as context:
            midi(input_data)
        self.assertEqual(str(context.exception), "Invalid note")

if __name__ == '__main__':
    unittest.main()
