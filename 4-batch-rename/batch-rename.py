import logging
import argparse
from pathlib import Path

logging.basicConfig(
    level=logging.INFO
)

def run(args):
    pass

def main():
    parser = argparse.ArgumentParser(description="renames files per batch to reduce repetitve actions")
    parser.add_argument("path", type=Path, help="path of folder to rename all files")
    parser.add_argument("file_type",type=str,help="type of files to include for renaming files")

    args = parser.parse_args()
    run(args)

if __name__ == "__main__":
    main()
