
class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: ${self.price}, Stock: {self.stock}"

    def update_stock(self, quantity):
        self.stock -= quantity

class Catalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def view_products(self):
        return [str(product) for product in self.products]

    def find_product(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None


class Order:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            self.total += product.price * quantity
            product.update_stock(quantity)
        else:
            print(f"Sorry, only {product.stock} items in stock.")

    def view_order(self):
        order_details = "\n".join([f"{product.name} x{quantity} - ${product.price * quantity}" for product, quantity in self.items])
        return f"Order Details:\n{order_details}\nTotal: ${self.total}"


class Store:
    def __init__(self):
        self.catalog = Catalog()
        self.orders = []

    def add_product_to_catalog(self, product):
        self.catalog.add_product(product)

    def place_order(self):
        order = Order()
        while True:
            self.show_catalog()
            product_id = input("Enter product ID to add to cart (or 'done' to finish): ")
            if product_id.lower() == 'done':
                break
            product = self.catalog.find_product(product_id)
            if product:
                quantity = int(input(f"Enter quantity for {product.name}: "))
                order.add_item(product, quantity)
            else:
                print("Product not found.")

        if order.items:
            self.orders.append(order)
            print("Order placed successfully.")
        else:
            print("No items in order.")

    def show_catalog(self):
        for product_info in self.catalog.view_products():
            print(product_info)

    def view_orders(self):
        for i, order in enumerate(self.orders):
            print(f"Order {i+1}:")
            print(order.view_order())



def main():
    store = Store()

    # Adding some products to the catalog for demonstration
    store.add_product_to_catalog(Product("001", "Laptop", 999.99, 10))
    store.add_product_to_catalog(Product("002", "Smartphone", 499.99, 20))
    store.add_product_to_catalog(Product("003", "Headphones", 79.99, 50))

    while True:
        print("\nE-Commerce Store")
        print("1. View Catalog")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            store.show_catalog()

        elif choice == '2':
            store.place_order()

        elif choice == '3':
            store.view_orders()

        elif choice == '4':
            print("Exiting the store.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": 
    main()