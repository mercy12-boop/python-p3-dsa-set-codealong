# Set Data Structure Code Along (CodeGrade)


# def first_repeated_value(list):
#     for i in range(0, len(list)):
#         for j in range(i+1, len(list)):
#             if list[i] == list[j]:
#                 return list[i]
#     return None

# print(first_repeated_value([1,2,3,3,4,4]))


# Let's make our own version of Python's Set class to understand how these methods might work under the hood. We'll build a MySet class using Python that has the following methods:

# __init__: Initializes a new MySet and adds any values from a list.
# has(value): Checks if the value is already included in the MySet. Must have a O(1) runtime.
# add(value): Adds the value to the MySet if it isn't already present. Must have a O(1) runtime.
# delete(value): Removes the value from the MySet. Must have a O(1) runtime.
# size(): Returns the number of elements in the MySet.

class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def __str__(self):
        set_list = []
        for key, value in self.dictionary.items():
            set_list.append(str(key))
        return f'MySet: {{{",".join(set_list)}}}'

    def add(self, value):
        self.dictionary[value] = True # Add a value as a key on the Dictionary
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()


