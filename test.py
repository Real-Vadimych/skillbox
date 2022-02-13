words =[]
with open('anna_words.txt', encoding='UTF-8') as file:
    words = [word.strip() for word in file]



len_words = {}
for word in words:
    lenght = len(word)
    if lenght in len_words:
        len_words[lenght] += 1
    else:
        len_words[lenght] = 1

sorted_words = {k: len_words[k] for k in sorted(len_words)}

for k, v in sorted_words.items():
    print(f'{k}; {v}')