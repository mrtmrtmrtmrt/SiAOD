
import string
def read_stroke(text):
    clean_text = split_stroke(text)

    freq = {}

    for word in clean_text:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq
     
def print_freq(freq):
    pair = freq.items()
    sorted_pairs = sorted(pair, key=lambda pair: pair[1], reverse=True)

    for word, value in sorted_pairs:          
        print(word, "->", value)

    return

def split_stroke(text):
    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))
    return text.split()
'''
    word_arr = []
    current_word = ""
    for sym in text:
        if sym.isalpha():
            current_word += sym
        elif (sym == " ") and (len(current_word) > 0):
            word_arr.append(current_word)
            current_word = ""

    if current_word:
        word_arr.append(current_word)

    return word_arr
'''
if __name__ == "__main__":
    stroke = "cat, dog cat bird dog cat , bob ? fdf dog  dog  dog  dog  dog  dog "
    freq_stroke = read_stroke(stroke)
    print_freq(freq_stroke)

