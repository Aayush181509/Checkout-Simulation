class Till:
    def __init__(self):
        self.time_remaining=0
        self.client_time=[]

def queueTime(queue,til):
    tills=[Till() for i in range(til)]
    offset_time=[]
    for c in queue:
        for i in range(til):
            if tills[i].time_remaining==0:
                tills[i].time_remaining=c
                tills[i].client_time.append(c)
                break;
        neg_time=min([j.time_remaining for j in tills])
        offset_time.append(neg_time)
        for t in tills:
            t.time_remaining-=neg_time
    offset_time.append(max([j.time_remaining for j in tills]))
    return sum(offset_time)
