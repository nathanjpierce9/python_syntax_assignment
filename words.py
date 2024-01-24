def print_upper_words(words):
    """ Print each word on a separate line uppercased"""
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """ print each word on separate line uppercased if it starts with e or E"""
    for word in words:
        if word.startswith("e") or word.startswith ("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
