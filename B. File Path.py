parts = []

while True:
    line = input()
    parts.append(line)
    if '.txt' in line:
        break

back_slash = '\\'
if len(parts) == 1:
    print(parts[0])
else:
    print(f"Unix path: /{'/'.join(parts)}")
    print(f"Windows path: C:\\{back_slash.join(parts)}")
