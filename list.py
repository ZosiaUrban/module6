x=[]


def sumo():
 print(sum(x))


num = int(input("Enter a number: "))


while num != 0:
 x.append(num)
 num = int(input("Enter a number: "))


sumo()
