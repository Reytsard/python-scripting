import argparse
from pathlib import Path
import os
import logging
import shutil

logging.basicConfig(level=logging.INFO)

def sort_dir(path):
    dir_path = Path(path)
    dirs = ["photos","documents","executables","others"]
    photos = []
    documents = []
    execs = []
    others = []

    for file in dir_path.iterdir():
        if not file.is_dir():
            if file.suffix == ".jpg" or file.suffix == ".jpeg" or file.suffix == ".png" or file.suffix == ".gif" or file.suffix == ".webp" or file.suffix == ".heic":
                photos.append(file)
            elif file.suffix == ".pdf" or file.suffix == ".docx":
                documents.append(file)
            elif file.suffix == ".exe":
                execs.append(file)
            else:
                others.append(file)

    # creation of directories
    for dir_location in dirs:
        path = dir_path / dir_location
        logging.info(f"Creating dir: {dir_location}")
        if not os.path.isdir(path):
            os.mkdir(path)
        else:
            logging.error(f"{dir_location} already exists, skipping")

    #move files into directory
    for file in photos:
        new_file_path = f"{dir_path}{os.sep}photos{os.sep}{file.name}"
        shutil.move(f"{file}", new_file_path)

    #move files into documents
    for file in documents:
        new_file_path = f"{dir_path}{os.sep}documents{os.sep}{file.name}"
        shutil.move(f"{file}", new_file_path)

    # move files into executables
    for file in execs:
        new_file_path = f"{dir_path}{os.sep}executables{os.sep}{file.name}"
        shutil.move(f"{file}", new_file_path)

    # move files into directory
    for file in others:
        new_file_path = f"{dir_path}{os.sep}others{os.sep}{file.name}"
        shutil.move(f"{file}", new_file_path)

def main(args):
    path = args.path
    logging.info(f"Path input: {path}")
    sort_dir(path)
    logging.info(f"directory sorted")

    exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort dir to images, documents, executables, others")
    parser.add_argument("path", help="path to dir to sort")

    args = parser.parse_args()

    main(args)