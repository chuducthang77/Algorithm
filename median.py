#Given 2 sorted array, each contains n elements. Find the median of list of 2n elements
#Runtime: O(logn)

def median(A, B, sA, eA, sB, eB):
    if len(A) == 1 or len(B) == 1:
        if A[sA] <= B[sB]:
            return A[sA]
        else:
            return B[sB]
    else:
        midA = int((sA + eA)/2)
        midB = int((sB + eB)/2)
        if A[midA] == B[midB]:
            return A[midB]
        elif A[midA] > B[midB]:
            median(A, B, midA + 1, eA, sB, midB)
        else: 
            median(A, B, sA, midA, midB + 1, eB)

def main():
    A = [2,5,6,8,12]
    B = [4,5,7,10,18]
    print(median(A, B, 0, 4, 0, 4))

main()