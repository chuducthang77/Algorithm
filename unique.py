#Given the sorted array, returns the number of unique elemnts in array
#Runtime: O(n) 

def unique(A):
    #input: A - sorted array
    #output: count - number of unique elements

    count = 0
    current = 0
    for number in A:
        if number != current:
            count+=1
            current = number
    return count 

def main():
    test1 = [1]
    test2 = [2,2,2]
    test3 = [1,2,3,4,4,5]
    print(unique(test1))
    print(unique(test2))
    print(unique(test3))

main()
