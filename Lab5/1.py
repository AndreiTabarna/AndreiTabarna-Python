### 1. Formulas for shapes:
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
        
circle = Circle(radius=5)
print("Circle Area: {:.2f}".format(circle.area()))
print("Circle Perimeter: {:.2f}".format(circle.perimeter()))

rectangle = Rectangle(width=4, height=6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

triangle = Triangle(side1=3, side2=4, side3=5)
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())

### 2. Bank Account System:
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
        else:
            print("Exceeded overdraft limit")
            
savings_account = SavingsAccount(balance=1000, interest_rate=0.05)
savings_account.deposit(500)
print("Savings Account Balance:", savings_account.balance)
print("Interest Earned:", savings_account.calculate_interest())

checking_account = CheckingAccount(balance=800, overdraft_limit=200)
checking_account.withdraw(1000)
print("Checking Account Balance:", checking_account.balance)

### 3. Vehicle Hierarchy:
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def calculate_mileage(self):
        pass

class Motorcycle(Vehicle):
    def calculate_mileage(self):
        pass

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return self.towing_capacity
        
car = Car(make="Toyota", model="Corolla", year=2022)
print("Car Make:", car.make)
print("Car Model:", car.model)

motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2021)
print("Motorcycle Make:", motorcycle.make)
print("Motorcycle Model:", motorcycle.model)

truck = Truck(make="Ford", model="F-150", year=2020, towing_capacity=5000)
print("Truck Towing Capacity:", truck.calculate_towing_capacity())

### 4. Employee Hierarchy:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Engineer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class Salesperson(Employee):
    def __init__(self, name, salary, sales_target):
        super().__init__(name, salary)
        self.sales_target = sales_target
        
manager = Manager(name="Alice", salary=60000, department="Sales")
print("Manager Name:", manager.name)
print("Manager Salary:", manager.salary)

engineer = Engineer(name="Bob", salary=70000, programming_language="Python")
print("Engineer Name:", engineer.name)
print("Engineer Salary:", engineer.salary)

salesperson = Salesperson(name="Charlie", salary=50000, sales_target=100000)
print("Salesperson Name:", salesperson.name)
print("Salesperson Salary:", salesperson.salary)

### 5. Animals Hierarchy:
class Animal:
    def __init__(self, species):
        self.species = species

class Mammal(Animal):
    def __init__(self, species, fur_color):
        super().__init__(species)
        self.fur_color = fur_color

class Bird(Animal):
    def __init__(self, species, wingspan):
        super().__init__(species)
        self.wingspan = wingspan

class Fish(Animal):
    def __init__(self, species, habitat):
        super().__init__(species)
        self.habitat = habitat
        
mammal = Mammal(species="Lion", fur_color="Golden")
print("Mammal Species:", mammal.species)
print("Mammal Fur Color:", mammal.fur_color)

bird = Bird(species="Eagle", wingspan=2.5)
print("Bird Species:", bird.species)
print("Bird Wingspan:", bird.wingspan)

fish = Fish(species="Salmon", habitat="Freshwater")
print("Fish Species:", fish.species)
print("Fish Habitat:", fish.habitat)


### 6. Library Catalog System:
class LibraryItem:
    def __init__(self, title, author, item_type):
        self.title = title
        self.author = author
        self.item_type = item_type
        self.checked_out = False

    def check_out(self):
        self.checked_out = True

    def return_item(self):
        self.checked_out = False

class Book(LibraryItem):
    def __init__(self, title, author, genre):
        super().__init__(title, author, item_type="Book")
        self.genre = genre

class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        super().__init__(title, author=director, item_type="DVD")
        self.duration = duration

class Magazine(LibraryItem):
    def __init__(self, title, publisher, issue_number):
        super().__init__(title, author=publisher, item_type="Magazine")
        self.issue_number = issue_number

book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction")
print("Book Title:", book.title)
print("Book Author:", book.author)

dvd = DVD(title="Inception", director="Christopher Nolan", duration=150)
print("DVD Title:", dvd.title)
print("DVD Duration:", dvd.duration)

magazine = Magazine(title="National Geographic", publisher="National Geographic Society", issue_number=250)
print("Magazine Title:", magazine.title)
print("Magazine Issue Number:", magazine.issue_number)
