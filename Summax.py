import sys, string, math

# Function to return max sum such that no two elements are adjacent
def find_max_sum(arr1):
    inc = 0
    exc = 0

    for i in arr1:
        # Current max excluding i == C ? : opr
        new_exc = exc if exc > inc else inc

        # Current max including i
        inc = exc + i
        exc = new_exc

        # return max of incl and excl
    return (exc if exc > inc else inc)


# Driver program to test above function
n = int(input())
L = [ int(x) for x in input().split()]
print(find_max_sum(L))
