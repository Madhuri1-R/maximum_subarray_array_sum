def maximum_subarray_sum(arr):
    current_sum = arr[0]
    maximum_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(arr[i],current_sum+arr[i])
        maximum_sum = max(current_sum,maximum_sum)
    return maximum_sum
nn = int(input("Enter the number of elements:"))
arr = []
for i in range(n):
    num = int(input("Enter element value:"))
    arr.append(num)
result = maximum_subarray_sum(arr)  
print("Maximum subarray sum is:",result)
    