import unittest
from models.treatment import Treatment

class TestTreatment(unittest.TestCase):

    def setUp(self):
        self.treatment = Treatment("HIIT (High Intensity Training)", "Monday", "13:00", 10)

    def test_treatment_has_name(self):
        self.assertEqual("HIIT (High Intensity Training)", self.treatment.name)

    def test_treatment_has_day_of_week(self):
        self.assertEqual("Monday", self.treatment.day_of_week)

    def test_treatment_has_time(self):
        self.assertEqual("13:00", self.treatment.time)
    
    def test_treatment_has_capacity(self):
        self.assertEqual(10, self.treatment.capacity)