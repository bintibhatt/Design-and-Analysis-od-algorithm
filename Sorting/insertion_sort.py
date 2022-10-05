def insertionsort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i-1
        while(key < A[j] and j >= 0):
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key


# address of the first element will be passed in 'A'
arr = [1, 4, 6, 0, 2, 69, 3, 2, 7, 9, 4, 2]  # declaration
insertionsort(arr)
print(arr)

# Complexity of this sorting
# loop-2 for each value of 'i' in 'while' loop will be executing
# best case - already sorted
# Omega(n) - best case complexity___________________(n)*(1) 'while' executed 1 time
# worst case - descending order
# O(n^2) - worst case complexity____________________(n)*(n) 'while' executed n times
# for for --- addition
# for(for) --- multiplication
# space complexity - extra variables - i,j,key,  arr is input so it doesnt count
# O(1) - space complexity - called as inspace sorting algorithm(in-place)
