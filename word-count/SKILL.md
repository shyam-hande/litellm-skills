---
name: word-count
description: Count words in text using Python helper script
---

# Word Count Skill

When the user asks to count words:

Execute exactly this command:

python3 word-count/scripts/count_words.py "$ARGUMENTS"

Rules:
- Never manually count words
- Always pass full user text
- Return only the script output

Example:

Input:
hello world from skill

Output:
Word Count: 4