# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# lredinger,191126,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #
# Class Product creates an object (product_object = name, price)
# Each product_object gets loaded into lstOfProductObjects
# Data -------------------------------------------------------------------- #
import os
strFileName = 'products.txt'
lstOfProductObjects = []

class MenuOutOfRange(Exception):
    pass

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        lredinger,191126,Modified code to complete assignment 8
    """
    #invCount = 0  # used for debugging

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
        # Product.invCount += 1  # used for debugging, to make sure objects were instantiated correctly

    def __str__(self):
        return '[{}, ${}]'.format(self.product_name, self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        lredinger,191126,Modified code to complete assignment 8
    """

    # Code to process data from a file
    @staticmethod
    def ReadFileDataToList(strFileName, lstOfProductObjects):
        """
        Reads data from a file into a list of dictionary rows

        :param strFileName: (string) with name of file:
        :param : lstOfProductObjects (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        with open("products.txt", "r") as strFileName:
            for line in strFileName:
                lstOfProductObjects.append(line)
            for prodObj in lstOfProductObjects:
                print(prodObj)
    # Code to process data to a file
    @staticmethod
    def save_data_to_file(strFileName, lstOfProductObjects):
        with open(strFileName, "w") as objFile:
            for prodObj in lstOfProductObjects:  # Write each row of data to the file
                objFile.write(str(prodObj))
# Processing  END------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Input/Output functions:

    methods:
        strMenu displays menu to customer

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        lredinger,191126,added strMenu, get_user_choice, show_product_lst, and add_product_to_list
    """
    # code to show menu to user
    @staticmethod
    def strMenu():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print("""
            ==========User Menu===========
            1. Add Product to list
            2. Show all Products 
            3. Save and Quit
            ===============================
           """)
        print()  # Add an extra line for looks
    # code to get user's choice
    @staticmethod
    def get_user_choice():
        # print(strMenu)
        while True:
            try:
                usrChoice = int(input("\nWhat would you like to do? "))
                return usrChoice
            except ValueError as e:  # user entered str instead of int
                print("\n!!!ERROR!!!\nThat's not a valid menu option")
                print("Menu option cannot be text: ", e)

    # Code to show the current data from the file to user
    @staticmethod
    def show_product_lst():
        for Product in lstOfProductObjects:
            print(Product)

    # Code to get product data from user
    @staticmethod  # creates an object instance of Class Product
    def add_product_to_list():
        product_name = input("Add a product: ")
        product_price = input("Enter a price for " + product_name + " : ")

        prodObj = Product(product_name, product_price)
        lstOfProductObjects.append(prodObj)

        print("You added " + Product.__str__(prodObj) + " to your inventory")
        # print(str(Product.invCount))  # used for debugging
        return

# Presentation (Input/Output) END-------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
if os.path.exists("products.txt"):  # searches for existing file
    print("Your current inventory contains the following products: ")
    FileProcessor.ReadFileDataToList(strFileName, lstOfProductObjects)

while True:
    # Show user a menu of options
    IO.strMenu()
    # Get user's menu option choice
    usrChoice = IO.get_user_choice()

    try:
        # Let user add data to the list of product objects
        if usrChoice not in range(1, 4):
            raise MenuOutOfRange  # user must choose int from menu options
        elif usrChoice == 1:
            IO.add_product_to_list()
        # Show user current data in the list of product objects
        elif usrChoice == 2:
            IO.show_product_lst()
        # let user save current data to file and exit program
        elif usrChoice == 3:
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            print("The following products have been saved!")
            IO.show_product_lst()
            break

# Main Body of Script  ---------------------------------------------------- #
# Error Handling
    except MenuOutOfRange:  # user entered int not matched to menu
        print("\n!!!ERROR!!!\nYour selection is out of range.\nPlease select a menu option between 1-4")
