students = {
    'ram': 'mumbai',
    'shyam': 'delhi',
    'naresh': 'chennai',
}
print(students["ram"])
print(students["shyam"])
print(students["naresh"])

# using for loop

print('using for loop')

for i in students:
    print(i, students[i], sep=",")