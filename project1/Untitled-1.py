max_num = 150 

def find_max(nums):
   max_num = float("-inf") # smaller than all other numbers
   for num in nums:
       if num > max_num:
        max_num = num
        return (max_num)

max_calculated = find_max({78,78,66})
print(max_calculated)

