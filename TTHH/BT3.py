f = open("Courses.txt")
content = f.read()
numd = 0
print(content, "\br")
with open("Courses.txt") as f:
  for x in f :
    numd = numd + 1
    a = "".join(x.split())
    print(numd,a)
f.close()