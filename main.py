from typing import Union
import lux_items
import items_class

items_class_list = list[Union[items_class.consumable_item, items_class.gun_item, items_class.normal_item]]

class inventory:
    def __init__(self, capacity: int = 2048) -> None:
        self.capacity_left: int = capacity
        self.items: list = []
    
    def add_item(self, item: items_class_list, count: int = 1):
        self.items.append(item)

    def get_all_items(self):
        return self.items

def create_item(name:str, weight:int):
    return items_class.normal_item(name, weight)

def main():
    inven = inventory()

    item_list: items_class_list = lux_items.items

    for i in item_list:
        print(i.name)
        if "yes" == input("Add to inventory? ").lower().strip():
            if "yes" == input("More than one? ").lower().strip():
                inven.add_item(i)

    stor: items_class_list = inven.get_all_items()

    for _ in stor:
    print()

if __name__ == "__main__":
    main()