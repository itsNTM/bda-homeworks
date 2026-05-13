import os

from google import genai


MODEL_NAME = "gemini-2.5-flash"
TEXT_FILE = "les_miserables.txt"
CHUNK_SIZE = 30
MAX_CHUNKS = 3


def ask_gemini(prompt):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return response.text


def book_chunks(path, chunk_size=30, max_chunks=3):
    chunk = []
    chunks_sent = 0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            chunk.append(line)

            if len(chunk) == chunk_size:
                yield "\n".join(chunk)
                chunks_sent += 1
                chunk = []

                if chunks_sent == max_chunks:
                    return

    if chunk and chunks_sent < max_chunks:
        yield "\n".join(chunk)


def build_summary_prompt(chunk_text, chunk_number):
    return f"""You are summarizing one chunk from Les Misérables.

Return only valid JSON with these keys:
- chunk: the chunk number
- characters: important character names mentioned
- events: short event descriptions
- summary: a 2-3 sentence summary
- uncertainty: anything unclear

Rules:
- Do not include Markdown fences.
- Do not add commentary outside the JSON.
- If there are no clear events, use an empty list.

Chunk number: {chunk_number}

Excerpt:
{chunk_text}
"""


for chunk_number, chunk_text in enumerate(
    book_chunks(TEXT_FILE, chunk_size=CHUNK_SIZE, max_chunks=MAX_CHUNKS),
    start=1,
):
    prompt = build_summary_prompt(chunk_text, chunk_number)
    summary = ask_gemini(prompt)
    print(f"Chunk {chunk_number}")
    print(summary)
    print()
