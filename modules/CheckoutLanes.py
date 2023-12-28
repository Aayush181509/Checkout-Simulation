from CheckoutLane import CheckoutLane
from Customers import Customers
import time
import random

class RegularCheckoutLane(CheckoutLane):
    def __init__(self, id, max_capacity=5, status=False, is_self_service=False) -> None:
        super().__init__(id, max_capacity, status, is_self_service)

    def burst_time(self,customer):
        return customer.no_items()*(4//3)

class SelfCheckoutLane(CheckoutLane):
    def __init__(self, id=6, max_capacity=15, status=True, is_self_service=True) -> None:
        super().__init__(id, max_capacity, status, is_self_service)

    def burst_time(self,customer):
        return customer.get_no_items()*(6//3)
    
    def process_checkout(self):
        if not self.is_empty():
            processed_customer = self.remove_customer()
            print(self.burst_time(processed_customer))
            # time.sleep(self.burst_time(processed_customer))   
            return processed_customer
        else:
            return None


c = Customers(8,18)
r = SelfCheckoutLane()
# r.assign_customer(c)
print(type(r.burst_time(c)))
