numbers = [1, 2, 3] #creates a list

for number in numbers:
    print(number)

numbers = [1, 2, 3]
it = iter(numbers) #converts list into iterator

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

# next(it) returns the current element and moves an internal pointer forward by 1
# So, Time complexity: O(1)
# Space complexity: O(1)

with open("les_miserables.txt", "r", encoding="utf-8") as file:
    it = iter(file)
    print(next(it))
    print(next(it))

# Time complexity: O(m) per line, where m is the length of the line being read.
# Space complexity: O(m), because only one line is held at a time.

#Task 1
TEXT_FILE = "les_miserables.txt"

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    first = next(file)
    print(first)

#Time: O(m), where m is the length of the first line.

#Space: O(m).

TEXT_FILE = "les_miserables.txt"
target = "Jean Valjean"
found = None

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        if target in line:
            found = line
            break

print(found)

TEXT_FILE = "les_miserables.txt"
count = 0

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        count += 1

print(count)

TEXT_FILE = "les_miserables.txt"
total_length = 0
count = 0

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        total_length += len(line)
        count += 1

average = total_length / count
print(average)

#Generators with yield
TEXT_FILE = "les_miserables.txt"

with open(TEXT_FILE, "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines[100])

#Count non-empty lines containing a word
TEXT_FILE = "les_miserables.txt"
target = "Jean"

def non_empty_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line

count = 0

for line in non_empty_lines(TEXT_FILE):
    if target in line:
        count += 1

print(count)