from CheckoutLane import CheckoutLane
from Customers import Customers
import time
import random

class RegularCheckoutLane(CheckoutLane):
    def __init__(self, id, max_capacity=5, status=False, is_self_service=False) -> None:
        super().__init__(id, max_capacity, status, is_self_service)


class SelfCheckoutLane(CheckoutLane):
    def __init__(self, id=6, max_capacity=15, status=True, is_self_service=True) -> None:
        super().__init__(id, max_capacity, status, is_self_service)


c = Customers(8,18)

r = RegularCheckoutLane(2)
r.assign_customer(c)
cu = r.process_checkout()

print(cu.get_customer_info())