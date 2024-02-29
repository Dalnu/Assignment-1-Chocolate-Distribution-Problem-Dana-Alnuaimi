# Name: Dana Ahmed Alnuaimi
# ID: 202203220

# Task1:
class Chocolate:  # Define a class for chocolates
    def __init__(self, id, weight, price, type):  # Constructor to initialize chocolate attributes
        self.id = id  # Unique identifier for the chocolate
        self.weight = weight  # Weight of the chocolate
        self.price = price  # Price of the chocolate
        self.type = type  # Type of the chocolate

# Function to distribute chocolates iteratively among students
def dIterative(chocolates, students):
    distributed_chocolates = {}  # Dictionary to store distributed chocolates
    student_index = 0  # Initialize index to track current student
    for chocolate in chocolates:  # Iterate through chocolates
        if student_index >= len(students):  # If all students have been covered, reset index
            student_index = 0
        student = students[student_index]  # Get current student
        if student not in distributed_chocolates:  # If student not in dictionary, add them
            distributed_chocolates[student] = []
        distributed_chocolates[student].append(chocolate)  # Add chocolate to student's list
        student_index += 1  # Move to the next student
    return distributed_chocolates  # Return dictionary of distributed chocolates

# Function to distribute chocolates recursively among students
def dRecursive(chocolates, students, distributed_chocolates=None, student_index=0):
    if distributed_chocolates is None:  # If dictionary not initialized, create it
        distributed_chocolates = {}
    if student_index >= len(students):  # If all students have been covered, return the distribution
        return distributed_chocolates
    student = students[student_index]  # Get current student
    if student not in distributed_chocolates:  # If student not in dictionary, add them
        distributed_chocolates[student] = []
    distributed_chocolates[student].append(chocolates[student_index % len(chocolates)])  # Add chocolate to student's list
    return dRecursive(chocolates, students, distributed_chocolates, student_index + 1)  # Recursive call for next student

# List of chocolates
chocolates = [ Chocolate("002", 5, 2, "Almond chocolate"), Chocolate("005", 7, 4, "Peanut butter chocolate"),
    Chocolate("007", 6, 3, "Hazelnut chocolate"), Chocolate("010", 8, 5, "Mint chocolate"),
    Chocolate("013", 4, 3, "Spicy chocolate"), Chocolate("016", 6, 4, "Orange chocolate")]

students = ["Dana", "Jamila", "Shamma", "Shaikah", "Salama", "Asma"]  # List of students

iterative_distribution = dIterative(chocolates, students)  # Perform iterative distribution
print("Iterative Distribution:")  # Print heading
for student, student_chocolates in iterative_distribution.items():  # Iterate through distributed chocolates
    print(f"{student}: {[(chocolate.id, chocolate.type) for chocolate in student_chocolates]}")  # Print student and their chocolates

recursive_distribution = dRecursive(chocolates, students)  # Perform recursive distribution
print("\nRecursive Distribution:")  # Print heading
for student, student_chocolates in recursive_distribution.items():  # Iterate through distributed chocolates
    print(f"{student}: {[(chocolate.id, chocolate.type) for chocolate in student_chocolates]}")  # Print student and their chocolates

# Test Cases:
def tDistribution(chocolates,
                  students):  # Define a function named tDistribution with parameters chocolates and students
    print("\nTest Cases:")  # Print a message to indicate the start of test cases
    print("1. chocolate = student:")  # Print a message for the case when chocolates are equal to students
    if len(chocolates) == len(students):  # Check if the number of chocolates is equal to the number of students
        print(
            "All chocolates can be distributed to each student.")  # If so, print a message saying all chocolates can be distributed to each student
    else:
        print(
            "Error: Number of chocolates doesn't match number of students.")  # Otherwise, print an error message indicating a mismatch in the numbers

    print("\n2. chocolate < student:")  # Print a message for the case when chocolates are less than students
    if len(chocolates) < len(students):  # Check if the number of chocolates is less than the number of students
        print(
            "Students are more than chocolates.")  # If so, print a message indicating there are more students than chocolates
    else:
        print(
            "Error: Number of chocolates is greater than or equal to the number of students.")  # Otherwise, print an error message indicating chocolates are sufficient or more

    print("\n3. chocolate > student:")  # Print a message for the case when chocolates are more than students
    if len(chocolates) > len(students):  # Check if the number of chocolates is greater than the number of students
        print(
            "Chocolates are more than students.")  # If so, print a message indicating there are more chocolates than students
    else:
        print(
            "Error: Number of chocolates is less than or equal to the number of students.")  # Otherwise, print an error message indicating chocolates are insufficient
        return

    print("\n3. chocolate < student:")  # Print a message for the case when chocolates are less than students
    for student, chocolate in zip(students, chocolates):  # Iterate over each student and chocolate using zip
        print(
            f"{student}: {[(chocolate.id, chocolate.type)]}")  # Print the student and the corresponding chocolate ID and type


tDistribution(chocolates, students)  # Call the tDistribution function with chocolates and students as arguments


# Task 2:
class Chocolate:
    def __init__(self, id, weight, price, type):
        self.id = id  # Initialize ID attribute
        self.weight = weight  # Initialize weight attribute
        self.price = price  # Initialize price attribute
        self.type = type  # Initialize type attribute

def sCWeight(chocolates):
    return sorted(chocolates, key=lambda x: x.weight)  # Sort chocolates by weight

def sCPrice(chocolates):
    return sorted(chocolates, key=lambda x: x.price)  # Sort chocolates by price

