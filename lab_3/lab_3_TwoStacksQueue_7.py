class TwoStacksQueue:
    
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        self.count_enqueue = 0
        self.count_dequeue = 0

    def enqueue(self, added_elem):
        # добавление элемента в очередь
        self.stack_in.append(added_elem)
        self.count_enqueue += 1
    
    def dequeue(self):
        # удаление элемента из начала очереди
        if self.is_empty():
            print("Очередь пуста")
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        self.count_dequeue += 1
        return self.stack_out.pop()
    
    def front(self):
        # просмотр первого элемента
        if self.is_empty():
            print("Очередь пуста")
            return None
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
    
    def is_empty(self):
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return True
        else:
            return False    

    
    def size(self):
        count_in = len(self.stack_in)
        count_out = len(self.stack_out)
        total = count_in + count_out
        return total
    
    def count_info(self):
        print("Количество операций enqueue:", self.count_enqueue)
        print("Количество операций dequeue:", self.count_dequeue)
        return 
    
# Демонстрация

if __name__ == "__main__":
    queue = TwoStacksQueue()
    queue.front()
    queue.enqueue("1 элемент")
    queue.enqueue("2 элемент")
    queue.enqueue("3 элемент")
    queue.enqueue("4 элемент")
    queue.enqueue("5 элемент")
    queue.enqueue("6 элемент")
    queue.enqueue("7 элемент")
    queue.enqueue("8 элемент")
    queue.enqueue("9 элемент")
    queue.enqueue("10 элемент")
    print(queue.front())
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(queue.front())
    queue.dequeue()
    queue.dequeue()
    print(queue.front())

    queue.count_info()