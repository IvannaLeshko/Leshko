def replace_word(text, old_word, new_word):
    result = ""
    words = text.split()
    for i in range(len(words)):
        if words[i] == old_word:
            words[i] = new_word
    result = " ".join(words)
    return result