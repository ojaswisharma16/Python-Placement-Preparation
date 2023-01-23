"""# Pattern no 01. Number triangles:
1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""



n=int(input("Enter the Size of Number Triangle: "))

print("Pattern Number 01 :")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

"""# Pattern no 02. Number triangles:
1         
2 2       
3 3 3     
4 4 4 4   
5 5 5 5 5 
"""
print()
print("Pattern Number 02 :")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

"""# Pattern no 03. Number triangles:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15 
"""
print()
print("Pattern Number 03 :")
num=1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num=num+1
    print()