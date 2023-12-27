import queue
import random

class Customer:
    def __init__(self, id):
        self.id = id

class CheckoutLane:
    def __init__(self, id, num_tills):
        self.id = id
        self.queue = queue.Queue()
        self.num_tills = num_tills

    def enqueue_customer(self, customer):
        self.queue.put(customer)

    def dequeue_customer(self):
        if not self.queue.empty():
            return self.queue.get()
        else:
            return None

    def process_checkout(self):
        for _ in range(min(self.num_tills, self.queue.qsize())):
            customer = self.dequeue_customer()
            print(f"Checkout Lane {self.id}: Processing customer {customer.id}")

class SelfServiceCheckoutLane(CheckoutLane):
    def __init__(self, id, num_tills):
        super().__init__(id, num_tills)

class RegularCheckoutLane(CheckoutLane):
    def __init__(self, id):
        super().__init__(id, 1)

class Supermarket:
    def __init__(self, num_self_service_lanes, num_regular_lanes):
        self.self_service_lanes = [SelfServiceCheckoutLane(i, 8) for i in range(1, num_self_service_lanes + 1)]
        self.regular_lanes = [RegularCheckoutLane(i) for i in range(1, num_regular_lanes + 1)]

    def add_customer_to_shortest_lane(self, customer):
        if random.choice([True, False]):  # Randomly choose between self-service and regular lanes
            shortest_lane = min(self.self_service_lanes, key=lambda lane: lane.queue.qsize())
        else:
            shortest_lane = min(self.regular_lanes, key=lambda lane: lane.queue.qsize())

        shortest_lane.enqueue_customer(customer)
        print(f"Customer {customer.id} added to Checkout Lane {shortest_lane.id}")

    def simulate_checkout_process(self, num_customers):
        for i in range(1, num_customers + 1):
            customer = Customer(i)
            self.add_customer_to_shortest_lane(customer)

        print("\nSimulating Checkout Process:\n")
        for lane in self.self_service_lanes + self.regular_lanes:
            lane.process_checkout()

# Example usage
if __name__ == "__main__":
    num_self_service_lanes = 1
    num_regular_lanes = 5
    num_customers = 20

    supermarket = Supermarket(num_self_service_lanes, num_regular_lanes)
    supermarket.simulate_checkout_process(num_customers)
