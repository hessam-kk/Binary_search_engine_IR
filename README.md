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

## Reading Files

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

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/8160ee10-46b8-48f8-b0c5-5148ef2e3ed7)

## Create Dictionary/Vocabulary

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/72ca5897-7d7b-4de6-85a3-8d9c87c0d2eb)

This code creates a dictionary of unique words (or tokens) found in a collection of documents. 

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/4022efab-f4e2-4459-937e-1c157ad30c96)

Here's a step-by-step breakdown of what each part of the code does:

•	The first line initializes an empty dictionary called vocab_list. This dictionary will store the unique words found in each document.

•	The for loop iterates over each item in the data dictionary (created in the previous code snippet). For each document, the code splits the text into individual words using the split() method and creates a set of unique words. The document ID is used as the key in the vocab_list dictionary, and the set of unique words is stored as the value.

•	After processing all the documents, the code prints a message indicating the total number of documents that have been tokenized (i.e., had their words extracted and stored in vocab_list).

•	The next line imports the chain() function from the itertools module. The chain() function is used to concatenate multiple lists or sets into a single iterable object.

•	The tokens variable is assigned the result of calling chain() with the values in vocab_list as arguments. The * operator before chain() unpacks the values in vocab_list into separate arguments. This effectively flattens the nested sets of words from each document into a single iterable object of all unique words.
Overall, this code creates a dictionary of unique words in a collection of documents and calculates the total number of unique words extracted from the documents. 

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/58ab8223-fa01-4f92-97cc-320a80d542d8)

## Creating Posting List

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/e19c9f3d-51a9-4913-a8d1-856415147b0b)

This code creates a posting list for the tokens extracted in the previous code snippet. 
```
## Creating Posting List
print('Creating Posting List')
posing_list = {}
for token in tokens[:100]:
    posing_list[token] = []
    for doc_id, doc_txt in vocab_list.items():
        if token in doc_txt:
            posing_list[token].append(doc_id) 

print('Finished Creating Posting List.')
```
Here's a step-by-step breakdown of what each part of the code does:

•	The posing_list variable is initialized as an empty dictionary. This dictionary will store the posting list for each token (i.e., the documents that contain the token).

•	The for loop iterates over the first 1000 tokens in the tokens iterable (created in the previous code snippet). For each token, the code initializes an empty list as the value for the token in the posing_list dictionary. The number 1000 is selected for test as the larger numbers will take much more time to compute.

•	The next for loop iterates over each item in the vocab_list dictionary. For each document, the code checks if the current token is in the document's set of words (i.e., if the token appears in the document). If it does, the code appends the document ID to the list of documents associated with the current token in the posing_list dictionary.

•	After processing all the documents for the current token, the code moves on to the next token and repeats the process until 1000 tokens have been processed.

Overall, this code creates a posting list for a subset of tokens extracted from a collection of documents. The posting list indicates which documents contain each token and can be used for text search and analysis purposes. Note that this code only processes a subset of the tokens (the first 1000), so the full posting list for all tokens would require changing this number.

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/74a4718b-ae2a-4d08-9cac-f09da96c1b71)

## Writing to file

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/c249acee-f4c0-409a-99d3-7b7add86977f)

This is not an important part to describe separately, but Midjourney works amazing… :))))
```
## Write Posing List to the file
with open('Posting_list.dat', 'w') as f:
    for token, post_list in posing_list.items():
        f.write(token + ': ' + '->'.join(post_list) + '\n\n')
```

This code writes all the result into a file called Posting_list in a format of linkedlist. 

# Interactive Search Engine

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/3a227d4f-2e4e-449d-b5c7-3b0bf205ceab)

Here, we defined a few functions to work with.

```       
def intersection(lst1, lst2):
    return set(lst1) & set(lst2)
```

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/482a759b-7112-41b1-9b26-71c8660a2a45)


```
def show_doc(word):
    print('Enter the document ID to open it.\
        enter \\all to show all the documents number. \
                Enter "\\return" to return to main menu')
    doc_id = input('>> ')
    if doc_id == '\all':
        if word == 0:
            print(intersec_list)
        else:
            print(posing_list[word])
            
    print('Enter the document ID to open it.\
        enter \\all to show all the documents number. \
                Enter "\\return" to return to main menu')
    doc_id = input('>> ')

    while doc_id != '\\return':
        if data.get(doc_id):
            print(border)
            print(border)
            print(data[doc_id])
            print(border)
            print(border)
            print('Enter another document ID to open it.\
            Enter "\\return" to return to main menu')
            doc_id = input('>> ')
            
        else:
            print('You may entered a wrong document Id. Try again.\
                Enter the document ID to open it. \
                Enter "\\return" to return to main menu')
            doc_id = input('>> ')
```

The second function show_doc(word) is used to display the contents of a document. It takes a word as input to handle batch file show. This function prompts the user to enter a document ID. In the main program, to make it consice, we only show the first 50 results to the user, so If the user enters '\all', it prints out a list of all document IDs containing the input word (if word != 0, we comprehend that the user query is containing only one word, then it prints out the documents containing the input word; if word == 0, we understand that we have to deal with intersection_list, thus it prints out the documents number in the intersect_list). If the user enters a valid document ID, it prints out the contents of that document. The function then prompts the user to enter another document ID or '\return' to return to the main menu. If the user enters an invalid document ID, it prompts the user to try again.

![image](https://github.com/hessam-kk/Binary_search_engine_IR/assets/24957423/c3509c88-43e3-4436-8527-4ac787e9d558)


# Main Part

```
border = '=' * 150
if __name__ == '__main__':
    while True:
        print(border)
        print('Type a word to search in documents. \
            Search multiple words by using the + sign. \
            Type "\exit" to finish the program')
        word = input('>> ')
        
        if word == '\exit':
            break
```
This code is the main part of a search engine that allows users to search for words in a set of documents. Here is an explanation of the code:
This code allows users to search for words in a set of documents. The program first prompts the user to input a word to search for. The user can also search for multiple words by using the + sign to join the words. If the user inputs the "\exit" command, the program terminates.

## handle multiple word search
```
if '+' in word:
            words = [x.strip() for x in word.split('+')]
            bundle = [[posing_list.get(x)] for x in words]
            try:
                intersec_list = bundle.pop()
                # merge all lists
                while bundle:
                    intersec_list = intersection(intersec_list, bundle.pop())
                    # flatten the list
                    while len(intersec_list) == 1:
                        intersec_list = intersec_list[0]
                        
            except:
                pass
            
            # # flatten the list
            while len(intersec_list) == 1:
                        intersec_list = intersec_list[0]
                
            print(intersec_list[:min(len(intersec_list), 50)])
            show_doc(0)
```
If the user searches for multiple words, the program generates a list of documents that contain all of the searched words. The program outputs the first 50 documents that contain all of the searched words and prompts the user to select a document ID to open. If the user inputs "\all", the program outputs all of the document IDs that contain all of the searched words.


