import os
import time
import json


class Trie:
    def __init__(self):
        # Each Trie node contains an array of 26 Trie nodes, representing the 26 lowercase English letters
        self.children = [None] * 26
        # 'values' is a list that holds the indices of words corresponding to the node path
        self.values = []

    def insert(self, word, index):
        # Insert a word into the Trie with corresponding index
        node = self
        for char in word:
            char_index = ord(char) - ord('a')
            if not (0 <= char_index < 26):  # Ensure the character is a lowercase English letter
                raise ValueError(f"Invalid character '{char}' in word '{word}'")
            if node.children[char_index] is None:
                node.children[char_index] = Trie()
            node = node.children[char_index]
            # Append the index of the word at every character's node
            node.values.append(index)
        print(f"Inserted word '{word}' with index {index} into Trie")

    def search(self, prefix):
        # Return a list of indices of words that start with the given prefix
        node = self
        for char in prefix:
            char_index = ord(char) - ord('a')
            if not (0 <= char_index < 26):  # Ensure the character is a lowercase English letter
                raise ValueError(f"Invalid character '{char}' in prefix '{prefix}'")
            if node.children[char_index] is None:
                return []  # Prefix not found
            node = node.children[char_index]
        print(f"Found prefix '{prefix}' with indices {node.values}")
        return node.values


class Solution:
    def __init__(self, words):
        self.trie = Trie()
        self.words = words
        self.squares = []

        # Insert all words into the Trie along with their respective indices
        for i, word in enumerate(words):
            self.trie.insert(word, i)

    def word_squares(self):
        def dfs(square):
            # Depth-first search to build word squares
            if len(square) == len(self.words[0]):  # Base case: Square is complete
                self.squares.append(square[:])  # Add a deep copy of the current square to results
                print(f"Completed word square: {square}")
                return
            # Get the current prefix to be matched from all words in the square
            idx = len(square)
            prefix = [word[idx] for word in square]
            # Find all words in the Trie with the current prefix
            indices = self.trie.search(''.join(prefix))
            for index in indices:
                square.append(self.words[index])  # Add the matching word to the current square
                print(f"Depth {idx}: Trying word '{self.words[index]}'")
                dfs(square)  # Continue to build the square recursively
                square.pop()  # Backtrack to try another word
                print(f"Backtracking from word '{self.words[index]}'")

        # Initialize the depth-first search with each word as a starting point
        for word in self.words:
            print(f"Starting new word square with '{word}'")
            dfs([word])

        return self.squares


def read_words_from_txt(file_path):
    """Read words from a text file and filter by length."""
    with open(file_path, 'r') as file:
        words = [line.strip().lower() for line in file if len(line.strip()) == 4 and line.strip().isalpha()]
    return words


def write_results_to_txt(file_path, squares):
    """Write the results to a text file"""
    with open(file_path, 'w') as file:
        if squares:
            for index, square in enumerate(squares):
                file.write(f"Square {index + 1}:\n")
                for row in square:
                    file.write(row + "\n")
                file.write("\n")
        else:
            file.write("No valid word square found.\n")


def write_results_to_json(file_path, squares):
    """Write the results to a JSON file, including the sorted characters used and their length"""
    squares_with_chars = [{
        "index": index + 1,
        "square": square,
        "square_characters": sorted(list(set(''.join(square)))),  # Sort characters alphabetically
        "square_length": len(sorted(list(set(''.join(square)))))  # Length of the unique characters array
    } for index, square in enumerate(squares)]

    with open(file_path, 'w') as file:
        json.dump(squares_with_chars, file, indent=4)
    print(f"Results written to {file_path}")


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(current_dir, 'four_letter_words.txt')
    output_txt_file_path = os.path.join(current_dir, 'results.txt')
    output_json_file_path = os.path.join(current_dir, 'results.json')

    words = read_words_from_txt(input_file_path)

    solution = Solution(words)
    start_time = time.time()
    all_squares = solution.word_squares()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total elapsed time: {elapsed_time:.2f} seconds")

    if all_squares:
        print("Word Squares:")
        for square in all_squares:
            for row in square:
                print(row)
            print()
    else:
        print("No valid word square found.")

    write_results_to_txt(output_txt_file_path, all_squares)
    write_results_to_json(output_json_file_path, all_squares)


if __name__ == "__main__":
    main()
