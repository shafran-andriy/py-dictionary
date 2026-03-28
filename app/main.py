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

    def __len__(self) -> int:
        return self.lenght

    def __setitem__(self, key: Any, value: Any) -> None:
        threshhold = int(len(self.hash_table) * (2 / 3))
        hash_key = self.__hash__(key)
        if threshhold > self.count_of_elements(self.hash_table):
            index = hash_key % len(self.hash_table)
            if all(x is None for x in self.hash_table):
                self.hash_table[index] = (key,
                                          value,
                                          hash_key)
                self.lenght += 1
            elif any(
                item is not None
                and item[0] == key for item in self.hash_table
            ):
                for index, item in enumerate(self.hash_table):
                    if item is not None:
                        if item[0] == key:
                            self.hash_table[index] = (key,
                                                      value,
                                                      hash_key)
            elif self.hash_table[index] is None:
                self.hash_table[index] = (key,
                                          value,
                                          hash_key)
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
                    idx = hash(element[0]) % len(temp_list)
                    if temp_list[idx] is None:
                        temp_list[idx] = element
                    else:
                        # If we have collision
                        self.collision(idx, temp_list, element[0], element[1])
            # add new element in hash table after resize
            self.hash_table = temp_list
            self.lenght = self.count_of_elements(self.hash_table)
            index = hash_key % len(self.hash_table)
            if self.hash_table[index] is None:
                self.hash_table[index] = (key,
                                          value,
                                          hash_key)
                self.lenght += 1
            elif key not in self.get_keys_from_hash_table(self.hash_table):
                self.collision(index, self.hash_table, key, value)
                self.lenght += 1
            else:
                self.update(key, value)

    def __getitem__(self, key: Any) -> Any:
        if len(self.hash_table) != 0:
            for element in self.hash_table:
                if element is not None:
                    if (
                        key == element[0]
                        # and self.__hash__(key) == element[2]
                    ):
                        return element[1]
        raise KeyError(key)

    def __hash__(self, value: Any) -> int:
        return hash(value)

    def __eq__(self, other: list[tuple]) -> bool:
        for i in range(len(self.hash_table)):
            if (
                self.hash_table[i][0] != other[i][0]
                or self.hash_table[i][1] != other[i][1]
                or self.hash_table[i][2] != other[i][2]
            ):
                return False
        return True

    def clear(self) -> None:
        self.hash_table = [None] * 8
        self.lenght = 0

    def __delitem__(self, key: Any) -> None:
        for item in self.hash_table:
            if item[0] == key:
                self.hash_table.remove(item)

    def get(self, key: Any) -> Any:
        if key in self.get_keys_from_hash_table(self.hash_table):
            for i in self.hash_table:
                if i is not None:
                    if i[0] == key:
                        return i[1]

    def pop(self, key: Any) -> list:
        for i, item in enumerate(self.hash_table):
            if item[0] == key:
                return self.hash_table.pop(i)

    def update(self, key: Any, value: Any) -> list:
        hash_key = self.__hash__(key)
        if key in self.get_keys_from_hash_table(self.hash_table):
            for i, item in enumerate(self.hash_table):
                if item and item[0] == key:
                    self.hash_table[i] = (key,
                                          value,
                                          hash_key)
                    break
        return self.hash_table

    def __iter__(self) -> Any:
        for key in self.hash_table:
            if key is None:
                continue
            else:
                yield key[0]
