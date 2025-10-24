# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

# BookBot
A CLI tool that analyzes a text file (like a book) and reports word counts, character frequencies, and other stats.

## Features
- Count total words
- Frequency of each character (letters only or all chars—configurable)
- Top-N most common words
- Optional JSON output and file export
- Clean, deterministic output for grading

## Installation
- Requires Python 3.10+

```bash
git clone https://github.com/oscar-villars/bookbot
cd bookbot
# optional: create a venv
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # if present