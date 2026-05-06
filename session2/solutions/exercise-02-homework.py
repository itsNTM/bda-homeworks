import csv
import json
import os
from time import sleep
from urllib.error import HTTPError
from urllib.request import Request, urlopen

# Gemini helper function
def ask_gemini(prompt, model_name="gemini-2.5-flash"):
     # Read your API key from the environment.
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")
    
    # Build the remote Gemini endpoint URL.
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model_name}:generateContent"
    )

    # Prepare the request body with your prompt.
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    # Create an HTTP POST request with JSON payload and API key.
    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )

    # Send request, parse JSON response, and return only model text.
    # If quota/rate limit is reached, show a student-friendly message.
    try:
        with urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as err:
        if err.code == 429:
            raise RuntimeError("Gemini rate/limit reached. Please wait a minute and try again.") from err
        raise

    return data["candidates"][0]["content"]["parts"][0]["text"].strip()

# File paths
INPUT_FILE = "studio_ghibli_movies.csv"
OUTPUT_FILE = "studio_ghibli_movies_ai_clean.csv"

rows = []
filled_year = 0
filled_musicby = 0

# Load CSV using csv.DictReader
with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    for row in reader:
        rows.append(row)
    print("Loaded records:", len(rows))

    print("\n----Fiiling rows with missing values----")
    # 3. Fill missing values
    for i, row in enumerate(rows, start=1):
        title = row.get("title", "").strip()
        year = row.get("year", "").strip()
        music_by = row.get("music_by", "").strip()
           
        # missing year
        if not year:
            print(f"Row {i} ({title}) missing year")
            prompt = f"""
            Return only the 4-digit release year for the Studio Ghibli movie "{title}".
            Output format: only 4 digits, no extra text.
            """
            try:
                year_api = ask_gemini(prompt)
                row["year"] = year_api
                filled_year += 1
                print(f"Filled year for {title} → {year_api}")
                sleep(1)
            except Exception as e:
                print(f"Row {i}: Error filling year for {title}: {e}")

        # missing music_by
        if not music_by:
            print(f"Row {i} ({title}) missing music_by")
            prompt = f"""
                Return only the composer full name for the Studio Ghibli movie "{title}".
                Output format: name only, no extra text.
                """
            try:
                music_api = ask_gemini(prompt)
                row["music_by"] = music_api
                filled_musicby += 1
                print(f"Filled music_by for {title}: {music_api}")
                sleep(1)  # avoid API rate limits
            except Exception as e:
                print(f"Error filling music_by for {title}: {e}")

# Save cleaned CSV
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
print(f"\nSaved output file: {OUTPUT_FILE}")

# Print Summary
print("\n--- Final Summary ---")

# how many values were filled
print("AI filled values:", filled_year + filled_musicby)

# check remaining missing values
missing_rows = 0
missing_year = 0
missing_musicby = 0

for i, row in enumerate(rows, start=1):
    year_missing = not row.get("year", "").strip()
    music_missing = not row.get("music_by", "").strip()
    if year_missing:
        missing_year += 1
    if music_missing:
        missing_musicby += 1
    if year_missing or music_missing:
       missing_rows += 1
       print(f"Row {i} ({row['title']}) still has missing values")
print(f"""
Total number of rows still missing values: {missing_rows}
Still missing year: {missing_year}
Still missing music_by: {missing_musicby}
""")

