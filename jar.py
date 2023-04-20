class Jar:
    def __init__(self, capacity=12):
        # Create a cookie jar with a certain capacity
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        # A string representation of the cookie jar is returned
        return "🍪" * self.cookies

    def deposit(self, n):
        # Add a certain number of cookies to the jar
        if not isinstance(n, int) or n < 0:
            raise ValueError(
                "Number of cookies to deposit must be a non-negative integer"
            )
        if self.cookies + n > self.capacity:
            raise ValueError("Cookie jar capacity exceeded")
        self.cookies += n

    def withdraw(self, n):
        # Remove a certain number of cookies in the jar
        if not isinstance(n, int) or n < 0:
            raise ValueError(
                "Number of cookies to withdraw must be a non-negative integer"
            )
        if n > self.cookies:
            raise ValueError("Not enough cookies in jar")
        self.cookies -= n

    @property
    def size(self):
        # Return the number of cookies left in the jar
        return self.cookies
