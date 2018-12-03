# Test

arr = [6, 5, 1, 8, 7, 2, 4, 3]
subArr1 = sorted([arr[i] for i in range(len(arr) // 2)])
subArr2 = sorted([arr[j] for j in range(len(arr) // 2, len(arr))])
print(subArr1)
print(subArr2)