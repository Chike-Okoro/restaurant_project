from restaurant import Restaurant, IceCreamStand

print("\n")
restaurant = Restaurant('kilimanjaro', 'african salad')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(40)
restaurant.increment_number_served(80)

print("\n----------WELCOME TO THE ICE CREAM STAND------------------")
sweet_tooth = IceCreamStand('sweet tooth', 'ice cream')
sweet_tooth.display_flavors()