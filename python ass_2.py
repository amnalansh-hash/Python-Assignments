# 1. List Creation
age_list = [24, 25, 26, 27, 28]
name_list = ["Zara", "Nehlom", "Arun", "Meera", "Kiran"]

print(age_list)
print(name_list)

# 2.List Operations
name_list.append("Yazhini")
print("After append:", name_list)

age_list.insert(2, 30)
print("After insert:", age_list)

name_list.remove("Yazhini")
print("After remove:", name_list)

age_list.pop()
print("After pop:", age_list)

age_list.extend([29, 30, 26])
print("After extend:", age_list)

age_list.sort(reverse=True)
print("After sort:", age_list)

print("Max age:", max(age_list))
print("Min age:", min(age_list))
print("Sum of ages:", sum(age_list))

# 3. Accessing List Elements
print(name_list[0])
print(name_list[-1])
print(name_list[2:5])
print(name_list[::-1])


# Dictionary
student_marks = {"Zara": 85, "Nehlom": 92, "Arun": 78, "Meera": 88, "Kiran": 70}
print(student_marks)

# b. Access the mark of a specific student
print(student_marks["Nehlom"])

# c. Add a new student Janani with 80
student_marks["Janani"] = 80
print(student_marks)

# d. Update the mark of an older student to 82
student_marks["Arun"] = 82
print(student_marks)

# e. keys(), values(), items()
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())

# Sets
# a. Create my_set (duplicates are removed automatically)
my_set = set(['a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'])
print(my_set)

# b. Try to change the value at index 4
try:
    my_set[4] = 'o'
except TypeError as error:
    print("Error:", error)

# c. Create two sets
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

# d. Union and intersection
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

# Performance Category Program
score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a number between 0 and 10.")
elif score > 7:
    print("Above Average: Excellent work! Keep it up.")
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve your performance, consistent practice will lead to better results.")
