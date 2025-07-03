#function that takes an integer input and returns the reversed number
n = int(input("Enter the intege: "))
reversed = 0
def REV_NEW(n):
    rev = 0
    while(n>0): 
            dig = n % 10
            rev = rev * 10 + dig
            n = n // 10
    return rev
print("the reversed number is: ",REV_NEW(n))
    

