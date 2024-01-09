from modules.Lane import Lane
import time
from datetime import datetime
from modules.SaveTable import SaveTable
from modules.Customer import Customer
import threading
import random


class RegularLane(Lane):
    def __init__(self, l_id) -> None:
        super().__init__(l_id, False, False, 5, 1)
        
    
    def process_customer(self):
        # print(customer_queue)
        # while not customer_queue.empty():
        if self.is_open:
            if not self.queue.empty():
                customer = self.queue.get()
                print(f'{self.id}: Processing for Customer:{customer[0]} Number of Items: {customer[1]} Time Required: {customer[2]}')
                time.sleep(customer[2]/50)
            else:
                # if customer_queue.empty():
                self.close_lane()
                # else:
                #     self.add_customer(customer_queue.get())
        else:
            if not self.queue.empty():
                self.open_lane()

    # def start_processing(self):
    #     for thread in self.tills:
    #         thread.start()
            
    
    def display_lane(self):
        if self.is_open:
            return f"{self.id} (Reg)-> {'* ' *self.get_current_length()} Estimated Time: {self.get_total_time()}"
        else:
            return f"{self.id} (Reg)-> closed"

        
    # def stop_processing(self):
    #     self.is_open = False
    #     for thread in self.tills:
            
    #         thread.join()




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