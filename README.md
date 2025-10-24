# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

A tiny script that reads and prints the text of Frankenstein.

## Requirements
- Python 3.10+ (or similar)

## Setup

This project ignores the books/ directory, so you must create it locally:

```bash
# from the project root (where main.py lives)
mkdir -p books
# download the text
curl -L -o books/frankenstein.txt https://www.gutenberg.org/cache/epub/84/pg84.txt