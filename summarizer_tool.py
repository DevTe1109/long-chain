# summarizer_tool.py

from transformers import pipeline
import os

def load_article():
    print("Choose input method:")
    print("1. Paste article text manually")
    print("2. Load article from a .txt file")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        print("\nPaste your article below. Press ENTER twice to end input.\n")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        return "\n".join(lines)

    elif choice == '2':
        file_path = input("Enter full path to the .txt file: ").strip()
        if not os.path.isfile(file_path):
            print("❌ File not found.")
            return None
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    else:
        print("❌ Invalid choice.")
        return None

def summarize(text, min_length=60, max_length=200):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, min_length=min_length, max_length=max_length, do_sample=False)
    return summary[0]['summary_text']

def main():
    print("\n🧠 Article Summarization Tool Using NLP\n")
    article = load_article()

    if article:
        print("\n🔍 Generating summary...\n")
        try:
            summary = summarize(article)
            print("✅ Summary:\n")
            print(summary)
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print("⚠️ No article provided.")

if __name__ == "__main__":
    main()
