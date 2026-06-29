# Let 5 integers are ( 32, 45, 90, 45, 6) then output "DUPLICATE" to be printes.
# Find Duplicate

numbers = input("Enter any 5 integers").split()
s1 = set(numbers)
for i in s1:
    c=numbers.count(i)
    if c>1:
        print("DUPLICATE"+i)
    else:
        print("NO DUPLICATE"+i)