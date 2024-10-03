# DSC510
# Week 8
# Exercise 8.1
# Author: Makayla McKibben
# Date 07.28.2024

# This program reads a text file line by line
# and counts the number of times a word appears
# then sorts it and prints it.
# It also prints this same information to a new text file
# with the name defined by the user.

import string

# Defining main to read the text file then call the next function
def main():
    counts = {}
    try:
        getty_text = open('Gettysburg.txt', 'r')
        process_line(getty_text, counts)
    except FileNotFoundError:
        print("File not found")
    try:
        new_name = input('Enter new filename: ')
        new_name = new_name.translate(str.maketrans('', '', string.punctuation))
        new_name = new_name.lower()
    except FileExistsError:
        print('File already exists')
    try:
        if not new_name.endswith('.txt'):
            new_name += '.txt'
            print(f'New file name is: {new_name}')
            fout = open(new_name, 'w')
    except:
        print("Could not set file type for file to '.txt'")
    try:
        fout = open(new_name, 'w')
        fout.write(f'Length of the dictionary: ')
        dict_len = (len(counts))
        dict_len = str(dict_len)
        fout.write(dict_len)
        fout.write('\n')
        pretty_print(counts)
        process_file(counts, new_name)
    except:
        print("Something went wrong, could not write to file.")
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

def process_file(counts, new_name):
    try:
        fout = open(new_name, 'a')
        fout.write('{:12} {:>14}'.format("Word", "Count"))
        fout.write(f'---------------------------')
        fout.write('\n')
        lst = []
        for key, val in list(counts.items()):
            lst.append((val, key))
        i = 0
        lst.sort(reverse=True)
        for i in range(0, len(lst)):
            fout.write('{:12} {:>14}'.format(lst[i][1], lst[i][0]))
            fout.write('\n')
            i += 1
    except:
        print("Something went wrong! Could print to file.")
        return


# Call to main
if __name__ == '__main__':
    main()
