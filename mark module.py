marks = {}

def add_marks(name, score):
    marks[name] = score

def calculate_average():
    total = sum(marks.values())
    return total / len(marks)

def find_topper():
    topper = max(marks, key=marks.get)
    return topper, marks[topper]

add_marks("Arun", 85)
add_marks("Maya", 92)
add_marks("Rahul", 78)

print("Average:", calculate_average())

topper = find_topper()
print("Topper:", topper[0], topper[1])