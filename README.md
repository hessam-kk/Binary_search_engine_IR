# Binary_search_engine_IR
A binary search engine implementation for the Information Retrieval course

# Introduction

This project involves building a search engine for searching in multiple
documents. The main objective of this project was to develop a tool that can
quickly and accurately search for a specific word or phrase in a collection of
documents and return the relevant results. To achieve this, I implemented a
posting list that stores the terms and their corresponding documents. This
allowed the search engine to efficiently index and retrieve the documents that
contain the search term. Overall, this project provided me with valuable
experience in developing information retrieval systems and utilizing data
structures for efficient search operations.

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/41781e25-ce83-44b3-8cdb-8a7f9966b1bc)

## Explain Reading Files

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/c2e7177c-c83e-4027-af7e-923d9d8c7da5)

First, I set the file names that I want to load into my program. Please note
that because files were really huge, to test the program I just use the content
of only one file, as well others are commented.

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/9ca6103f-8e56-459d-b8c3-4f0e82a4a25e)

After that, I we reach here:

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/3267c04c-038f-418b-9c30-6874687af187)

This code reads multiple text files and extracts relevant information from them to build a data dictionary. Here's a step-by-step breakdown of what each part of the code does:

•	The first line of code starts a for loop that iterates over a list of file names (stored in the variable file_names). 

•	The second line opens the current file in read-only mode ('r') using a with block. This ensures that the file is properly closed after it has been read. The readlines() method reads the entire file and returns a list of lines.

•	The ID variable is initialized as an empty string. This variable will store the current document ID as the loop processes each line of the file.

•	The next block of code is a for loop that iterates over each line in the file (stored in the x variable). For each line, the code checks if it contains the string '.I' (indicating the start of a new document). If it does, the code extracts the document ID from the line and stores it in the ID variable. It also initializes an empty string in the data dictionary with the document ID as the key. To keep track of the code progress, we check If the document ID is a multiple of 100,000, the code prints the ID.

•	If the line is the string '.W', the code skips the line and continues with the next line.

•	Otherwise, the code appends the current line to the text associated with the current document ID in the data dictionary. The += operator concatenates the current line with the existing text and adds a space at the end.

Overall, this code reads multiple files and extracts the document IDs and text content from them, storing the data in a dictionary. The code also includes a print statement to display the document IDs for every 100,000th document to monitor progress while processing large numbers of files. (I got shocked when I see that chatGPT could comprehend that the print statement was to ‘monitor the progress for large number of files’…!!!!!)