chocolates = [Chocolate("002", 5, 2, "Almond chocolate"), Chocolate("005", 7, 4, "Peanut butter chocolate"),
              Chocolate("007", 6, 3, "Hazelnut chocolate"), Chocolate("010", 8, 5, "Mint chocolate"),
              Chocolate("013", 4, 3, "Spicy chocolate"), Chocolate("016", 6, 4, "Orange chocolate")]

sWeight = sCWeight(chocolates)  # Sort chocolates by weight
print("Chocolates sorted by weight:")
for chocolate in sWeight:  # Print sorted chocolates by weight
    print(f"ID: {chocolate.id}, Weight: {chocolate.weight}, Price: {chocolate.price}, Type: {chocolate.type}")

sPrice = sCPrice(chocolates)  # Sort chocolates by price
print("\nChocolates sorted by price:")
for chocolate in sPrice:  # Print sorted chocolates by price
    print(f"ID: {chocolate.id}, Weight: {chocolate.weight}, Price: {chocolate.price}, Type: {chocolate.type}")

# Test Cases:
def tSorting(chocolates):  # Define a function named tSorting which takes a list of chocolates as input
    print("\nTest Cases:")  # Print a message indicating the start of test cases
    # Sort chocolates by weight
    sWeight = sCWeight(chocolates)  # Call the function sCWeight to sort chocolates by weight and store the result in sWeight
    print("Chocolates sorted by weight:")  # Print a message indicating the list of chocolates sorted by weight
    for chocolate in sWeight:  # Iterate over each chocolate in the sorted list by weight
        print(f"ID: {chocolate.id}, Weight: {chocolate.weight}, Price: {chocolate.price}, Type: {chocolate.type}")  # Print details of each chocolate

    sWeights = [chocolate.weight for chocolate in sWeight]  # Create a list of weights of chocolates in the sorted list by weight
    assert sWeights == sorted(sWeights), "Chocolates are not sorted by weight."  # Assert that the list of weights is sorted, raise an error message if not
    print("Chocolates are sorted by weight.")  # Print a message indicating that chocolates are sorted by weight

    sPrice = sCPrice(chocolates)  # Call the function sCPrice to sort chocolates by price and store the result in sPrice
    print("\nChocolates sorted by price:")  # Print a message indicating the list of chocolates sorted by price
    for chocolate in sPrice:  # Iterate over each chocolate in the sorted list by price
        print(f"ID: {chocolate.id}, Weight: {chocolate.weight}, Price: {chocolate.price}, Type: {chocolate.type}")  # Print details of each chocolate

    sPrices = [chocolate.price for chocolate in sPrice]  # Create a list of prices of chocolates in the sorted list by price
    assert sPrices == sorted(sPrices), "Chocolates are not sorted by price."  # Assert that the list of prices is sorted, raise an error message if not
    print("Chocolates are sorted by price.")  # Print a message indicating that chocolates are sorted by price

tSorting(chocolates)  # Call the function tSorting with the list of chocolates as input


# Task 3:
class Chocolate:  # Define a class named Chocolate
    def __init__(self, id, weight, price, type):  # Define constructor method for initializing object attributes
        self.id = id  # Initialize id attribute
        self.weight = weight  # Initialize weight attribute
        self.price = price  # Initialize price attribute
        self.type = type  # Initialize type attribute

chocolates = [Chocolate("002", 5, 2, "Almond chocolate"), Chocolate("005", 7, 4, "Peanut butter chocolate"),
              Chocolate("007", 6, 3, "Hazelnut chocolate"), Chocolate("010", 8, 5, "Mint chocolate"),
              Chocolate("013", 4, 3, "Spicy chocolate"), Chocolate("016", 6, 4, "Orange chocolate")]

def findSCprice(chocolates, price):  # Define a function to find a chocolate by price
    for chocolate in chocolates:  # Iterate through the chocolates list
        if chocolate.price == price:  # Check if the chocolate's price matches the given price
            return chocolate  # Return the chocolate if found
    return None  # Return None if no chocolate with the given price is found

def findSCweight(chocolates, weight):  # Define a function to find a chocolate by weight
    for chocolate in chocolates:  # Iterate through the chocolates list
        if chocolate.weight == weight:  # Check if the chocolate's weight matches the given weight
            return chocolate  # Return the chocolate if found
    return None  # Return None if no chocolate with the given weight is found

# Test Cases:
def tSearching(chocolates):  # Define a function to perform test cases
    print("\nTest Cases:")  # Print a message indicating the start of test cases
    # Search for a chocolate by price
    pSearch = float(input("Enter the price of the chocolate: "))  # Prompt user to enter price
    fcPrice = findSCprice(chocolates, pSearch)  # Call function to find chocolate by price
    if fcPrice:  # If chocolate with specified price is found
        print(f"Chocolate with price {pSearch} found. ID: {fcPrice.id}, Type: {fcPrice.type}")  # Print chocolate details
    else:  # If no chocolate with specified price is found
        print(f"No chocolate found with price {pSearch}.")  # Print message indicating no chocolate found

    wSearch = float(input("Enter the weight of the chocolate: "))  # Prompt user to enter weight
    fcWeight = findSCweight(chocolates, wSearch)  # Call function to find chocolate by weight
    if fcWeight:  # If chocolate with specified weight is found
        print(f"Chocolate with weight {wSearch} found. ID: {fcWeight.id}, Type: {fcWeight.type}")  # Print chocolate details
    else:  # If no chocolate with specified weight is found
        print(f"No chocolate found with weight {wSearch}.")  # Print message indicating no chocolate found

tSearching(chocolates)  # Call the test function with the chocolates list

