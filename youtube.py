def queue_time(customers,n):
    if len(customers)==0:
        return 0
    
    if len(customers) <= n:
        time = max(customers)
        return time
    
    if len(customers) > n:
        cashier_queues = [0] * n
        for j in customers:
            cashier_queues.sort()
            cashier_queues[0] += j
        return max(cashier_queues)