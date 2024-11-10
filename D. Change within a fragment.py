line = input()
first = line.find('h')
last = line.rfind('h')
print(line[:first + 1] + line[first + 1:last].replace('h', 'H') + line[last:])