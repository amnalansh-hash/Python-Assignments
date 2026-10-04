string1 = "Hello "
name = input("Enter your Name: ")

string2 = string1 + name 
print(string2)

string3 = ", Welcome to python programming"
string2 = string2 + string3
print(string2)


text = string2

print(text[0])
print(text[-1])
print(text[:5])
print(text[-11:])
print(text[::-1])
print(text[-18:-12])


strM = "Python beginner tutorial"

print(strM.upper())
print(strM.lower())
print(strM.lower().capitalize())
print(strM.count('t'))
print(strM.replace("Python", "Machine Learning"))

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

t_combine = tuple1 + tuple2
print(t_combine)

print(t_combine * 3)

print(t_combine[2])

print(t_combine[:3])

print(t_combine[-3:])