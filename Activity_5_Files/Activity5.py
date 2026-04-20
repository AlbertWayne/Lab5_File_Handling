# ============================================================
#1 — Writing to a File
from pathlib import Path

output_dir = Path.home() / "Documents" / "Legaspi_Activity_5"
output_dir.mkdir(exist_ok=True)
file_path = output_dir / "Act5_example.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, Welcome to Python Programming!\n")
    file.write("File saved safely with pathlib.\n")
    file.write("Python makes file handling easy!")

print(f"File saved to: {file_path.resolve()}")

# ============================================================
# PROCEDURE 2 — Reading from a File
if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("File content:\n", content)

with open(file_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        if "Python" in line:
            print(f"Line {line_number}: {line.strip()}")

# ============================================================
# PROCEDURE 3 — Appending Data
with open(file_path, "a", encoding="utf-8") as file:
    file.write("\nThis line was added!")
print("Data appended successfully.")

user_text = input("Type information you want to append: ") #TRY IT:
with open(file_path, "a", encoding="utf-8") as file:
    file.write("\n" + user_text)
print("Additional data appended successfully.")


# ============================================================
# PROCEDURE 4 — Safe File Operations with Backup

from datetime import datetime
import shutil

backup_dir = Path.home() / "Documents" / "Legaspi_Activity_5"

def write_with_backup(filename: str, content: str):
    fp = backup_dir / filename
    if fp.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = fp.with_name(
            f"{fp.stem}_Legaspi_backup_{timestamp}{fp.suffix}"
        )
        shutil.copy2(fp, backup_path)
        print(f"Backup saved: {backup_path.name}")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"File saved: {fp.name}")

def read_file(filename: str):
    fp = backup_dir / filename
    with open(fp, "r", encoding="utf-8") as f:
        return f.read()

print("\n=== File Operations Demo ===")
print("\n1. Creating new file:")
write_with_backup("demo.txt", "Initial content")
print("\n2. Updating file (triggers backup):")
write_with_backup("demo.txt", "Updated content")
print("\n3. Reading file:")
print(read_file("demo.txt"))
print("\n4. Listing backups:")
for backup in backup_dir.glob("*backup*"):
    print("-", backup.name)

# ============================================================
# PROCEDURE 5 — Menu-Driven File Manager
def file_manager():
    file_name = input("\nEnter filename (e.g., notes.txt): ")
    fp = backup_dir / file_name

    while True:
        print("\n--- MENU ---")
        print("1. Write to file")
        print("2. Append to file")
        print("3. Read file")
        print("4. Backup file")
        print("5. Show all backup files")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            content = input("Enter content to write:\n")
            with open(fp, "w", encoding="utf-8") as f:
                f.write(content)
            print("File written successfully.")

        elif choice == "2":
            more = input("Enter content to append:\n")
            with open(fp, "a", encoding="utf-8") as f:
                f.write("\n" + more)
            print("Content appended.")

        elif choice == "3":
            if fp.exists():
                with open(fp, "r", encoding="utf-8") as f:
                    print("\nFile Content:\n", f.read())
            else:
                print("File not found.")

        elif choice == "4":
            if fp.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = fp.with_name(
                    f"{fp.stem}_Legaspi_backup_{timestamp}{fp.suffix}"
                )
                shutil.copy2(fp, backup_file)
                print(f"Backup created: {backup_file.name}")
            else:
                print("Cannot backup. File does not exist.")

        elif choice == "5":
            backups = list(backup_dir.glob("*backup*"))
            if backups:
                for b in backups:
                    print("-", b.name)
            else:
                print("Compilation of Backup Files")

        elif choice == "6":
            print("Exiting the file manager.")
            break

        else:
            print("Invalid choice. Please try again.")

file_manager()