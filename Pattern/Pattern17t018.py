"""# Pattern no 13. Star Diamond:
        *           
      *   *         
    *   *   *       
  *   *   *   *     
*   *   *   *   *   
  *   *   *   *     
    *   *   *       
      *   *         
        *           

"""



n=int(input("Enter the Size of Star Diamond: "))

print("Pattern Number 13:")
#Upper part
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print(" ", end=" ")

    for j in range(1, i+1):
        print("*"," ", end=" ")
    print()

#lower part
for i in range(n-1,0,-1):
    for j in range(1, n+1-i):
        print(" ", end=" ")

    for j in range(1, i+1):
        print("*"," ", end=" ")
    print()



"""# Pattern no 14. Hollow Star Diamond:
        *
      *   *   
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *
"""
print()
print("Pattern Number 14:")
#Upper part
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        if(j==1 or j==i or i==1):
            print("*"," ", end=" ")
        else:
             print(" "," ", end=" ")

    print()

#Lower Part
for i in range(n-1,0,-1):
    for j in range(1, n+1-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        if(j==1 or j==i or i==1):
            print("*"," ", end=" ")
        else:
             print(" "," ", end=" ")

    print()