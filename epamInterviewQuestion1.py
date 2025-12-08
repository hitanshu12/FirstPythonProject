"""
Write a Python program using a class where:
	•	Two numbers are taken from the user
	•	Stored inside the class
	•	A class method or instance method is used to print the sum of the two numbers
"""

input1 = int(input("Enter your first number: "))
input2 = int(input("Enter your second number: "))
class addition:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

add = addition(input1, input2)
print(add.sum())


"""
Find the longest substring without repeating characters.
"""

def longest_substring_without_repeating(s: str):
    last_index = {}
    left = 0
    best_start = 0
    best_len = 0

    for right, ch in enumerate(s):
        if ch in last_index and last_index[ch] >= left:
            left = last_index[ch] + 1

        last_index[ch] = right
        if right - left + 1 > best_len:
            best_len = right - left + 1
            best_start = left

    return s[best_start:best_start + best_len]


print(longest_substring_without_repeating("abcabcbb"))




