# yield thaklei generator
# yield does not hold the whole result at a time
# It yields one item at a time

def square_makers(nums):
    for i in nums:
        yield (i*i)


nums = square_makers([1, 2, 3, 4, 5, 6])

for n in nums:
    print(n)


# list comprehensions 
lis = [1, 2, 3, 4, 5]
res = [n*n for n in lis]

print(res)

# Make generator using list comprehension 
# just use () isstead of []
lis = [1, 2, 3, 4, 5]
res = (n*n for n in lis)

print(res)
print(list(res))