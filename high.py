def high(x):
    words = x.split()
    max_score = 0
    best_word = ""

    for word in words:
        score = sum(ord(char) - ord('a') + 1 for char in word)
        if score > max_score:
            max_score = score
            best_word = word

    return best_word