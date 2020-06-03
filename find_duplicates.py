#  Make the list with some duplicates
# two lists
# no_duplicates
example_list = ["1", "1", "lemon", "banana", "lemon", "5", "3", "5", "7", "3", "5", "3", "5", "7", "3"]

def remove_duplicates(example_list):
    no_duplicates = []
    for item in example_list:
        if no_duplicates.count(item) < 1:
            no_duplicates.append(item)
    return no_duplicates


print(remove_duplicates(example_list))


