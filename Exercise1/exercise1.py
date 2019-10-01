
stop_words_file = open("stop_words.txt", "r");

stop_words_lines = stop_words_file.readlines();

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

story = open("test.txt", "r");

for line in story:
    word = '';
    for letter in range(len(line)):
        if (letter +1) != len(line) and is_legal(line[letter]):
            word += line[letter];
            if (is_not_legal(line[letter + 1])):
                if word in stop_words:
                    print("stop word!");
                else:
                    if word in words:
                        pass;
                    else:
                        words[word] = 1
                print(word);
                word = '';
