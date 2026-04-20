#1 Create and Write to a File
from pathlib import Path

student_id = "2025-0476"
student_name = "Albert Wayne O. Legaspi"

documents_path = Path.home() / "Documents" / "Activity_5_Files"
documents_path.mkdir(parents=True, exist_ok=True)
file_path = documents_path / f"intro_{student_id}.txt"
file_path.write_text(f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!")
print(f"File created and text written at: {file_path}")

#2 Read File Content
content = file_path.read_text()
print(content)

#3 Append to a File
with file_path.open("a") as f:
    f.write("\nThis is a new line.")
print(f"Line appended to: {file_path}")

#4 - Write Multiple Lines
file_path = documents_path / f"lines_{student_id}.txt"
lines = ["Line 1", "Line 2", "Line 3"]
with file_path.open("w") as f:
    f.write("\n".join(lines))
print(f"Multiple lines written to: {file_path}")

#5 - Read File Line by Line
with file_path.open("r") as f:
    for line in f:
        print(line.strip())

#6 - Count Words in File
text = file_path.read_text()
word_count = len(text.split())
print(f"{student_name} (ID: {student_id}) - Word count in file '{file_path.name}': {word_count}")

#7 - Copy File
import shutil
src = documents_path / f"intro_{student_id}.txt"
dst = documents_path / f"intro_copy_{student_id}.txt"
shutil.copy(src, dst)
print(f"File copied successfully from {src.name} to {dst.name}.")

#8 - Rename File
old_file = documents_path / f"intro_copy_{student_id}.txt"
new_file = documents_path / f"intro_renamed_{student_id}.txt"
old_file.replace(new_file)
print(f"File renamed successfully from {old_file.name} to {new_file.name}.")

#9 - Delete File
file_path = documents_path / f"intro_renamed_{student_id}.txt"
if file_path.exists():
    file_path.unlink()
    print(f"File deleted successfully from: {file_path}")
else:
    print(f"No file found to delete at: {file_path}")

#10 - Create Directory
new_dir = documents_path / f"data_{student_id}"
new_dir.mkdir(parents=True, exist_ok=True)
print(f"Subdirectory created at: {new_dir}")

#11 - Write JSON File
import json
data_dir = documents_path / f"data_{student_id}"
data_dir.mkdir(parents=True, exist_ok=True)
data = {"name": student_name, "age": 21, "course": "Python Programming"}
file_path = data_dir / f"student_{student_id}.json"
with file_path.open("w") as f:
    json.dump(data, f, indent=4)
print(f"JSON file written at: {file_path}")

#12 - Read JSON File
import json
json_file = documents_path / f"data_{student_id}" / f"student_{student_id}.json"
with json_file.open("r") as f:
    data = json.load(f)
print(data)

#13 - Write CSV File
import csv
csv_file = documents_path / f"students_{student_id}.csv"
rows = [
    ["Name", "Student ID", "Score"],
    ["Eddie", "2025-1001", 90],
    ["Jeff", "2025-1002", 67],
    [student_name, student_id, 95]
]
with csv_file.open("w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
print(f"CSV file created at: {csv_file}")

#14 - Read CSV File
with csv_file.open("r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#15 - File Not Found Handling
missing_file = documents_path / f"missing_file_{student_id}.txt"
try:
    print(missing_file.read_text())
except FileNotFoundError:
    print(f"File not found for Student ID: {student_id}")

#16 - Count .txt Files
txt_files = list(documents_path.glob("*.txt"))
print(f"Student ID: {student_id}")
print(f"Found {len(txt_files)} .txt files in {documents_path}")
for file in txt_files:
    print(file.name)

#17 - File Metadata
import os
import time
file_path = documents_path / f"intro_{student_id}.txt"
if file_path.exists():
    stat = file_path.stat()
    print(f"Student ID: {student_id}")
    print(f"File: {file_path.name}")
    print(f"Size: {stat.st_size} bytes")
    print(f"Last Modified: {time.ctime(stat.st_mtime)}")
else:
    print(f"File {file_path.name} not found for Student ID: {student_id}")

#18 - Uppercase and Number Lines
file_path = documents_path / f"lines_{student_id}.txt"
if not file_path.exists():
    sample_lines = ["Line 1", "Line 2", "Line 3"]
    file_path.write_text("\n".join(sample_lines))
    print(f"Sample file created for Student ID: {student_id}")
lines = file_path.read_text().splitlines()
with file_path.open("w") as f:
    for i, line in enumerate(lines, 1):
        f.write(f"{i}: {line.upper()}\n")
print(f"Lines formatted and updated in file: {file_path}")

#19 - Reverse File Content
file_path = documents_path / f"lines_{student_id}.txt"
if not file_path.exists():
    sample_lines = ["Line 1", "Line 2", "Line 3"]
    file_path.write_text("\n".join(sample_lines))
    print(f"Sample file created for Student ID: {student_id}")
lines = file_path.read_text().splitlines()
lines.reverse()
with file_path.open("w") as f:
    f.write("\n".join(lines))
print(f"File lines reversed for Student ID: {student_id}")

#20 - Merge Two Files
f1 = documents_path / f"intro_{student_id}.txt"
f2 = documents_path / f"lines_{student_id}.txt"
merged = documents_path / f"merged_{student_id}.txt"
if not f1.exists():
    f1.write_text(f"Welcome {student_id} to File Handling in Python!")
    print(f"Sample intro file created for Student ID: {student_id}")
if not f2.exists():
    f2.write_text("Line 1\nLine 2\nLine 3")
    print(f"Sample lines file created for Student ID: {student_id}")
with merged.open("w") as mf:
    mf.write(f1.read_text())
    mf.write("\n")
    mf.write(f2.read_text())
print(f"Files merged successfully for Student ID: {student_id}")