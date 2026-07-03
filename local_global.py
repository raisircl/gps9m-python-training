user ="Mohan"  
# this  variable defined in global scope it will not overwrite by local variable 
# if that has same name as per global variable
def sayhello():
    global user
    user="Ram" # user is local variable and accessible only in sayhello function
    print(f"Hello {user}")

sayhello()
print(f"Hello {user}") # here outside the sayhello we can not access user var

