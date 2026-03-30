import sys
from tools.file_reader import read_file
from utils.chunking import chunk_text
from llm import ask_llm

# ---------------- MCP Tool Selection ----------------
def choose_tool_mcp(file_name):
    prompt = f"""
You are an intelligent assistant. Decide which tool should be used to read the following file:

File name: {file_name}

Options:
- pdf_reader        : PDF with extractable text
- image_pdf_reader  : PDF that requires OCR
- image_reader      : Image file (jpg, png, etc.)
- text_reader       : Plain text file

Return only the tool name.
"""
    tool = ask_llm(prompt).strip()
    return tool

# ---------------- Summarization ----------------
def summarize(text):
    prompt = f"""
You are a helpful assistant.

Combine and refine the content below into a structured summary:

1. Key Points (bullet points)
2. Short Summary (5–6 lines)
3. Main Theme (1 line that captures the essence)

Content:
{text}
"""
    return ask_llm(prompt)

# ---------------- Final Recursive Summary ----------------
def final_summary(all_chunk_summaries):
    combined_text = "\n".join(all_chunk_summaries)
    prompt = f"""
You are a helpful assistant.

Combine the following summaries into a single coherent summary with:

1. Key Points (bullet points)
2. Short Summary (5–6 lines)
3. Main Theme (1 line)

Content:
{combined_text}
"""
    return ask_llm(prompt)

# ---------------- Main ----------------
def main(file_path):
    # MCP chooses the tool
    tool = choose_tool_mcp(file_path)

    try:
        text = read_file(file_path, tool)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Chunking
    chunks = chunk_text(text)

    # Summarize each chunk
    chunk_summaries = []
    for idx, chunk in enumerate(chunks, 1):
        print(f"Summarizing chunk {idx}/{len(chunks)}...")
        chunk_summaries.append(summarize(chunk))

    # Final recursive summary
    print("\n=== FINAL SUMMARY ===\n")
    final = final_summary(chunk_summaries)
    print(final)

# ---------------- Entry Point ----------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <file>")
    else:
        main(sys.argv[1])