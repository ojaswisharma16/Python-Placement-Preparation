"""# Pattern no 04. Inverted Number triangles:
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
n=int(input("Enter the Size of Number Triangle: "))

print("Pattern Number 04 :")
for i in range(n,0,-1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

"""# Pattern no 05. Inverted Number triangles:
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2
1
"""
print()
print("Pattern Number 05 :")
for i in range(n,0,-1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

"""# Pattern no 06. Inverted Number triangles:
15 14 13 12 11
10 9 8 7
6 5 4
3 2
1
"""
print()
print("Pattern Number 06 :")
num=0
for i in range(1,n+1):
    for j in range(1, i+1):
        num=num+1

for i in range(n,0,-1):
    for j in range(1, i+1):
        print(num, end=" ")
        num=num-1
    print()