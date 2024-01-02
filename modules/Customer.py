import random


class Customer:

    def __init__(self,c_id,items_in_basket) -> None:
        self.c_id = c_id
        self.items_in_basket = items_in_basket
        

    def lucky_draw(self):
        
        if self.get_number_of_items() >= 10:
            return random.randint(0,1)
        
        else:
            return None
    
    def get_number_of_items(self):
        return self.items_in_basket
    
    def get_burst_time(self,lane_type):
        self.lane_type = lane_type
        return self.get_number_of_items()*(4 if lane_type=="reg" else 6)
    
    def get_lane_info(self):
        if self.lane_type=='reg':
            return "Regular Lane"
        else:
            return "Self Service Lane"

    def __str__(self) -> str:
        if self.lucky_draw()==1:
            return f""" ### Lucky Customer ###
C{self.c_id} -> items in basket: {self.get_number_of_items()}, wins a lottery ticket!
    time to process basket at cashier till: {self.get_burst_time('reg')} Secs
    time to process basket at self-service till: {self.get_burst_time('self')} Secs"""
        else:
            return f"""C{self.c_id} -> items in basket: {self.get_number_of_items()}, hard luck, no lottery ticket this time! 
    time to process basket at cashier till: {self.get_burst_time('reg')} Secs
    time to process basket at self-service till: {self.get_burst_time('self')} Secs"""


