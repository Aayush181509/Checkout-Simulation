from queue import Queue

# Create a queue
my_queue = Queue()
class Item:
    def __init__(self) -> None:
        self.id = 1
        self.name = 'Alice'

    def display(self):
        self.val = 9
        return self.val




# Enqueue some objects for demonstration
i = Item()
# my_queue.put((i.id,i.name,i.display()))
# my_queue.put((i.id,i.name))
# my_queue.put((i.id,i.name))
my_queue.put(i)
my_queue.put(i)
my_queue.put(i)

# Function to access information about the objects in the queue
# def access_info(queue):
#     while not queue.empty():
#         obj = queue.get()
#         print("Object Info:", obj)
        # Do further processing with the object's information

# Access information about the objects in the queue
# access_info(my_queue)
c = list(my_queue.queue)
for i in c:
    print(i.display())
# c = [i.display() for i in my_queue.queue]


