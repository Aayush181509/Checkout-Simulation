from modules.Customer import Customer
from modules.RegularLane import RegularLane
from modules.SelfServiceLane import SelfServiceLane

class AddCustomer:
    def __init__(self) -> None:
        pass

    def add_customer(self):
        try:
            while not self.customer.empty():
                customer = self.get_customers()
                lane = self.get_lane()
                lane.add_customer(customer)
        except Exception as e:
            print(e)