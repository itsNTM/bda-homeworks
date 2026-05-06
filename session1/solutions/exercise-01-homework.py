#1. Load the dataset with csv.reader
import csv # imports Python’s built-in CSV module
import os

# stores the location of the file
file_path = os.path.join(os.path.dirname(__file__), "../movies.csv")

with open(file_path, "r", encoding="utf-8") as file: # opens the CSV file
    data = list(csv.reader(file))

header = data[0]
rows = data[1:]

#2. Print: the number of data rows (excluding header) and the number of columns
print("\nThe number of data rows without header:", len(rows))
print("\nThe number of columns:", len(header))

#3. Print the first 3 rows (including header).
print("\n---First 3 rows with header----")
print("Header:", header)
print("Row 1:", rows[0])
print("Row 2:", rows[1])
print("Row 3:", rows[2])

#4. Find and print the first movie where the genres column contains Action.
expected_columns = len(header)
genre_index = header.index("genres")

for i, row in enumerate(rows, start=1):
    if len(row) != expected_columns:
        continue
    if "Action" in row[genre_index]:
        print("\nFirst Action movie at row", i)
        print(row)
        break

#5. Compute and print the average of rating_imdb (ignore missing or invalid values).
rating_index = header.index("rating_imdb")

total = 0
count = 0
    
for i, row in enumerate(rows, start=1):
    if len(row) != expected_columns:
        continue
    try:
        value = row[rating_index]
        if value:
            total += float(value)
            count += 1
    except ValueError:
        continue
    
avg_rating = total / count if count > 0 else 0
print("\nAverage IMDb rating:", avg_rating)

#6. Compute and print the average of one more numeric column (for example runtime_min or metascore, ignoring missing values).
runtime_index = header.index("runtime_min")

total_runtime = 0
count_runtime = 0

for i, row in enumerate(rows, start=1):
    if len(row) != expected_columns:
        continue
    try:
        value = row[runtime_index]
        if value:
            total_runtime += float(value)
            count_runtime += 1
    except ValueError:
        continue

avg_runtime = total_runtime / count_runtime if count_runtime > 0 else 0
print("\nAverage runtime:", avg_runtime)

#7. Count how many movies have rating_imdb >= 8.0.
high_rating_count = 0

for i, row in enumerate(rows, start=1):
    if len(row) != expected_columns:
        continue
    try:
        value = row[rating_index]
        if value and float(value) >= 8.0:
            high_rating_count += 1
    except ValueError:
        continue

print("\nMovies with rating >= 8.0:", high_rating_count)

#8. Report the time and space complexity for: 
print("\nTime and Complexity Analysis")
print("""
First-match search (Task 4-Action movie):
- Time Complexity: O(n)
- Space Complexity: O(1)

Average computation (Tasks 5- rating_imdb & Task 6-runtime):
- Time Complexity: O(n)
- Space Complexity: O(1)
""")
