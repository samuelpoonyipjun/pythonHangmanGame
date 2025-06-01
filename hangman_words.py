word_list = []
with open('word_list.txt', 'r') as f:
    for line in f:
        word_list.append(line.strip())
new_word = input("Enter a new word to add to the word list: ")
if new_word in word_list:
  print("Word list already has that word.")
else:
  word_list.append(new_word)
  print("Word added to word list.")
  with open('word_list.txt', 'a') as f:
          f.write(new_word + '\n')
new_word_list = word_list