from Lane import Lane
import time
from datetime import datetime
from SaveTable import SaveTable
from Customer import Customer
import threading
import random

class RegularLane(Lane):
    def __init__(self, l_id, is_open) -> None:
        super().__init__(l_id, False, is_open, 5, 3)
        self.tills = [threading.Thread(target=self.process_customer,args = (i,)) for i in range(self.max_tills)]
    
    def process_customer(self,till_id):
        if self.is_open:
            while not self.queue.empty():
                with open('processed_customers.txt','w') as file:
                    customer = self.queue.get()
                    time.sleep(customer[2]/50)
                    print(f'Processing for Customer:{customer[0]} in Till{till_id} Number of Items: {customer[1]} Time Required: {customer[2]}')
                    # print(f'Processing for Customer:{customer[0]}Number of Items: {customer[1]} Time Required: {customer[2]}')
                    SaveTable().append_to_table('processed_customers.csv',self.id,datetime.now(),[customer])
                    # print(self.display_lane())
                        #file.write(f'''
                        # ### Regular Lane ####                               
                        # In Lane: {self.id}
                        # Customer ID: C{customer[0]}
                        # Number of Items in Basket: {customer[1]}
                        # Estimated Time: {customer[2]}
                        # Taken Time: {datetime.now() - customer[3]} secs
                        # ''')

    def start_processing(self):
        for thread in self.tills:
            thread.start()
            
    
    def display_lane(self):
        if self.is_open:
            return f"{self.id} (Reg)-> {'* ' *self.get_current_length()} Estimated Time: {self.get_total_time()}"
        else:
            return f"{self.id}(Ref)-> closed"

        
    def stop_processing(self):
        self.is_open = False
        for thread in self.tills:
            
            thread.join()




# lane = SelfServiceLane()
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




# c1 = Customer(3,8)
# l = SelfServiceLane()
# # l = RegularLane(2,9)
# l.add_customer(c1)
# c2 = Customer(8,9)
# l.add_customer(c2)
# l.process_customer()
# print(l.display_lane())
# # print(l.display_details())