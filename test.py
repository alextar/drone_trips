from copy import deepcopy
from typing import List
from typing import Dict


def shipment(items: List[Dict], drone: Dict, trip: int = 1, initial: bool = True) -> None:

    if initial:
        # sort items by weight from heavier to lighter
        # do this only for the first function call (initial=True)
        items.sort(key=lambda x: x.get('weight'), reverse=True)
        print(drone.get('name'))

    capacity = drone.get('capacity')
    loading_weight = 0
    selected_items = []

    def drone_loaded() -> None:
        """
        Print selected items
        Check if we still have items in list and initiate next trip
        :return:
        """
        print(f'location {", ".join(selected_items)}')
        if len(items):
            shipment(items, drone, trip=trip + 1, initial=False)

    print(f'trip #{trip}')

    # copy items to keep original collection without changes
    item_iterator = iter(deepcopy(items))

    while True:
        try:
            item = next(item_iterator)
            item_weight = item.get('weight')
            # check if it's possible to add next item
            if item_weight + loading_weight <= capacity:
                loading_weight += item_weight
                # add item to selected items
                selected_items.append(item.get('name'))
                # remove item from available items list
                items.remove(item)

            # check if item weight less then drone capacity
            elif item_weight > capacity:
                # if item weight > capacity remove it from the list
                items.remove(item)

            if loading_weight == capacity:
                raise StopIteration()

        except StopIteration as e:
            # print current trip and initiate next
            drone_loaded()
            break


test_items = [{'name': 'test1', 'weight': 23},
          {'name': 'test2', 'weight': 15},
          {'name': 'test3', 'weight': 17}]
test_drone = {'name': 'drone 1', 'capacity': 40}

shipment(test_items, test_drone)





