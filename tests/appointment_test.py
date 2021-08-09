import unittest
from models.customer import Customer
from models.treatment import Treatment
from models.appointment import Appointment

class TestAppointment(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jennifer", "Premium")
        self.treatment = Treatment("HIIT (High Intensity Training)", "Monday", "13:00", 10)
        self.appointment = Appointment(self.customer, self.treatment)

    def test_appointment_has_customer(self):
        self.assertEqual("Jennifer", self.appointment.customer.full_name)

    def test_appointment_has_treatment(self):
        self.assertEqual("HIIT (High Intensity Training)", self.appointment.treatment.name)

    def test_appointment_has_day_of_week(self):
        self.assertEqual("Monday", self.appointment.treatment.day_of_week)

    def test_appointment_has_time(self):
        self.assertEqual("13:00", self.appointment.treatment.time)

    def test_appointment_has_capacity(self):
        self.assertEqual(10, self.appointment.treatment.capacity)
