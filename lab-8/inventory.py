import json
import os
from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from supplier import Supplier


class Inventory:
    def __init__(self):
        self.__products = []


    def add_product(self, product):
        self.__products.append(product)


    def search_product(self, product_id):
        for item in self.__products:
            if item.get_product_id() == product_id:
                return item
        return None

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------")
        for item in self.__products:
            item.display_information()
        print("------------------------------------------------")
        return None

    def get_all(self):
        return self.__products

    def save(self):
        data = []
        for product in self.__products:
            data.append(product.to_dict())
        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

    def load(self, default_supplier: Supplier) -> None:
        if os.path.exists("inventory.json"):
            print("inventory.json found.")
            with open("inventory.json", "r") as file:
                data = json.load(file)
            for item in data:
                if item.get("type") == "digital":
                    product = DigitalProduct(item["ID"], item["Name"], item["Price"], item["stock"], item["download_size"], default_supplier)
                else:
                    product = PhysicalProduct(item["ID"], item["Name"], item["Price"], item["stock"], item.get("weight", 1.0), default_supplier)
                self.add_product(product)
            print("Inventory loaded successfully.")
        else:
            print("inventory.json not found, starting with empty inventory.")

    def update_stock(self, product_id, new_quantity):
        item = self.search_product(product_id)
        if item:
            return item.update_stock(new_quantity)
        else:
            print("Product not found")
            return False