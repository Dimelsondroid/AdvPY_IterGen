
nested_list = [
    ['a', 'b', 'c', ['r', 'g']],
    ['d', 'e', 'f', [[1, [2, [3]]], [False]], 'h', False],
    [1, 2, None],
]


# Iterator
class MyIterator:

    def iter_next(self, item):
        for nested_i in item:
            if isinstance(nested_i, list):
                self.iter_next(nested_i)
            else:
                self.my_list.append(nested_i)

    def __init__(self, my_list):
        self.my_list = my_list
        self.limit = len(my_list)
        self.start = -1
        for item in my_list:
            self.start += 1
            if self.start == self.limit:
                del my_list[:self.limit]
                break
            self.iter_next(item)

    def __iter__(self):
        self.cursor = -1
        self.end = len(self.my_list)
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.end:
            raise StopIteration
        return self.my_list[self.cursor]


for i in MyIterator(nested_list):
    print(i)

flat_list = [item for item in nested_list]
print(flat_list)

#####################

nested_list = [
    ['a', 'b', 'c', ['r', 'g']],
    ['d', 'e', 'f', [[1, [2, [3]]], [False]], 'h', False],
    [1, 2, None],
]


# Generator
def my_generator(my_list):
    for item in my_list:
        if isinstance(item, list):
            for nested_item in my_generator(item):
                yield nested_item
        else:
            yield item


for i in my_generator(nested_list):
    print(i)

print(list(item for item in my_generator(nested_list)))
