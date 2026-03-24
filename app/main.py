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

    @staticmethod
    def get_keys_from_hash_table(ls: list[tuple | None]) -> list:
        return [i[0] for i in ls if i is not None]

    def collision(self,
                  index: int,
                  ls: list,
                  key: Any = 0,
                  value: Any = 0) -> None:
        index = random.choice(
            [i for i in range(len(ls))
                if ls[i] is None])
        ls[index] = (key, value)
        # self.lenght += 1

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
                item is not None
                and item[0] == key for item in self.hash_table
            ):
                for index, item in enumerate(self.hash_table):
                    if item is not None:
                        if item[0] == key:
                            self.hash_table[index] = (key, value)
            elif self.hash_table[index] is None:
                self.hash_table[index] = (key, value)
                self.lenght += 1
            else:
                # If we have collision
                self.collision(index, self.hash_table, key, value)
                self.lenght += 1
        else:
            # if we need to resize hash table
            temp_list = [None] * (len(self.hash_table) * 2)
            for element in self.hash_table:
                if element is None:
                    continue
                else:
                    index = hash(element[0]) % len(temp_list)
                    if temp_list[index] is None:
                        temp_list[index] = element
                    else:
                        # If we have collision
                        old_key, old_value = element
                        self.collision(index, temp_list, old_key, old_value)
            # add new element in hash table after resize
            self.hash_table = temp_list
            index = self.__hash__(key) % len(self.hash_table)
            if self.hash_table[index] is None:
                self.hash_table[index] = (key, value)
                self.lenght += 1
            elif self.hash_table[index] is not None:
                if key not in self.get_keys_from_hash_table(self.hash_table):
                    # If we have collision
                    self.collision(index, temp_list, key, value)
                else:
                    self.hash_table[index] = (key, value)

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
