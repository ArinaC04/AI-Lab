import unittest
from functions import midi_to_pitch, pitch_to_midi

class test_midi_pitch(unittest.TestCase):
    def test_case_1(self):
        with self.assertRaises(ValueError) as context:
            pitches, duration = midi_to_pitch("main.py")
        self.assertEqual(str(context.exception), "Not a MIDI file")
    def test_case_2(self):
        pitches, duration = midi_to_pitch('jackson_m.mid')
        pitch_to_midi(pitches, duration, 48)
        pitches_2, duration_2 = midi_to_pitch('output.mid')
        self.assertEqual(pitches, pitches_2)

    def test_case_3(self):
        pitches, duration = midi_to_pitch('jackson_m.mid')
        pitch_to_midi(pitches, duration, 48)
        pitches_2, duration_2 = midi_to_pitch('output.mid')
        self.assertEqual(duration, duration_2)


        

    