from pathlib import Path
from datetime import datetime
import shutil

student_id = "2025-0476"
student_name = "Albert Wayne O. Legaspi"

documents_path = Path.home() / "Documents" / "Activity_5_Files"
backup_dir = documents_path / f"backup_{student_id}"
backup_dir.mkdir(parents=True, exist_ok=True)

log_file = documents_path / f"backup_log_{student_id}.txt"

def backup_file(target_filename: str):
    target_path = documents_path / target_filename

    if not target_path.exists():
        print(f"File not found: {target_filename}")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_filename = f"{target_path.stem}_{student_id}_{timestamp}{target_path.suffix}"
    backup_path = backup_dir / backup_filename

    shutil.copy2(target_path, backup_path)

    file_size = target_path.stat().st_size

    with log_file.open("a", encoding="utf-8") as log:
        log.write(f"Student ID: {student_id}\n")
        log.write(f"Student Name: {student_name}\n")
        log.write(f"Original File: {target_filename}\n")
        log.write(f"Timestamp: {timestamp}\n")
        log.write(f"File Size: {file_size} bytes\n")
        log.write(f"Backup Path: {backup_path}\n")
        log.write("-" * 50 + "\n")

    print(f"Backup completed for {student_id} ({student_name})")
    print(f"File saved as: {backup_filename}")
    print(f"Log updated at: {log_file}")

txt_files = list(documents_path.glob("*.txt"))

if not txt_files:
    print("No .txt files found to backup!")
else:
    for file in txt_files:
        print()
        backup_file(file.name)