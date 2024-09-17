x=[]

num = int(input("Enter a number: "))



def remove_prime(numbers):
 return [num for num in numbers if num % 2 == 0]


while True:

 num = int(input("Enter a number: "))

 x.append(num)
 if num == 0:
    break


newList=remove_prime(x)

print(f"the original list is {x}")
print(f"the new list is {newList}")