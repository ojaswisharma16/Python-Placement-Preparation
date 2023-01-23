"""# Pattern no 07. Star triangles:
* 
* * 
* * * 
* * * * 
* * * * * 

"""



n=int(input("Enter the Size of Star Triangle: "))

print("Pattern Number 07:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

"""# Pattern no 08. Hollow Star triangles:
* 
* * 
*   * 
*     *
* * * * *
"""
print()
print("Pattern Number 08:")
for i in range(1, n+1):
    for j in range(1, i+1):
        if(j==1 or j==i or i==1 or i==n):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

"""# Pattern no 09. Inverted Hollow Star triangles:
* * * * *
*     *
*   *
* *
* 
"""
print()
print("Pattern Number 09:")
for i in range(n, 0,-1):
    for j in range(1, i+1):
        if(j==1 or j==i or i==1 or i==n):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


