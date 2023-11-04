from typing import List, Optional
from logger import logger
from sentence_transformers import SentenceTransformer
import csv
import os

model = SentenceTransformer('moka-ai/m3e-base')
sample_file = "../Sample/sample.txt"
csv_file = "../Database/m3e.csv"

def get_file_content(filename) -> List[str]:
    with open(file=filename, mode="r") as f:
        content = f.read()
    lines = [line for line in content.split("\n") if line != ""]
    logger.info("Read %d lines from %s", len(lines), filename)
    return lines

def create_vector(lines: List[str]) -> Optional[List[List[float]]]:
    try:
        embeddings = model.encode(lines)
        return embeddings
    except Exception as e:
        logger.warning("Error: %s", e)
        return None

def save_vector(vectors: List[List[float]]) -> None:
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        for vector in vectors:
            writer.writerow(vector)
    logger.info("Vectors have been written to %s" % csv_file)

if __name__ == "__main__":
    lines = get_file_content(sample_file)
    vectors = create_vector(lines)
    save_vector(vectors)
