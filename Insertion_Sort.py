# Insertion Sort
# No Temporary array/list used. Swapping ocurrs within the original array/list 
def Insertion_Sort(arr):
    # Initializing start value with 1. In this Insertion sort, Unsorted Array index starts with 1
    # Start value indicates the starting index of unsorted array
    start = 1
    
    # This for loop is to loop the unsorted array till the end
    for i in range(start, len(arr)):
        # For every value in unsorted array is compared with the sorted array to fix the position 
        # And the current checking value in unsorted array is stored in the variable 'val' 
        val = arr[i]
        
        # Each unsorted array value is compared with sorted array in reverse order starts form i - 1 th position till 0th position
        for j in range(start - 1, -1, -1):
            
            # If value in sorted array not greater than i'th value(val) means that there is no need to change in the sorted array. Then the loop will break
            if arr[j] <= val:
                break

            # If greater the value will be jumped to the next index to fix the position 
            if j >= 0 and arr[j] > val:
                arr[j + 1] = arr[j]
                # After jumping the value from their position we have to clear the value from their original position to avoid incorrect output
                arr[j] = None
            else:
                break

        # At the end of one check there is possible that 'None' at j'th position or j + 1'th position
        # Scenario of 'None' at j'th position only occurs when the comparing value comes at the 1st element of the array
        # Rest of the scenarios j + 1 th position have 'None', 'val' is assigned for that position 
        if arr[j + 1] == None:
            arr[j + 1] = val
        if arr[j] == None:
            arr[j] = val

        # Increment start value by 1 to move forward one by one value
        start += 1

    # * before variable 'arr' used to pint the list elements without bracket and commas 
    print(*arr)
    

if __name__ == "__main__":
    # Get integer input form the user in a single line seperated with spaces
    # Store the integer in a list 
    arr = list(map(int, input().split()))

    # Call the function 'Insertion_Sort' and pass the argument 'arr' list
    Insertion_Sort(arr)