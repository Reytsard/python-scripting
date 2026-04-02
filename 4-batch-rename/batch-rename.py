import logging
import argparse
from pathlib import Path
import os
from typing import List

logging.basicConfig(
    level=logging.INFO
)


def rename(path, file_type, prefix, suffix, count):
    prefix = f"{prefix}_" if prefix else ""
    suffix = f"_{suffix}" if suffix else ""
    for file in path.iterdir():
        if os.path.exists(file) and file.suffix == f".{file_type}" or file_type is None:
            new_name = f"{path}{os.sep}{prefix}{count:04d}{suffix}{file.suffix}"
            os.rename(file, new_name)
            count += 1
            logging.info(f"renamed {file} to {new_name}")
        else:
            logging.info(f"skipping {file.name}")


def run(args):
    path = args.path
    file_type = args.file_type
    prefix = args.prefix
    suffix = args.suffix
    count: int = 1
    rename(path, file_type, prefix, suffix, count)


def main():
    parser = argparse.ArgumentParser(description="renames files per batch to reduce repetitve actions")
    parser.add_argument("path", type=Path, help="path of folder to rename all files")
    parser.add_argument("--file_type", type=str, help="type of files to include for renaming files")
    parser.add_argument("--prefix", type=str, default="", help="prefix of files to rename")
    parser.add_argument("--suffix", type=str, default="", help="suffix of files to rename")

    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()


#python 4-batch-rename\batch-rename.py 4-batch-rename\to_rename
# C:\Balong\python-scripting>python 4-batch-rename\batch-rename.py 4-batch-rename\to_rename --file_type png --prefix image
#
# C:\Balong\python-scripting>python 4-batch-rename\batch-rename.py 4-batch-rename\to_rename --file_type ts --prefix code --suffix typescript