#Two Sum Problem: Given an array of integers, return indices of the two numbers such that they add 
#up to a specific target. You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.


def find_indices_for_sum(nums, target):
    num_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

# Take input from the user for the array
user_input = input("Enter a list of numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

# Take input from the user for the target sum
target = int(input("Enter the target sum: "))

result = find_indices_for_sum(nums, target)
print("Indices of the two numbers:", result)
