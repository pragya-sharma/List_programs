'''
Aim: Can you use the addition assignment operator,+= ,with two lists?
'''
l1 = list(map(int,input("enter values for list").split()))
l = list(map(int,input("enter values for append by += in list").split()))
l1 += l
print("ues of += with two lists",l1)

