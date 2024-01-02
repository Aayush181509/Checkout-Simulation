from datetime import datetime
import queue
from modules.Customer import Customer
import time
from prettytable import PrettyTable
from modules.SaveTable import SaveTable
import csv

lanes = [f'L{i}' for i in range(1,7)]


class Lane:
    def __init__(self,l_id,is_self_service,is_open,max_capacity,max_tills) -> None:
        self.id = lanes[l_id-1]
        self.is_self_service = is_self_service
        self.is_open = is_open
        
        self.max_capacity = max_capacity
        self.max_tills = max_tills
        self.queue = queue.Queue(maxsize=max_capacity)


    def open_lane(self):
        try:
            self.is_open = True
            print(self.id," Opened")
        except Exception as e:
            print(e)

    def close_lane(self):
        if self.is_open:
            if self.queue.empty():
                self.is_open = False
                return True
            else:
                return False
        else:
            return "closed"
            

    def add_customer(self,customer):
        if self.is_open:
            if not self.queue.full():
                if not self.is_self_service:
                    self.queue.put((customer.c_id,customer.items_in_basket,
                                    customer.get_burst_time('reg'),datetime.now()),block=False)
                else:
                    self.queue.put((customer.c_id,customer.items_in_basket,
                                    customer.get_burst_time('self'),datetime.now()),block=False)
                return True
                    
            else:
                return "full"
        else:
            return "closed"
                    
    def remove_customer(self):
        if self.is_open:
            if not self.queue.empty():
                return self.queue.get()
            else: 
                return None
            
        else:
            return None
            
    def empty_lane(self):
        try:
            while not self.queue.empty():
                self.queue.get()
            return True
        except:
            return False

    def move_customer(self):
        if self.is_open:
            if not self.queue.empty():
                return self.queue.queue.pop()
            else:
                return None
        else:
            return None

    def get_total_time(self):
        if self.is_open:
            if not self.queue.empty():
                return sum([i[2] for i in list(self.queue.queue)])
            else:
                return 0
        else: 
            return 0

    def process_customer(self):
        pass

    def get_current_length(self):
        return self.queue.qsize()
    
    def display_lane(self):
        pass

    def display_details(self):
        try:
            customers = list(self.queue.queue)
            # SaveTable().append_to_table('tableinfo.csv',self.id,datetime.now(),customers)
            table = PrettyTable()
            with open('processed_customers.csv','r') as file:
                reader = csv.reader(file)

                header = next(reader)
                table.field_names = header
                for row in reader:
                    table.add_row(row)

            return table
        
        except:
            return None
        

    
        
                

# c1 = Customer(2,8)
# l = Lane(3,False,True,5,1)
# c2 = Customer(4,8)
# l.add_customer(c1)
# l.add_customer(c2)
# # print(l.get_total_time())
# # print(l.move_customer())
# # print(l.get_total_time())
# l.display_details()
    
# print(table)
    
        