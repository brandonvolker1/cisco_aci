reader = open('output.txt')

with open('output.txt') as reader:
    content = reader.readlines()

for line in content:
    print(line)

reader.close()
