class Menu:
    def __init__(self, category, name, portion, price):
        self.category = category
        self.name = name
        self.portion = portion
        self.price = price
    #Menu Class is defined here

def read_menu(file):
    menu = []
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            category, name, portion, price = line.strip().split(";") #splitting the line due to ";" into 4 parts
            price = price.lstrip()
            price = float(price.lstrip("$"))
            menu.append(Menu(category, name, portion, price))
    return menu
    #read_menu function that reads the menu file and returns a list of Menu objects is defined here

def main():
    menu = read_menu("menu.txt")
    order = []
    total_price = 0
    categories = set([item.category for item in menu]) #create set of categories with list comprehension and with set function it secures there are no duplicate values.

    while True:
        print("Product Categories")
        for i, category in enumerate(categories): #enumerate function is used for printing the categories with numbers.
            print(f"{i+1}. {category}")
        choice = input("Please select product category: ")
        if not choice.isnumeric() or int(choice) not in range(1, len(categories)+1):
            print("Invalid input. Please try again.")
            continue

        selected_category = list(categories)[int(choice)-1]
        products = [item for item in menu if item.category == selected_category] 
        product_names = set([item.name for item in products]) 
        '''
        The method simply checks if the input is valid or not and if it is,
        it selects the category from categories set with choice input and then it creates a new list of products due to selected category with list comprehension,
        lastly it creates a set of product names due to products list.
         
        '''
        print(f"Products in {selected_category}")
        for i, name in enumerate(product_names):
            print(f"{i+1}. {name}")
        choice = input("Please select product name: ")
        if not choice.isnumeric() or int(choice) not in range(1, len(product_names)+1):
            print("Invalid input. Please try again.")
            continue
        selected_product = list(product_names)[int(choice)-1]
        product_portions = set([item.portion for item in products if item.name == selected_product]) 
        '''
        The method does the same thing as the previous one but it creates a set of product portions due to selected product.
        '''
        
        print(f"{selected_product} Portions")
        for i, portion in enumerate(product_portions):
            print(f"{i+1}. {portion}")
        choice = input("Please select product portion: ")
        if not choice.isnumeric() or int(choice) not in range(1, len(product_portions)+1):
            print("Invalid input. Please try again.")
            continue
        selected_portion = list(product_portions)[int(choice)-1]
        selected_item = [item for item in products if item.name == selected_product and item.portion == selected_portion][0] 
        #This creates another list named selected_item with list comprehension of the exactly selected product by previous steps then it selects the first element of that list.
        order.append(selected_item) #add selected item to order list that created start of the main function
        total_price += selected_item.price #add items price to total price that created start of the main function
        print("1. Add New")
        print("2. Checkout")
        choice = input("Please select an operation: ")
        if choice == "2": 
            break
        #If user selects to checkout break the menu loop and print the receipt.
        if not choice.isnumeric() or int(choice) not in range(1, len(product_portions)+1):
            print("Invalid input. Please try again.")
            continue
            

    print("\nReceipt:\n-------------------------------")
    for item in order:
        print(f"{item.name} ({item.portion}): ${item.price}")
    print("-------------------------------")
    print(f"Total price: ${total_price}")
    #receipt is printed with data from order list
main()
