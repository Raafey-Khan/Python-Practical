# Accept n elements from the user and arrange them in ascending order
n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
arr.sort()
print(f"Elements in ascending order: {arr}")
