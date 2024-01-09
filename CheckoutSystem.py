import random
from modules.RegularLane import RegularLane
from modules.SelfServiceLane import SelfServiceLane
import threading
from modules.Customer import Customer
from datetime import datetime
import queue
import time

class CheckoutSystem:
    def __init__(self) -> None:
        self.regular_lanes = [RegularLane(i) for i in range(1,6)]
        self.selfservice_lane = SelfServiceLane()
        self.lanes = self.regular_lanes+[self.selfservice_lane]
        self.regular_lanes[0].open_lane()
        # self.regular_lanes[1].open_lane()
        # self.regular_lanes[2].open_lane()
        # self.regular_lanes[3].open_lane()
        # self.regular_lanes[4].open_lane()
        # self.open_lane(self.selfservice_lane)
        # self.regular_lanes[4].close_lane()
        self.open_lanes = [self.regular_lanes[0]]
        # self.open_lanes = [self.regular_lanes[0],self.regular_lanes[1],self.regular_lanes[2],self.regular_lanes[3],self.regular_lanes[4]]
        # self.open_lanes.remove(self.regular_lanes[4])
        self.count = 0
        self.customer = queue.Queue(100)

    def is_max_capacity(self):
        for i in self.open_lanes:
            if not i.queue.full():
                return False
        return True
            
    def generate_customers(self,num):
        for _ in range(num):
            items_in_basket = random.randint(1,30)
            c = Customer(random.randint(1,100),items_in_basket)
            self.customer.put(c)

    def get_customers(self):
        if self.customer.empty():
            print("No Customers remaining")
            return
        else:
            return self.customer.get()
    
    def get_lane(self):
        if not self.is_max_capacity():
            lanes = []
        
            for i in self.open_lanes:
                if not i.queue.full():
                    lanes.append(i)
                else:
                    # print(i.id,"Lane Capacity Full")
                    pass
            lane = min(lanes, key=lambda lane: lane.get_total_time())
            return lane
        else:
            lane = self.open_new_lane()
            if lane is not None:
                lane.open_lane()
                return lane
            else:
                return

    

    def open_new_lane(self):
        # for i in self.open_lanes:
        if self.is_max_capacity():
            for lane in self.regular_lanes:
                if lane not in self.open_lanes:
                    lane.open_lane()
                    self.open_lanes.append(lane)
                    return lane
                else:
                    pass
            # print("Sorry all lanes opened")
            return 
        else:
            # print(i.id,"Lane has not reached max capacity")
            return 
            
    def add_customer(self):
        try:
            while not self.customer.empty():
                customer = self.get_customers()
                lane = self.get_lane()
                # self.count+=1
                lane.add_customer(customer)
                
                # time.sleep(2)
        except Exception as e:
            print(e)

    def selflane_process_customer(self):
        lane = self.selfservice_lane
        lane.start_processing()
        print(lane.id,lane.is_open)
        # lane.stop_processing()

    def regularlane_process_customer(self,lane):
        while True:
            if lane.is_open:
                if not lane.queue.empty():
                    lane.process_customer()
                else:
                    time.sleep(5)
            else:
                time.sleep(5)


    def customer_simulation(self):
        while True:
            count=0
            self.generate_customers(25)
            while not self.customer.empty():
                lane=self.get_lane()
                if lane is not None:
                    self.count+=1
                    lane.add_customer(self.customer.get())
                else:
                    time.sleep(3)
                    break
            self.display_lane_info()
            time.sleep(5)

            # lane.process_customer()
            # self.count-=1
            
        # if not lane.queue.full():
        #     print(lane.id,"Not Full")
        #     lane.process_customer(self.customer)
        #     if self.get_customers() is not None:
        #         print(self.get_customers())
        #         lane.add_customer(self.get_customers())
        # print(lane.id,lane.is_open)

    def simulate(self):
        threads = [threading.Thread(target=self.regularlane_process_customer,args=(lane,)) for lane in self.regular_lanes if lane!=self.selfservice_lane]
        threading.Thread(target=self.customer_simulation).start()
        # threads.append(threading.Thread(target=self.selflane_process_customer))
        # print(threads)
        for thread in threads:
            thread.start()

        # for thread in threads:
        #     thread.join()

    def simulation(self):
        self.display_lane_info()
        # self.generate_customers(50)
        # threading.Thread(target=self.add_customer()).start()
        # self.add_customer()
        # self.process_customer()
        self.simulate()
        # time.sleep(10)
        # self.display_lane_info()
        


    def display_lane_info(self):
        print(f"""
### Lane Status at the start of simulation ###
Total Number of customers waiting to checkout at {datetime.now()} is {self.count}
""")
        for i in self.regular_lanes:
            print(i.display_lane())
        print(self.selfservice_lane.display_lane())


   
    
s = CheckoutSystem()
s.simulation()
# s.generate_customers(45)
# s.display_lane_info()
# print(s.is_max_capacity())
# s.add_customer()
# s.display_lane_info()
# # s.process_customer()
# s.simulate()
# s.display_lane_info()




