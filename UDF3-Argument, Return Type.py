# Argument, Return Type

# program 1
def sum(n1, n2): 
    ans = n1+n2 
    return ans 
a1 = sum(10, 20) 
print("Sum is ", a1)


# program 2 (sum avg)
def dosum(a,b,c):
    d = a + b + c
    return d
def calculateAvg(total):
    per = total/300*100
    return per

totalmarks = dosum(85,65,74)
print("Total is ",totalmarks)

getper = calculateAvg(totalmarks)
print("% is",getper)