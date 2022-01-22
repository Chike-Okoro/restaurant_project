class Restaurant():
    """Modelling a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the attributes that represents a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    
    def describe_restaurant(self):
        """Simulate a descriptive restaurant in response to a command"""
        print(self.restaurant_name.title() + " is a prestigous restaurant that serves the best " + self.cuisine_type.title())


    def open_restaurant(self):
        """Simulate a welcoming restaurant in response to a command"""
        print("Welcome to " + self.restaurant_name.title() + ". We are opened!!!")

    def set_number_served(self, number_served):
        """Simulate a command that sets the number of customers served"""
        self.number_served = number_served
        print("Customers served: " + str(self.number_served))

    def increment_number_served(self, number_of_customers):
        """Simulate a command that sets an increment to the number of customers who have been served"""
        self.number_served += number_of_customers
        print("Total number of customers served: " + str(self.number_served))
    
class IceCreamStand(Restaurant):
    """Represents part of the services the restaurant offers, ice cream to be specific"""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint', 'banana', 'gelato']


    def display_flavors(self):
        """Print a statement that displays the ice cream flavors"""
        print("Ice Cream Flavors:")
        for flavors in self.flavors:
            print(flavors.title())
