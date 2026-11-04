import time

f = open("Courses.txt")
content = f.read() 
print(content)

with open("Courses.txt", "a") as f:
  f.write("Lap trinh")
  
time.sleep(2)  
f = open("Courses.txt")
contentre = f.read()
print(contentre)