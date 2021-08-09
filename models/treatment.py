class Treatment:
    def __init__(self, name, day_of_week, time, capacity, id=None, customers_booked=0):
        self.name = name
        self.day_of_week = day_of_week
        self.time = time
        self.capacity = capacity
        self.id = id
        self.customers_booked = customers_booked
        
    
    def get_capacity_left(self, capacity, customers_booked):
        space_left = capacity - customers_booked
        return space_left