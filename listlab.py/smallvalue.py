#small value
def small(list):
  low_num = list[0]
  for n in list:
    if n < low_num:
        low_num = n
  return low_num


nums = [9, 3, 8, 11, 5, 29, 2]
print(small(nums))