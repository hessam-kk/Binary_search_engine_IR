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
