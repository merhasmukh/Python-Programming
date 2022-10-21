list1 = [(1,4), (8, 6), (2,3), (9,8), (7, 6)]
  
print("The original list is : " + str(list1))
  
# initializing tuple
tup = (5, 7)
  
# initializing K 
K = 1
print(len(list1))
res = min(range(len(list1)), key = lambda x: abs(list1[x][K - 1] - tup[K - 1]))
print(list1[3])

