import os
import json
import shutil
from subprocess import PIPE, run
import sys

if __name__ = _main__:
    args = sys.argv 
    print(args)
    # Check if the script is run from the correct directory
    if not os.path.exists("data"):
        print("Please run this script from the root directory of the repository.")
        sys.exit(1)

    # Create a data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Define the URL for downloading the dataset
    url = "https://huggingface.co/datasets/stanfordnlp/stanford-corenlp-english/resolve/main/stanford-corenlp-english.zip"

    # Download the dataset
    print("Downloading dataset...")
    result = run(["wget", url, "-O", "data/stanford-corenlp-english.zip"], stdout=PIPE, stderr=PIPE)
    
    if result.returncode != 0:
        print("Error downloading dataset:", result.stderr.decode())
        sys.exit(1)

    # Unzip the downloaded file
    print("Unzipping dataset...")
    shutil.unpack_archive("data/stanford-corenlp-english.zip", "data")

    # Remove the zip file after extraction
    os.remove("data/stanford-corenlp-english.zip")

    print("Dataset downloaded and extracted successfully.")