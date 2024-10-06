class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0  # Initialize size to 0
  
    def __str__(self):
        icon = "🍪"
        if self.size >= 1:
            return icon * self.size
        else:
            return ""
    
    def deposit(self, n):
        if not isinstance(n, int):
            raise ValueError("Cookie must be an integer")
        insert = n + self.size
        if insert > self.capacity:
            raise ValueError("Jar overload")
        self.size = insert

    def withdraw(self, n):
        if not isinstance(n, int):
            raise ValueError("Cookie must be an integer")
        withdraw = self.size - n
        if withdraw < 0:
            raise ValueError("Cant take what you dont have")
        self.size = withdraw


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int):
            raise ValueError("Jar capacity must be an integer")
        if capacity <= 0:
            raise ValueError("Jar capacity must be positive")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        self._size = value

def main():
    jar = Jar()  # Create an instance of Jar
    jar.deposit(3)  # Call deposit on the instance
    jar.withdraw(1)  #Call to withdraw on the instance
    jar.deposit(2)  # Call deposit on the instance
    print(f"Jar contains: {jar} Cookies")

if __name__ == "__main__":
    main()