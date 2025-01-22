class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    @property
    def is_empty(self):
        return self.head is None

    @property
    def size(self):
        return self.count

    def append(self, value):
        """Add element to the end of the list."""
        new_node = Node(value)

        if self.is_empty:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def prepend(self, value):
        """Add element to the beginning of the list."""
        new_node = Node(value)

        if self.is_empty:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1

    def insert(self, value, index):
        """Insert element at specific index."""
        if index < 0 or index > self.count:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.prepend(value)
            return

        if index == self.count:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head
        previous = None
        current_index = 0

        while current_index < index:
            previous = current
            current = current.next
            current_index += 1

        new_node.next = current
        previous.next = new_node
        self.count += 1

    def remove(self, index):
        """Remove element at specific index."""
        if self.is_empty:
            raise IndexError("Cannot remove from empty list")

        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")

        if index == 0:
            removed_value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            previous = None
            current_index = 0

            while current_index < index:
                previous = current
                current = current.next
                current_index += 1

            removed_value = current.value
            previous.next = current.next

            if index == self.count - 1:
                self.tail = previous

        self.count -= 1
        return removed_value

    def get(self, index):
        """Get element at specific index."""
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")

        current = self.head
        current_index = 0

        while current_index < index:
            current = current.next
            current_index += 1

        return current.value

    def __str__(self):
        """Convert list to string for printing."""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)

    def __len__(self):
        """Get the length of the list."""
        return self.count