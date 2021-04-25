#Given the number, count the number of occurrence in the list
# Run time: O(logn)
 
def occurrence(A, x):
    left = -1
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = int((start + end)/2)
        if A[mid] >= x:
            end = mid - 1 
        else:
            start = mid + 1

    left = start

    right = -1
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = int((start + end)/2)
        if A[mid] > x: 
            end = mid - 1
        else:
            start = mid + 1
    right = end

    return right - left + 1
def main():
    A = [1,1,2,3,4]
    x = -1
    print(occurrence(A, x))
    
main()