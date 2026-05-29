---
name: word-count
description: Count words in the given text
allowed-tools: Bash, Read
metadata:
  author: shyam
  version: "v1.0.1"
---

Use the Bash tool.

The Bash tool requires this structure:

Bash(command="python3 ~/.claude/skills/word-count/scripts/count_words.py \"$ARGUMENTS\"")

Execute the command exactly in this format.

Return only the script output.

