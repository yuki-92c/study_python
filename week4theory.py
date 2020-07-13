mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])
for x in mylist:
    print(x)

# mylist = [1,2,3]
# print(mylist[10])

def my_function():
    print("Hello From My Function!")
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" %(username,greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()
#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")
# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print(x)