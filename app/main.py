import random
from typing import Any


class Dictionary:
    def __init__(self) -> None:
        # self.value = value
        self.hash_table: list = [None] * 8
        self._dict = dict()
        self.lenght = 0

    @staticmethod
    def count_of_elements(ls: list) -> int:
        count = 0
        for element in ls:
            if element is not None:
                count += 1
        return count
    
    def __len__(self) -> int:
        return self.lenght

    def __setitem__(self, key: Any, value: Any) -> None:
        # if len(self._dict) != 0:
        self.lenght = len(self._dict)
        threshhold = int(len(self.hash_table) * (2 / 3))
        if isinstance(value, (list, dict, set, bytearray)):
            raise TypeError("Unhashable type: 'list', 'dict', 'set', 'bytearray'")
        else:
            # c_l = self.count_of_elements(self.hash_table)
            if threshhold > self.count_of_elements(self.hash_table):
                index = self.__hash__(key) % len(self.hash_table)
                if self.hash_table[index] == None:
                    self.hash_table[index] = value
                    self._dict[key] = self.hash_table[index]
                else:
                    #If we have collision
                    index = random.choice(
                        [index for index in range(len(self.hash_table))
                            if self.hash_table[index] == None]
                        )
                    self.hash_table[index] = value
                    self._dict[key] = self.hash_table[index]
            else:
                # if we need to resaize hash table
                temp_list = [None] * (len(self.hash_table) * 2)
                for element in self.hash_table:
                    if element == None:
                        continue
                    index = hash(element) % len(temp_list)

                    if temp_list[index] is None:
                        temp_list[index] = element
                    else:
                        index = self.__hash__(key) % len(temp_list)
                        if temp_list[index] == None:
                            temp_list[index] = element
                            self._dict[key] = temp_list[index]
                        else:
                            #If we have collision
                            index = random.choice(
                            [index for index in range(len(temp_list))
                                if temp_list[index] == None]
                            )
                            temp_list[index] = value
                            self._dict[key] = temp_list[index]
                self.hash_table = temp_list
                index = self.__hash__(key) % len(self.hash_table)
                if self.hash_table[index] is None:
                    self.hash_table[index] = value
                else:
                    index = random.choice(
                        [i for i in range(len(self.hash_table)) if self.hash_table[i] is None]
                    )
                    self.hash_table[index] = value

                self._dict[key] = value

    def __getitem__(self, key: Any) -> Any:
        if key in self._dict:
            return self._dict.get(key)
        return "Key not found"

    def __hash__(self, value) -> int:
        return hash(value)

    def __eq__(self, other: dict) -> None:
        return self._dict == other
