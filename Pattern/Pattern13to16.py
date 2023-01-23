"""# Pattern no 13. Star Pyramid:
       *           
      *   *         
    *   *   *       
  *   *   *   *     
*   *   *   *   *   

"""



n=int(input("Enter the Size of Star Pyramid: "))

print("Pattern Number 13:")
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print(" ", end=" ")

    for j in range(1, i+1):
        print("*"," ", end=" ")
    print()

"""# Pattern no 14. Hollow Star Pyramid:
        *           
      *   *         
    *       *       
  *           *
*   *   *   *   *
"""
print()
print("Pattern Number 14:")
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        if(j==1 or j==i or i==1 or i==n):
            print("*"," ", end=" ")
        else:
             print(" "," ", end=" ")

    print()

"""# Pattern no 15.  Inverted Star Pyramid:
*   *   *   *   *
  *           *   
    *       *
      *   *
        *
"""
print()
print("Pattern Number 15:")
for i in range(n, 0,-1):
    for j in range(1, n+1-i):
        print(" ", end=" ")

    for j in range(1, i+1):
        if(j==1 or j==i or i==1 or i==n):
            print("*"," ", end=" ")
        else:
            print(" "," ", end=" ")

    print()

"""# Pattern no 16. Inverted Hollow Star Pyramid:
*   *   *   *   *
  *   *   *   *
    *   *   *
      *   *
        *

"""

print("Pattern Number 16:")
for i in range(n,0,-1):
    for j in range(1, n+1-i):
        print(" ", end=" ")

    for j in range(1, i+1):
        print("*"," ", end=" ")
    print()

