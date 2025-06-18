file = open('sometext.txt', 'r') # open sometext.txt file
text = file.read() # read entire content of file
file.close() # close file
text = text.lower() # convert to lowercase
words = text.split() # split into words
new_words = [] # store cleaned words

for w in words:
    clean_w = w.strip('.,') # remove punctuation
    if clean_w:
        new_words.append(clean_w)

count = {} # dictionary to count words

for w in new_words: # count each word
    if w in count:
        count[w] = count[w] + 1
    else:
        count[w] = 1

for w in count: # print the results
    print(w + ':', count[w])
