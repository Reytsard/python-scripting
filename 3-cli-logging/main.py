import logging
import argparse
from pathlib import Path

logging.basicConfig(level=logging.INFO,
                    # format="%(asctime)s %(levelname)s %(message)s",
                    )
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")


def run(args):
    print(args.verbose)
    with args.file.open() as f:
        for line in f:
            if args.level is None or args.level in line:
                level = args.level.upper()
                if level == "DEBUG":
                    logging.debug(line)
                elif level == "INFO":
                    logging.info(line)
                elif level == "WARNING":
                    logging.warning(line)
                elif level == "ERROR":
                    logging.error(line)
                elif level == "CRITICAL":
                    logging.critical(line)


def main():
    parser = argparse.ArgumentParser(description="Logging example")
    parser.add_argument("file",type=Path, help="File for uploading")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--level",type=str, help="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")

    args = parser.parse_args()
    run(args)

if __name__ == "__main__":
    main()