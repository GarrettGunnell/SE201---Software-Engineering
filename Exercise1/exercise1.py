
stop_words_file = open("stop_words.txt", "r");

stop_words_lines = stop_words_file.readlines();

stop_words = [];

for line in stop_words_lines:
    word = '';
    for letter in range(len(line)):
        if (letter + 1) != len(line) and line[letter] != ',':
            word += line[letter];
            if (line[letter + 1] == ','):
                stop_words.append(word);
                word = '';

for i in stop_words:
    print(i)
