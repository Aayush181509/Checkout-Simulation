import random

class Customers:
    def __init__(self,id,items_in_basket):
        self.id = id
        self.items_in_basket = items_in_basket

    def award_luckydraw(self):
        if self.items_in_basket>=10:
            return random.choice(['yes','no'])
        else:
            return None

    def get_checkout_time(self,checkout_type):
        return self.get_no_items()*(4 if checkout_type=='reg' else 6)
    

    # def __str__(self):
    #     return f"Customer: {self.id} Items in Basket: {self.get_no_items()}"
        
    def get_no_items(self):
        return self.items_in_basket
    
    def get_customer_info(self):
        if self.award_luckydraw()=='yes':
            return f""" ### Lucky Customer ###
C{self.id} -> items in basket: {self.get_no_items()}, wins a lottery ticket!
    time to process basket at cashier till: {self.get_checkout_time('reg')} Secs
    time to process basket at self-service till: {self.get_checkout_time('self')} Secs"""
        else:
            return f"""C{self.id} -> items in basket: {self.get_no_items()}, hard luck, no lottery ticket this time! 
    time to process basket at cashier till: {self.get_checkout_time('reg')} Secs
    time to process basket at self-service till: {self.get_checkout_time('self')} Secs"""

