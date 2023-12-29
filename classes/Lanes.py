from Lane import Lane
import time
from datetime import datetime
from SaveTable import SaveTable
from Customer import Customer
import threading
import random

class RegularLane(Lane):
    def __init__(self, l_id, is_open) -> None:
        super().__init__(l_id, False, is_open, 5, 1)

    
    def process_customer(self):
        if self.is_open:
            with open('processed_customers.txt','w') as file:
                while not self.queue.empty():
                    customer = self.queue.get()
                    time.sleep(customer[2]/50)
                    print(customer)
                    SaveTable().append_to_table('processed_customers.csv',self.id,datetime.now(),[customer])
#                     file.write(f'''
# ### Regular Lane ####                               
# In Lane: {self.id}
# Customer ID: C{customer[0]}
# Number of Items in Basket: {customer[1]}
# Estimated Time: {customer[2]}
# Taken Time: {datetime.now() - customer[3]} secs
# ''')

                    
    def display_lane(self):
        if self.is_open:
            return f"{self.id} (Reg)-> {'* ' *self.get_current_length()} Estimated Time: {self.get_total_time()}"
        else:
            return f"{self.id}(Ref)-> closed"

        



class SelfServiceLane(Lane):
    def __init__(self) -> None:
        super().__init__(6, True, True, 15, 8)
        self.tills = [threading.Thread(target=self.process_customer,args = (i,)) for i in range(self.max_tills)]

    def process_customer(self,till_id):
        if self.is_open:
            with open('processed_customers.txt','w') as file:
                while not self.queue.empty():
                    customer = self.queue.get()
                    print(f'Processing for Customer:{customer[0]} in Till{till_id} Number of Items: {customer[1]} Time Required: {customer[2]}')
                    time.sleep(customer[2]/20)
                    # print(customer)
                    SaveTable().append_to_table('processed_customers.csv',self.id,datetime.now(),[customer])
#                     file.write(f'''
# ### Self Service Lane ####                                
# In Lane: {self.id}
# Customer ID: C{customer[0]}
# Number of Items in Basket: {customer[1]}
# Estimated Time: {customer[2]}
# Taken Time: {int(datetime.now() - customer[3])} secs
# ''')

    def start_processing(self):
        for thread in self.tills:
            thread.start()


    def display_lane(self):
        if self.is_open:
            return f"{self.id} (Slf)-> {'* '*self.get_current_length()} Estimated Time: {self.get_total_time()}"
        else:
            return f"{self.id}(Slf)-> closed"
        
    def stop_processing(self):
        self.is_open = False
        for thread in self.tills:
            thread.join()


# lane = SelfServiceLane()
# for i in range(15):
#     customer = Customer(i,random.randint(1,30))
#     lane.add_customer(customer)

# lane.start_processing()

# time.sleep(10)

# lane.stop_processing()




# c1 = Customer(3,8)
# l = SelfServiceLane()
# # l = RegularLane(2,9)
# l.add_customer(c1)
# c2 = Customer(8,9)
# l.add_customer(c2)
# l.process_customer()
# print(l.display_lane())
# # print(l.display_details())