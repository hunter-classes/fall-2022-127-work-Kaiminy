#small value
nums = [9, 3, 8, 11, 5, 29, 2]
low_num = 0
for n in nums:
    if n < low_num:
        low_num = n
print(low_num)