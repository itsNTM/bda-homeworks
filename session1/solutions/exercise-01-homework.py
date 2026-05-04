#1. Load the dataset with csv.reader
import csv # imports Python’s built-in CSV module

file_path = "session1/movies.csv" # stores the location of the file

with open(file_path, "r", newline="", encoding="utf-8") as file:  # opens the CSV file
    reader = csv.reader(file) # creates a CSV reader object that reads the file

#2. Print: the number of data rows (excluding header) and the number of columns
    header = next(reader)  # extract header first
    
    col_count= len(header)

    row_count = 0
    for row in reader:
        row_count += 1

    print("The number of data rows:", row_count)
    print("The number of columns:", col_count)

#3. Print the first 3 rows (including header).
with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    header = next(reader)
    print("\nHeader:", header)

    print("Row 1:", next(reader))
    print("Row 2:", next(reader))
    print("Row 3:", next(reader))

#4. Find and print the first movie where the genres column contains Action.
with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    expected_columns = len(header)
    genre_index = header.index("genres")

    for i, row in enumerate(reader):
        if len(row) != expected_columns:
            print(f"Issue at row {i}: {row}")
            continue
        if "Action" in row[genre_index]:
            print("\nFirst Action movie at row", i)
            print(row)
            break
    
#5. Compute and print the average of rating_imdb (ignore missing or invalid values).
with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    expected_columns = len(header)
    rating_index = header.index("rating_imdb")

    total = 0
    count = 0
    
    for i, row in enumerate(reader):
        if len(row) != expected_columns:
            print(f"Issue at row {i}: {row}")
            continue
        try:
            value = row[rating_index]
            if value != "":
                total += float(value)
                count += 1
        except:
            print(f"Bad data at row {i}")
    
    avg_rating = total / count
    print("\nAverage IMDb rating:", avg_rating)

#6. Compute and print the average of one more numeric column (for example runtime_min or metascore, ignoring missing values).
with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    expected_columns = len(header)
    runtime_index = header.index("runtime_min")

    total_runtime = 0
    count_runtime = 0

    for i, row in enumerate(reader):
        if len(row) != expected_columns:
            print(f"Issue at row {i}: {row}")
            continue
        try:
            value = row[runtime_index]
            if value != "":
                total_runtime += float(value)
                count_runtime += 1
        except:
            print(f"Bad data at row {i}")

avg_runtime = total_runtime / count_runtime
print("\nAverage runtime:", avg_runtime)

#7. Count how many movies have rating_imdb >= 8.0.
with open(file_path, newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    expected_columns = len(header)
    rating_index = header.index("rating_imdb")
    high_rating_count = 0

    for i, row in enumerate(reader):
        if len(row) != expected_columns:
            print(f"Issue at row {i}: {row}")
            continue
        try:
            value = row[rating_index]
            if value != "" and float(value) >= 8.0:
                high_rating_count += 1
        except:
            print(f"Bad data at row {i}")

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
