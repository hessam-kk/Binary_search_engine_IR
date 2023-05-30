## Reading Files
data = {}
file_names = ('lyrl2004_tokens_train.dat',
              #   'lyrl2004_tokens_test_pt2.dat',
              #   'lyrl2004_tokens_test_pt3.dat',
              )

for file_name in file_names:
    with open(file_name, 'r') as f:
        x = f.readlines()

    ID = ''
    for line in x:
        if '.I' in line:
            ID = line.replace('.I ', '').strip()
            data[ID] = ''
            print((ID + '\n') * (int(ID) % 100_000 == 0), end='')
        elif line == '.W\n':
            continue

        else:
            data[ID] += line + ' '
        # input()

print('A total of {} documents has been loaded...!\n'.format(len(data)))


## Create Dictionary/Vocabulary
vocab_list = {}

for key, val in data.items():
    vocab_list[key] = set(val.split())
    

print('A total of {} documents has been tokenized...!\n'.format(
    len(vocab_list)))
from itertools import chain
tokens = *chain(*vocab_list.values()),
print('A total of {} tokens has been extracted...!\n'.format
      (len(tokens)))

## Creating Posting List
print('Creating Posting List')
posing_list = {}
for token in tokens[:100]:
    posing_list[token] = []
    for doc_id, doc_txt in vocab_list.items():
        if token in doc_txt:
            posing_list[token].append(doc_id) 

print('Finished Creating Posting List.')

## Write Posing List to the file
with open('Posting_list.dat', 'w') as f:
    for token, post_list in posing_list.items():
        f.write(token + ': ' + '->'.join(post_list) + '\n\n')


  
def intersection(lst1, lst2):
    return set(lst1) & set(lst2)

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

        # handle multiple word search
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
               
              
        # handle single word
        elif posing_list.get(word):
            print(border)
            print('The word {} has {} occurance in all documents, here are the top documents:'.format(word, len(posing_list[word])))
            print(posing_list[word][:min(len(posing_list[word]), 50)])
            
            show_doc(word)
            print(border)
            
                
        # Not found 
        else:
            print('No such a word found in our database. \
                Try searching other words! ')
            
        
