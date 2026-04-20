from pathlib import Path
import string
import csv
from collections import Counter

student_id = "2025-0476"
student_name = "Albert Wayne O. Legaspi"

documents_path = Path.home() / "Documents" / "Activity_5_Files"

stopwords = {"the", "is", "and", "to", "a", "an", "of", "in", "it", "on",
             "at", "by", "for", "with", "this", "that", "was", "are", "be"}

stopwords_file = documents_path / "stopwords.txt"
if stopwords_file.exists():
    extra = stopwords_file.read_text(encoding="utf-8").split()
    stopwords.update(extra)

txt_files = list(documents_path.glob("*.txt"))

if not txt_files:
    print("No .txt files found!")
else:
    overall_counter = Counter()

    for file in txt_files:
        text = file.read_text(encoding="utf-8").lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()
        filtered = [w for w in words if w not in stopwords]
        file_counter = Counter(filtered)
        overall_counter += file_counter

        print(f"\nWord frequencies in {file.name}:")
        for word, count in file_counter.most_common(5):
            print(f"  {word}: {count}")

    print(f"\nOverall Most Frequent Meaningful Words:")
    for word, count in overall_counter.most_common(10):
        print(f"  {word}: {count}")

    export_path = documents_path / f"word_frequency_{student_id}.csv"
    with export_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Frequency"])
        writer.writerows(overall_counter.most_common())
    print(f"\nWord frequency data exported to: {export_path}")
    