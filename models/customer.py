class Customer:
    def __init__(self, full_name, customership, status="Active", id=None):
        self.full_name = full_name
        self.customership = customership
        self.status = status
        self.id = id