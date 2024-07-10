n =int(input("Nechtalik list kiritasiz:  "))
lst1 =[]

for i in range(n):
    lst1.append(int(input(f"{i+1}-chi elementni kiriting: ")))
lst2 = []
x =len(lst1)
for i in range(1,x):
    lst2.append(lst1[i]-lst1[i-1])
print(max (lst2))


