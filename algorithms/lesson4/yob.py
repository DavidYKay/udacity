f = open('yob1995.txt', 'r')

names = []

for line in f:
  name, gender, count = line.split(",")
  if gender == 'F':
    names.append((name, gender, int(count)))
  # print line

names.sort(key=lambda t: t[2], reverse=True)
print names[0]
print names[1]
print names[-2]
print names[-1]

