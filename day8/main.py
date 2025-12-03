class User():
    def __init__(self, name : str, age: int):

        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if not isinstance(age, int):
            raise TypeError("age must be an integer")

        if len(name) < 2:
            raise ValueError("name must be at least 2 characters long")

        if age < 0 or age > 120:
            raise ValueError("age must be a valid human age")
        
        self.name = name
        self.age = age



user1 = User(name="Ali", age=15)
user2 = User(name="Ali", age="fifteen")

print(user1.__dict__)
print(user2.__dict__)