import random
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.hash_table: list = [None] * 8
        self.lenght = 0

    @staticmethod
    def count_of_elements(ls: list) -> int:
        count = 0
        for element in ls:
            if element is not None:
                count += 1
        return count

    def collision(self,
                  index: int,
                  ls: list,
                  key: Any = 0,
                  value: Any = 0) -> None:
        index = random.choice(
            [i for i in range(len(ls))
                if ls[i] is None])
        ls[index] = (key, value)
        self.lenght += 1

    def __len__(self) -> int:
        return self.lenght

    def __setitem__(self, key: Any, value: Any) -> None:
        threshhold = int(len(self.hash_table) * (2 / 3))
        if threshhold > self.count_of_elements(self.hash_table):
            index = self.__hash__(key) % len(self.hash_table)
            if all(x is None for x in self.hash_table):
                self.hash_table[index] = (key, value)
                self.lenght += 1
            elif any(
                item is not None and item[0] == key
                for item in self.hash_table):
                for item in self.hash_table:
                    if item[0] == key:
                        item[1] = value
            elif self.hash_table[index] is None:
                self.hash_table[index] = (key, value)
                self.lenght += 1
            else:
                # If we have collision
                self.collision(index, self.hash_table, key, value)
        else:
            # if we need to resaize hash table
            temp_list = [None] * (len(self.hash_table) * 2)
            for element in self.hash_table:
                if element is None:
                    continue
                index = hash(element) % len(temp_list)
                if all(x is None for x in self.hash_table):
                    self.hash_table[index] = (key, value)
                    self.lenght += 1
                elif any(
                    item is not None and item[0] == key
                    for item in self.hash_table):
                    for item in self.hash_table:
                        if item[0] == key:
                            item[1] = value
                elif temp_list[index] is None:
                    temp_list[index] = element
                else:
                    index = self.__hash__(key) % len(temp_list)
                    if temp_list[index] is None:
                        temp_list[index] = element
                    else:
                        # If we have collision
                        self.collision(index, temp_list, key, value)
            self.hash_table = temp_list
            index = self.__hash__(key) % len(self.hash_table)
            if self.hash_table[index] is None:
                self.hash_table[index] = (key, value)
                self.lenght += 1
            else:
                index = random.choice(
                    [i for i in range(len(self.hash_table))
                        if self.hash_table[i] is None]
                )
                self.hash_table[index] = (key, value)
                self.lenght += 1

    def __getitem__(self, key: Any) -> Any:
        if len(self.hash_table) != 0:
            for element in self.hash_table:
                if element is not None:
                    if key == element[0]:
                        return element[1]
        raise KeyError(key)

    def __hash__(self, value: Any) -> int:
        return hash(value)

    def __eq__(self, other: dict) -> None:
        return self.hash_table == other

    def clear(self) -> None:
        self.hash_table = [None] * self.lenght

    def __delitem__() -> None:
        pass

    def get() -> None:
        pass

    def pop() -> None:
        pass

    def update() -> None:
        pass

    def __iter__() -> None:
        pass
