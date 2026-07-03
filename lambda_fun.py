sqaure=lambda x: x*x

print(sqaure(5))

# working or application
def getlen(item):
    return len(item)

fruits=["Apple","Banana","Mango","Grapes"]
fruits_len=[]
#for x in fruits:
    #fruits_len.append(getlen(x))

fruits_len=list(map(lambda item:len(item), fruits))
print(fruits_len)