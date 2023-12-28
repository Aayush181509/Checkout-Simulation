import queue
import time
import random

lanes=[f'L{i}' for i in range(1,7)]
type=['Reg','Slf']
is_open = ['opened','closed']

class CheckoutLane:
    def __init__(self,id,max_capacity,is_open=False,is_self_service=True) -> None:
        self.id = lanes[id-1]
        self.max_capacity=max_capacity
        self.queue = queue.Queue(maxsize=max_capacity)
        self.is_open=is_open
        self.type=type[1 if is_self_service else 0]

    def is_full(self):
        return self.queue.full()

    def change_is_open(self):
        self.is_open = not self.is_open

    def assign_customer(self,customer):
        if self.type=='Reg':
            self.burst_time = customer.get_no_items()*(4//3)
        else:
            self.burst_time = customer.get_no_items()*(6//3)
        self.queue.put(customer)

    
    def get_burst_time(self):
        print(self.burst_time)
        return self.burst_time

    def is_empty(self):
        return self.queue.empty()
    
    def remove_customer(self):
        return self.queue.get()
        
    
    def process_checkout(self):
        if not self.is_empty():
            time.sleep(random.uniform(0.5, 2.0))
            processed_customer = self.remove_customer()
            return processed_customer
        else:
            return None
    
    # def move_customer(self, target_lane):
    #     if not self.is_empty():
    #         customer = self.queue.get()
    #         target_lane.assign_customer(customer)
    
    def remove_new(self):
        if not self.is_empty():
            temp_queue = queue.Queue()

            while self.queue.qsize() > 1:
                temp_queue.put(self.remove_customer())
            val = self.remove_customer()
            while not temp_queue.empty():
                self.queue.put(temp_queue.get())
            return val
        else:
            return None

    def current_capacity(self):
        return self.queue.qsize()
    

    def display_queue(self):
        if self.is_open:
            print(f"{self.id} ({self.type})",'-> ','* '*self.current_capacity())
        else:
            print(f"{self.id} ({self.type})",'->','closed')
        # print("----")
            
    def display_queue_details(self):
        for customer in list(self.queue.queue):
            print(customer,'\n')


