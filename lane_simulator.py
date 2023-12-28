import random
import heapq
import time

class Customer:
    def __init__(self, items):
        self.items = items

class CheckoutLane:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.customers = []

    def is_full(self):
        return len(self.customers) >= self.max_capacity

    def assign_customer(self, customer):
        self.customers.append(customer)

    def process_checkout(self):
        # Simulate checkout process
        time.sleep(random.uniform(0.5, 2.0))
        return self.customers.pop(0)

    def move_customer(self, target_lane):
        customer = self.customers.pop(0)
        target_lane.assign_customer(customer)

class SupermarketSimulation:
    def __init__(self):
        self.regular_lanes = [CheckoutLane(1) for _ in range(5)]
        self.self_service_lane = CheckoutLane(8)
        self.customers = []
        self.time_limit = 300  # Set a time limit for simulation (in seconds)
        self.start_time = time.time()

    def generate_random_basket_size(self):
        return random.randint(1, 30)

    def generate_customers(self, num_customers):
        return [Customer(self.generate_random_basket_size()) for _ in range(num_customers)]

    def enter_lane(self, customer):
        # Assign customer to the shortest available lane
        lanes = self.regular_lanes + [self.self_service_lane]
        shortest_lane = min(lanes, key=lambda lane: len(lane.customers))
        shortest_lane.assign_customer(customer)

    def leave_lane(self, lane):
        return lane.process_checkout()

    def move_lane(self, source_lane, target_lane):
        source_lane.move_customer(target_lane)

    def open_new_lane(self):
        new_lane = CheckoutLane(1)  # New regular lane
        self.regular_lanes.append(new_lane)

    def close_lane(self, lane):
        if len(lane.customers) == 0:
            self.regular_lanes.remove(lane)

    def simulate(self):
        while time.time() - self.start_time < self.time_limit:
            # Generate new customers
            new_customers = self.generate_customers(random.randint(1, 10))
            for customer in new_customers:
                if len(self.customers) < 40:
                    self.enter_lane(customer)
                    self.customers.append(customer)

            # Process checkout for each lane
            for lane in self.regular_lanes + [self.self_service_lane]:
                if len(lane.customers) > 0:
                    processed_customer = self.leave_lane(lane)
                    self.enter_lane(processed_customer)

            # Check if all open lanes are full, open a new lane if available
            if all(lane.is_full() for lane in self.regular_lanes):
                self.open_new_lane()

            # Close lanes with few customers
            for lane in self.regular_lanes[:]:
                if len(lane.customers) <= 1:
                    self.close_lane(lane)

            # Move customers between lanes if needed
            for lane in self.regular_lanes:
                if len(lane.customers) > 5:
                    target_lane = min(self.regular_lanes, key=lambda l: len(l.customers))
                    self.move_lane(lane, target_lane)

            # Print simulation status (optional)
            print("Time:", int(time.time() - self.start_time), "s")
            for i, lane in enumerate(self.regular_lanes):
                print(f"Lane {i + 1}:", len(lane.customers), "customers")
            print("Self-Service Lane:", len(self.self_service_lane.customers), "customers")
            print("----")

# Run the simulation
simulation = SupermarketSimulation()
simulation.simulate()
