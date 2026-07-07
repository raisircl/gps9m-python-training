a=[2,3,40,9,60,7,8]
b=[]
# for i in a:
#     b.append(i**2)
# print(b)    
#list comprehension
b=[i**2 for i in a]
print(b)

# fetch even numbers from a
even_numbers=[i for i in a if i%2==0]
print(even_numbers)

# fetch those number which are devide by 2 and 5
divisible_by_2_and_5=[i for i in a if i%2==0 and i%5==0]
print(divisible_by_2_and_5)
