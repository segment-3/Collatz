# Andrew Rochford
# AIST 2120

#-----------------------------------------------------------------------

print()
print('--------------------------------'.center(60))
print('---        AIST 2120         ---'.center(60))
print('---    Not Totally Random    ---'.center(60))
print('--------------------------------'.center(60))
print()

#-----------------------------------------------------------------------

def collatz(n):
    if n == 1:
        print(n)
        print("You've been collatzed!")
        return
    elif n % 2 == 0:            
        print(n)
        collatz(n // 2)
    else:
        print(n)
        collatz(3 * n + 1)

n = int(input("Enter a positive integer and I'll collatz it: "))
collatz(n)
#-----------------------------------------------------------------------

print()
print('--------------------------------'.center(60))
print('-------------  End -------------'.center(60))
print('--------------------------------'.center(60))

#-----------------------------------------------------------------------
