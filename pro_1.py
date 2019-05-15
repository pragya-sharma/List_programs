'''
Aim: List Comprehension with sutable examples:
'''
'''
Ex_1 : print all even no of that no which was entered by user .
'''
n = int(input("enter a no "))
l = [i  for i in range(0,n+1)  if i%2 == 0  ]
print("even no",l)
'''
Ex_2 : print square of all numbers of that no which was entered by user.
'''
n = int(input("enter a no"))
l = [i*i for i in range(0,n+1)]
print(l)
