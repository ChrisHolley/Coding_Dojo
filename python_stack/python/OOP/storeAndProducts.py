
# Start by creating a Store class that has 2 attributes: a name and a list of products. The name must be provided upon creation, but the products list should be empty.
# Let's also give some methods to our Store class:
# add_product(self, new_product) - takes a product and adds it to the store
# sell_product(self, id) - remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
# inflation(self, percent_increase) - increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
# set_clearance(self, category, percent_discount) - updates all the products matching the given category by reducing the price by the percent_discount given (use the method 
# you wrote in the Product class!)

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.product_list = []
        print("Store created:", store_name)
    def add_product(self, new_product):
        self.product_list.append(new_product)
        print(new_product, "added to store:", self.store_name)
    def print_list(self):
        for p in range(len(self.product_list)):
            print(self.product_list[p])
        print(self.product_list)


# Next, create a Product class that has 3 attributes: a name, a price, and a category. All of these should be provided upon creation.
# Let's give some methods to our Product class:
# update_price(self, percent_change, is_increased) - updates the product's price. If is_increased is True, the price should increase by the percent_change provided. If False, the price should decrease by the percent_change provided.
# print_info(self) - print the name of the product, its category, and its price.

class Product:
    def __init__(self, product_name, product_price, product_category):
        self.product_name = product_name
        self.product_price = product_price
        self.product_category = product_category
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.product_price = self.product_price * (percent_change/100 + 1)
            print("Updated Price(increased):", self.product_price)
        else:
            self.product_price = self.product_price * (1 - (percent_change/100))
            print("Updated Price:(decreased)", self.product_price)
    def print_info(self):
        print(self.product_name, self.product_category, "Price: $", self.product_price)

tp = Product("charmin", 5, "toiletry")
tp.print_info()
store_7_11 = Store("store_7_11")
store_7_11.add_product(tp)
store_7_11.print_list




