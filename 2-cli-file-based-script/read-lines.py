from pathlib import Path
import argparse

def count_lines(filename:Path) -> int:
    with filename.open() as f: #opens the file with .open and aliased it as f
        return sum(1 for _ in f) # 1 for _ in f, is a function that 


def main():
    parser = argparse.ArgumentParser(description="Line Counter")
    parser.add_argument("filename",type=Path,help="File path for file")

    args = parser.parse_args()

    total_lines = count_lines(args.filename)
    print(f"lines: {total_lines}")

if __name__ == "__main__":
    main()

# run "python read-lines.py <filepath>" in terminal to get the number of lines in the file.