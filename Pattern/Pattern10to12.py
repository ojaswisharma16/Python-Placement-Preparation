"""# Pattern no 10. Right Star triangles:
        *         
      * *         
    * * *         
  * * * *         
* * * * * 

"""



n=int(input("Enter the Size of Right Star Triangle: "))

print("Pattern Number 10:")
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print(" ", end=" ")

    for j in range(1, i+1):
        print("*", end=" ")
    print()

"""# Pattern no 11. Right Hollow Star triangles:
        *         
      * *         
    *   *         
  *     *
* * * * *
"""
print()
print("Pattern Number 11:")
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        if(j==1 or j==i or i==1 or i==n):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

"""# Pattern no 12. Right Inverted Hollow Star triangles:
* * * * *
  *     *
    *   *
      * *
        *
"""
print()
print("Pattern Number 12:")
for i in range(n, 0,-1):
    for j in range(1, n+1-i):
        print(" ", end=" ")

    for j in range(1, i+1):
        if(j==1 or j==i or i==1 or i==n):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


