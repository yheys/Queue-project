class Queue:
    def __init__(self):
        self.items=[]

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "the queue is empty"

    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            print("their is nothing")
            return None
        return self.items[0]

    def display(self):
        if self.is_empty():
            print("their is nothing")
            return None
        print(self.items)

yheys=Queue()

while True:
    print("this is the manu")
    print(" 1 Enqueue(add item)")
    print(" 2 Dequeue(remove item)")
    print(" 3 Peek(show the first element)")
    print(" 4 Display (show all the elements)")
    print(" 5 Exit")

    choice=int(input("What do you want: "))

    if choice==1:
        added=int(input("enter the item to enqueue: "))
        yheys.enqueue(added)
        print(f" {added} is added")

    elif choice== 2:
        removed=yheys.dequeue()
        if removed is not None:
            print(f"{removed} is removed")

    elif choice ==3:
        first_element=yheys.peek()
        if first_element is not None:
            print(f"{first_element} is first element")

    elif choice== 4:
        yheys.display()

    elif choice==5:
        print("Thenks for using")
        break

    else:
        print("Invalid Choice!")







