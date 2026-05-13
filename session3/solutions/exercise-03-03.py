import os

from google import genai

TEXT_FILE = "les_miserables.txt"

#Updated question and keywords
QUESTION = "Who is Fantine?"
KEYWORDS = ["fantine"]
MAX_LINES = 14 # increased context


def useful_lines(path):
    """Yield non-empty lines from a text file."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line != "":
                yield line


def retrieve_context(path, keywords, max_lines):
    """Find a small chunk of text that matches the question."""
    matches = []
    extra_lines = 0

    for line in useful_lines(path):
        line_lower = line.lower()

        if any(keyword in line_lower for keyword in keywords):
            matches.append(line)
            # Keep two lines after a match so Gemini has a little context.
            extra_lines = 2
        elif extra_lines > 0:
            matches.append(line)
            extra_lines -= 1

        if len(matches) >= max_lines:
            break

    return "\n".join(matches)


context = retrieve_context(TEXT_FILE, KEYWORDS, MAX_LINES)

# Send only the retrieved context to Gemini.
prompt = f"""Use only this context to answer the question.

Question:
{QUESTION}

Context:
{context}
"""

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print(response.text)
