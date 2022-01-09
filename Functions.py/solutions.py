# 1. Write a Python function to find the Max of three numbers.
# Solution:
def my_max(a, b, c):
    if a > b > c:
        return a
    elif b > c > a:
        return b
    else:
        return c
print(my_max(21, 12, 22))
# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def my_sum(lst):
    add = 0
    for i in lst:
        add += i
    return add

print(my_sum([1,2,3,4,5]))
