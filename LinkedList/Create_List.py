class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        return self.head

    def insert_first(self,data):
        new_node = Node(data)
        if self.head is None:
             self.head = new_node
             return self.head
        new_node.next = self.head
        self.head = new_node
        return self.head

    def traverse(self):
        if self.head is None:
            print("The List is Empty")
            return
        temp = self.head
        while temp:
            print(temp.data,end=" => ")
            temp = temp.next
        print("NULL")

    def delete_first(self):
        if self.head is None:
            print("Nothing to delete .. !")
            return
        temp = self.head
        self.head = temp.next
        temp = None
        return self.head

    def delete_last(self):
        if self.head is None:
            print("Nothing to delete .. !")
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        return self.head

    def count(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return count

    def is_cycle(self):
        pass

    def middle_element(self):
        pass

    def reverse_list(self):
        pass

    def rotate_list(self):
        pass


if __name__ == "__main__":

    list = LinkedList()
    print("Enter your choice ")
    while (1):
        print("0 : Quit")
        print("1 : Insert at last ")
        print("2 : Insert at first ")
        print("3 : Delete the first element ")
        print("4 : Delete the last element ")
        print("5 : Count Elements ")
        print("9 : Display")

        n = int(input("Selection : "))
        if n == 1:
            nn = int(input("Enter the value  "))
            list.insert(nn)
            list.traverse()
        elif n == 2:
            nn = int(input("Enter the value  "))
            list.insert_first(nn)
            list.traverse()
        elif n == 3:
            list.delete_first()
            list.traverse()
        elif n == 4:
            list.delete_last()
            list.traverse()
        elif n == 5:
            print("The Count is : ", list.count())

        elif n == 9:
            list.traverse()

        elif n == 0:
            break
        else:
            print("Wrong Selection !!!")









