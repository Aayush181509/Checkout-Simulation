import time
def regularlane_process_customer(self,lane):
        # while not self.customer.empty():
        while not self.customer.empty():
            # print(self.customer.get())
            for i in range(10):
                if not self.customer.empty():
                    self.count+=1
                    # alane = self.get_lane()
                    lane.add_customer(self.customer.get())
                    # lane.process_customer()
                    # self.count-=1
                    # lane.add_customer(self.customer.get())                    
                    
                else:
                    # self.generate_customers(random.randint(5,10))
                    pass
            self.display_lane_info()
            for i in range(10):
                lane.process_customer()
                self.count-=1

            self.display_lane_info()
            time.sleep(2)