file = open("students.txt", "w")
file.write("Arya,101,85\n")
file.write("Rahul,102,90\n")
file.close()

print("Data saved successfully")
file = open("students.txt", "r")
data = file.read()
print("\nFile Data:")
print(data)
file.close()

file = open("students.txt", "a")
file.write("Anu,103,88\n")
file.close()

print("New record appended")

file = open("students.txt", "r")
print("\nUpdated File Data:")
print(file.read())
file.close()