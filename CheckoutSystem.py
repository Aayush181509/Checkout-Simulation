import random
from modules.RegularLane import RegularLane
from modules.SelfServiceLane import SelfServiceLane
import threading
from modules.Customer import Customer
from datetime import datetime
import pickle

class CheckoutSystem:
    def __init__(self) -> None:
        self.regular_lanes = [RegularLane(i) for i in range(1,6)]
        self.selfservice_lane = SelfServiceLane()
        self.lanes = self.regular_lanes+[self.selfservice_lane]
        # self.open_lane = [self.regular_lanes[0],self.selfservice_lane]
        # self.count = 0


    def create_customers(self,num):
        customers = []
        for _ in range(num):
            items_in_basket = random.randint(1,30)
            c = Customer(_,random.randint(1,30))
            customers.append(c)

        with open('files/customers.pkl','ab') as file:
            for customer in customers:
                pickle.dump(customer,file)


    def read_customers_from_files(self):
        objects = []
        try:
            with open('files/customers.pkl','rb') as file:
                while True:
                    obj = pickle.load(file)
                    objects.append(obj)
        except EOFError:
            pass

        return objects
    
    def open_lane(self,lane):
        lane.open_lane()

    
    
    def open_new_lane(self):
        if len(self.open_lane)<6:
            for i in self.regular_lanes:
                if i not in self.open_lane:
                    self.open_lane.append(i)
                    i.open_lane()
                    return i

        else:
            print("Sorry!! Max limit reached")
            return False
                

    def add_customer_to_lane(self,customer):
        selected_lane = min(self.open_lane,key=lambda lane: lane.get_total_time())
        if selected_lane.queue.full():
            for i in self.open_lane:
                if i!=selected_lane and not i.queue.full():
                    selected_lane = i
                else:
                    if not self.open_new_lane():
                        print("Sorry")
                    else:
                        selected_lane = self.open_new_lane()
        print(selected_lane.id)
        selected_lane.open_lane()
        selected_lane.add_customer(customer)
        self.count+=1
        self.display_lane_info()

    def display_lane_info(self):
        print(f"""
### Lane Status at the start of simulation ###
Total Number of customers waiting to checkout at {datetime.now()} is {self.count}
""")
        for i in self.regular_lanes:
            print(i.display_lane())
        print(self.selfservice_lane.display_lane())


s = CheckoutSystem()
s.create_customers(10)
obj = s.read_customers_from_files()
for o in obj:
    print(o)
# for i in range(20):
#     c = Customer(i,random.randint(1,28))
#     s.add_customer_to_lane(c)
# lane = RegularLane(3,True)              
# for i in range(15):
#     customer = Customer(i,random.randint(1,30))
#     # t = threading.Thread(target=lane.add_customer,args=(customer,))
#     # t.start()
#     lane.add_customer(customer)

# # t.join()
# # print(lane.display_lane())
# # lane.process_customer()
# lane.start_processing()

# # print(lane.display_lane())
# time.sleep(5)



# lane.stop_processing()

