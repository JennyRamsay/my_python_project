class Appointment:
    def __init__(self, customer, treatment, id=None):
        self.customer = customer
        self.treatment = treatment
        self.id = id