## Word Square Generator
This project generates all possible word squares from a given list of four-letter words. A word square is a special type of word arrangement where the words read the same horizontally and vertically.

## Features
Uses a Trie data structure for efficient prefix searching.
Supports depth-first search (DFS) to construct word squares.
Outputs results to both text and JSON files with indices for each word square.
Includes detailed debug statements to trace the computation step-by-step.

## Requirements
Python 3.x
Usage
Input File
Prepare a text file named four_letter_words.txt in the same directory as the script. This file should contain four-letter words, one per line.

#### Example four_letter_words.txt:

- area
- ball
- dear
- lady
- lead
- yard

## Running the Script

run main.py

### Output Files
results.txt: A text file containing all the word squares found, with each square indexed.
results.json: A JSON file containing all the word squares found, with each square indexed.

#### Example Output
results.txt:
* ball
* area
* lead
* lady


* dear
* area
* rear
* dear


### results.json
[
    {
        "index": 1,
        "square": [
            "ball",
            "area",
            "lead",
            "lady"
        ]
    },
    {
        "index": 2,
        "square": [
            "dear",
            "area",
            "rear",
            "dear"
        ]
    }
]

## Script Explanation
Trie Class
The Trie class is used to build a prefix tree (Trie) for efficient prefix searches.

## Solution Class
The Solution class is used to insert words into the Trie and perform a depth-first search to find all possible word squares.

## Functions
read_words_from_txt(file_path): Reads words from a text file and filters by length.
write_results_to_txt(file_path, squares): Writes the results to a text file.
write_results_to_json(file_path, squares): Writes the results to a JSON file.
Main Function
The main function coordinates reading the input file, generating word squares, and writing the results to the output files.

## Debugging
The script includes debug statements to print detailed information about the steps of building word squares, including inserting words into the Trie, searching for prefixes, starting new word squares, trying words, and backtracking.


