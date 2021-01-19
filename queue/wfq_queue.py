QUEUE_COUNT = 3
PACKET_VALUE = 100


# Node for a linked link
class QueueNode:
    def __init__(self, f, sf, power, next_item=None):
        self.f = f
        self.sf = sf
        self.power = power
        self.next = next_item


class LinkedLink:
    def __init__(self, priority=None):
        self.head = None
        self.tail = None
        self.active_r = 0
        self.priority = priority
        self.sf = 0

    def add(self, f, sf, power):
        if self.head is None:
            self.head = QueueNode(f, sf, power, None)
            self.tail = self.head
        else:
            item = QueueNode(f, sf, power, None)
            self.tail.next = item
            self.tail = item


class WFQ:
    @staticmethod
    def push(power, queue_number):
        queue = queue_array[queue_number - 1]
        queue.active_r += power
        f = power / queue.priority
        sf = f + queue.sf
        queue.sf = sf
        queue.add(f, sf, power)


class WFQDelete:
    def __init__(self):
        self.t = 0
        self.prev_t = 0
        self.v_t = 1 / sum([queue.active_r for queue in queue_array if queue.head])

    def pop(self):
        f = [queue.head.f for queue in queue_array if queue.head]
        minim_f = min(f)
        all_f_queue = [
            _id
            for _id, queue in enumerate(queue_array)
            if queue.head and queue.head.f == minim_f
        ]
        queue_f = queue_array[all_f_queue.pop(0)]
        self.t += queue_f.head.power / queue_f.priority
        sf = [queue.head.sf for queue in queue_array if queue.head]
        minim_sf = min(sf)
        all_sf_queue = [
            _id
            for _id, queue in enumerate(queue_array)
            if queue.head and queue.head.sf == minim_sf
        ]
        while True:
            pop_queue = all_sf_queue.pop(0)
            queue = queue_array[pop_queue]
            min_sf = queue_array[pop_queue].head.sf
            tmp_t = (
                self.prev_t + (min_sf - self.v_t) * queue_f.active_r / queue_f.priority
            )
            if tmp_t > self.t:
                self.v_t += (self.t - self.prev_t) * queue_f.priority / queue_f.active_r
                self.prev_t = self.t
                print(queue.head.sf, queue.priority)
                queue.head = queue.head.next
                return
            self.prev_t = tmp_t
            self.v_t = min_sf
            queue_f.active_r -= queue.head.power


# Queue initialization
queue_array = []
for i in [1, 1, 2]:
    queue_array.append(LinkedLink(i))

WFQ.push(10, 1)
WFQ.push(10, 2)
WFQ.push(10, 2)
WFQ.push(10, 3)
WFQ.push(10, 3)
WFQ.push(10, 3)
WFQ.push(10, 3)
WFQ.push(10, 3)

print("All queue: ")
for i in queue_array:
    curr = i.head
    while curr:
        print(curr.f, curr.sf)
        curr = curr.next

w = WFQDelete()
for i in queue_array:
    curr = i.head
    while curr:
        w.pop()
        curr = curr.next
# Pop last item
w.pop()

for i in queue_array:
    curr = i.head
    while curr:
        print(curr.f, curr.sf)
        curr = curr.next
