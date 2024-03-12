def find_middle_element(lst):
    length = len(lst)
    middle_index = length // 2

    if length % 2 == 0:
        return lst[middle_index]
    else:
        return lst[middle_index]

user_input = input("Enter a list of numbers separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

result = find_middle_element(user_list)
print("Middle element:", result)