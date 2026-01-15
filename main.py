print("Hi greg's students in Internship Ready")
print(len("fiu"))
print(type("fiu"))
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)

professors = ["greg", "kianoosh", "richard", "patricia", "debra"]
print(professors[0])
print(professors[-1])
professors.append("leo")
print(professors)
professors.extend(["heather", "kevin", "jason"])
print(professors)
professors.insert(2, "trevor")
print(professors)
professors[3] = "mark"
print(professors)
print(professors[3:5])
print(professors[5:])
professors.remove("kianoosh")
print(professors.index("mark"))
x= professors.pop()