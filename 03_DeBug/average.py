def average(nums):
    sum = 0
    n = 0
    for n in nums:
      sum += x
      n += 1
    avg = sum / n
    print(avg)

# 평균값은 22.857142857142858 이여야 함.
average([2, 4, 6, 8, 20, 50, 70]) 


#수정
def average(nums):
    sum = 0
    n = 0
    for n in nums:
      sum += n
      
    avg = sum / len(nums)
    print(avg)

# 평균값은 22.857142857142858 이여야 함.
average([2, 4, 6, 8, 20, 50, 70])
