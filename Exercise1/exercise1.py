stop_words_file = open("stop_words.txt", "r");
story = open("neuromancer.txt", "r");
stop_words_lines = stop_words_file.readlines();
rank = 1
stop_words = [];
words = {};

def is_legal(letter):
    return letter != ' ' and letter != ',' and letter != '.' and letter != '"' and letter != '?' and letter != '!' and letter != ';';

def is_not_legal(letter):
    return letter == ' ' or letter == ',' or letter == '.' or letter == '"' or letter == '?' or letter == '!' or letter == ';';

for line in stop_words_lines:
    word = '';
    for letter in range(len(line)):
        if (letter + 1) != len(line) and line[letter] != ',':
            word += line[letter];
            if (line[letter + 1] == ','):
                stop_words.append(word);
                word = '';

for line in story:
    word = '';
    for letter in range(len(line)):
        if (letter + 1) != len(line) and is_legal(line[letter]):
            word += line[letter];
            if (is_not_legal(line[letter + 1])):
                word = word.lower();
                if word in stop_words:
                    pass;
                else:
                    if word in words:
                        words[word] += 1;
                    else:
                        words[word] = 1
                word = '';

while rank <= 25:
    frequency = 0;
    frequent_word = ''
    for word in words:
        if words[word] > frequency:
            frequent_word = word;
            frequency = words[word];
    print(str(rank) + '. ' + frequent_word + ' - ' + str(frequency));
    words.pop(frequent_word);
    rank += 1;
