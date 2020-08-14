'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    count = 0
    temp = []
    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])
        else:
            count += 1
        
    for j in range(count):
        temp.append(0)
    
    return temp


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")