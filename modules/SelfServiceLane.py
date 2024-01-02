from modules.Lane import Lane
import threading
import time
from modules.SaveTable import SaveTable
from datetime import datetime
from modules.Customer import Customer
import random


class SelfServiceLane(Lane):
    def __init__(self) -> None:
        super().__init__(6, True, True, 15, 8)
        self.tills = [threading.Thread(target=self.process_customer,args = (i,)) for i in range(self.max_tills)]

    def process_customer(self,till_id):
        if self.is_open:
            with open('processed_customers.txt','w') as file:
                while not self.queue.empty():
                    customer = self.queue.get()
                    
                    SaveTable().append_to_table('processed_customers.csv',self.id,datetime.now(),[customer])
                    print(f'Processing for Customer:{customer[0]} in Till{till_id} Number of Items: {customer[1]} Time Required: {customer[2]}')
                    time.sleep(customer[2]/20)
                    # print(customer)
                    # print(self.id,customer)
                    # print(self.display_lane())
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
# # lane = RegularLane(3,True)            
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