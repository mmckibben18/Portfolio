# DSC510
# Week 7
# Exercise 7.1
# Author: Makayla McKibben
# Date 07.27.2024

# This program reads a text file line by line
# and counts the number of times a word appears
# sorts it and prints it.

import string

# Defining main to read the text file then call the next function
def main():
    counts = {}
    try:
        getty_text = open('Gettysburg.txt', 'r')
        process_line(getty_text, counts)
    except FileNotFoundError:
        print("File not found")
    pretty_print(counts)
    return

# This function adds the word to the dictionary and
# counts the number of times it's appeared
def add_word(words, counts):
    try:
        for word in words:
            if word not in counts:
                counts[word] = 1
                continue
            else:
                counts[word] += 1
                continue
    except:
       print("Something went wrong")
    return

# This function reads the line in the text file and removes the
# punctuation then separates the string to each word and calls add_word
def process_line(getty_text, counts):
    try:
        for line in getty_text:
            line = line.translate(str.maketrans('', '', string.punctuation))
            line = line.lower()
            words = line.split()
            add_word(words, counts)
            pass
    except:
        print("Something went wrong!")
    return

# This function prints the information nicely formatted
def pretty_print(counts):
    print(f'Length of the dictionary: ', len(counts))
    print('{:12} {:>14}'.format("Word", "Count"))
    print(f'---------------------------')
    lst = []
    for key, val in list(counts.items()):
        lst.append((val, key))
    i = 0
    lst.sort(reverse=True)
    for i in range(0, len(lst)):
        print('{:12} {:>14}'.format(lst[i][1], lst[i][0]))
        i += 1
    return


# Call to main
if __name__ == '__main__':
    main()
