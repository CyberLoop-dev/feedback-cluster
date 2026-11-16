#!/usr/bin/env python3
"""Cluster short text notes using TF-IDF and cosine similarity."""
import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

STOP = {"a","an","and","are","as","at","be","but","by","for","from","in","is","it","of","on","or","our","the","to","was","we","with"}

def tokenize(text):
    return [word for word in re.findall(r"[a-z0-9']+", text.lower()) if len(word) > 1 and word not in STOP]

def tfidf_vectors(documents):
    tokens = [tokenize(doc) for doc in documents]
    document_frequency = Counter()
    for words in tokens:
        document_frequency.update(set(words))
    count = len(tokens)
    vectors = []
    for words in tokens:
        frequencies = Counter(words)
        vector = {}
        for word, frequency in frequencies.items():
            tf = frequency / max(1, len(words))
            idf = math.log((1 + count) / (1 + document_frequency[word])) + 1
            vector[word] = tf * idf
        norm = math.sqrt(sum(value * value for value in vector.values())) or 1.0
        vectors.append({word: value / norm for word,value in vector.items()})
    return vectors

def similarity(left, right):
    return sum(value * right.get(word, 0.0) for word,value in left.items())

def cluster_texts(documents, threshold=0.28):
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    vectors = tfidf_vectors(documents)
    parent = list(range(len(documents)))
    def find(item):
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            if similarity(vectors[i], vectors[j]) >= threshold:
                union(i, j)
    groups = defaultdict(list)
    for index, document in enumerate(documents):
        groups[find(index)].append({"index": index + 1, "text": document})
    return [groups[key] for key in sorted(groups)]

def main():
    parser = argparse.ArgumentParser(description="Cluster feedback notes with local TF-IDF similarity.")
    parser.add_argument("input", type=Path, help="One feedback item per line")
    parser.add_argument("--threshold", type=float, default=0.28)
    parser.add_argument("--output", type=Path, default=Path("clusters.json"))
    args = parser.parse_args()
    try:
        documents = [line.strip() for line in args.input.read_text(encoding="utf-8").splitlines() if line.strip()]
        clusters = cluster_texts(documents, args.threshold)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    args.output.write_text(json.dumps({"count": len(documents), "clusters": clusters}, indent=2), encoding="utf-8")
    print(f"Grouped {len(documents)} items into {len(clusters)} cluster(s): {args.output}")
if __name__ == "__main__":
    main()
