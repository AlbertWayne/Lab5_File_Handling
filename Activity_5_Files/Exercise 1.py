from pathlib import Path
import csv

student_id = "2025-0476"
student_name = "Albert Wayne O. Legaspi"

# Define folder
documents_path = Path.home() / "Documents" / "Activity_5_Files"

# Get all .txt files
txt_files = list(documents_path.glob("*.txt"))

if not txt_files:
    print("No .txt files found in the folder!")
else:
    results = []

    for file in txt_files:
        text = file.read_text(encoding="utf-8")
        lines = [line for line in text.splitlines() if line.strip()]  # ignore empty lines
        words = text.split()
        characters = len(text.replace(" ", "").replace("\n", ""))

        total_lines = len(lines)
        total_words = len(words)
        total_chars = characters
        words_per_line = round(total_words / total_lines, 2) if total_lines > 0 else 0
        chars_per_word = round(total_chars / total_words, 2) if total_words > 0 else 0

        results.append({
            "Filename": file.name,
            "Lines": total_lines,
            "Words": total_words,
            "Characters": total_chars,
            "Words/Line": words_per_line,
            "Chars/Word": chars_per_word
        })

    # Sort by word density (Words/Line) highest to lowest
    results.sort(key=lambda x: x["Words/Line"], reverse=True)

    # Display table
    print(f"\n{'Filename':<35} {'Lines':>6} {'Words':>6} {'Characters':>12} {'Words/Line':>11} {'Chars/Word':>11}")
    print("-" * 85)
    for r in results:
        print(f"{r['Filename']:<35} {r['Lines']:>6} {r['Words']:>6} {r['Characters']:>12} {r['Words/Line']:>11} {r['Chars/Word']:>11}")

    # Most and least content-dense
    print(f"\nMost content-dense file: {results[0]['Filename']}")
    print(f"Least content-dense file: {results[-1]['Filename']}")

    # Optional: export to CSV
    summary_path = documents_path / "content_summary.csv"
    with summary_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Filename", "Lines", "Words", "Characters", "Words/Line", "Chars/Word"])
        writer.writeheader()
        writer.writerows(results)
    print(f"\nSummary exported to: {summary_path}")
    