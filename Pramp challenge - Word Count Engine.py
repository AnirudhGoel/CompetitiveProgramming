# Pramp challenge - Word Count Engine (https://www.pramp.com/challenge/W5EJq2Jld3t2ny9jyZXG)

from collections import OrderedDict

def word_count_engine(document):
  striped_s = list()
  for i in range(len(document)):
    if 97 <= ord(document[i].lower()) <= 122 or document[i] == ' ':
      striped_s.append(document[i].lower())
  
  striped_s = ''.join(striped_s)
  document_words = striped_s.split(' ')
  
  word_count_map = OrderedDict()
  
  for word in document_words:
    if word != '':
      word_count_map[word] = word_count_map.get(word, 0) + 1
  
  word_count_list = [[] for _ in range(len(document_words))]
  
  for word in word_count_map.keys():
    word_count_list[word_count_map[word]].append(word)
  
  output = []
  
  for i in range(len(word_count_list)-1, -1, -1):
    if word_count_list[i]:
      word_list = word_count_list[i]

      for word in word_list:
        output.append([word, str(i)])

  return output