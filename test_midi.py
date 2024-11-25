import unittest
from functions import midi

class test_midi(unittest.TestCase):
    def test_case_1(self):
        input_data = "C#1"
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

    def test_case_4(self):
        input_data = 'C*10'
        with self.assertRaises(ValueError) as context:
            midi(input_data)
        self.assertEqual(str(context.exception), "Invalid note")

    def test_case_5(self):
        input_data = 'S5'
        with self.assertRaises(ValueError) as context:
            midi(input_data)
        self.assertEqual(str(context.exception), "Invalid note")

    def test_case_6(self):
        input_data = 'C'
        with self.assertRaises(ValueError) as context:
            midi(input_data)
        self.assertEqual(str(context.exception), "Invalid note")
    
    

if __name__ == '__main__':
    unittest.main()
