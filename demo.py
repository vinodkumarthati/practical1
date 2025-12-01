class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end


    # Display list
    def display(self):
        temp = self.head
        print("Linked List: ", end="")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Driver Code (Main Program)
if __name__ == "__main__":
    ll = LinkedList()

    # Insert at beginning
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(10)

    
    # Display final list
    ll.display()
