from datetime import datetime
import queue
from Customer import Customer
import time

lanes = [f'L{i}' for i in range(1,7)]


class Lane:
    def __init__(self,l_id,is_self_service,is_open,max_capacity,tills) -> None:
        self.id = lanes[l_id-1]
        self.is_self_service = is_self_service
        self.is_open = is_open
        self.timestamp = datetime.now()
        self.max_capacity = max_capacity
        self.tills = tills
        self.queue = queue.Queue(maxsize=max_capacity)


    def open_lane(self):
        self.is_open = True

    def close_lane(self):
        if self.queue.empty():
            self.is_open = False

    def add_customer(self,customer):
        if self.is_open:
            if not self.queue.full():
                if not self.is_self_service:
                    self.queue.put((customer.c_id,customer.items_in_basket,
                                    customer.get_burst_time('reg')))
                else:
                    self.queue.put((customer.c_id,customer.items_in_basket,
                                    customer.get_burst_time('self')))
                    
    def remove_customer(self):
        if self.is_open:
            if not self.queue.empty():
                return self.queue.get()
            
    def empty_lane(self):
        while not self.queue.empty():
            self.queue.get()

    def move_customer(self):
        if self.is_open:
            if not self.queue.empty():
                return self.queue.queue.pop()

    def get_total_time(self):
        if self.is_open:
            if not self.queue.empty():
                return sum([i[2] for i in list(self.queue.queue)])

    def process_customer(self):
        pass

    def get_current_length(self):
        return self.queue.qsize()
    
    def display_lane(self):
        pass

    
        
                

c1 = Customer(2,8)
l = Lane(3,False,True,5,1)
c2 = Customer(4,8)
l.add_customer(c1)
l.add_customer(c2)
print(l.get_total_time())
print(l.move_customer())
print(l.get_total_time())
    
    
        