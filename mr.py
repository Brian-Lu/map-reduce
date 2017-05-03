# Book Text
raw = open("Crime_and_Punishment.txt", "r").read().lower().strip().split()

def freq(word):
    return len(filter(lambda cur_word: cur_word == word, raw))

def total_freq(words):
    return len(filter(lambda cur_word: cur_word in words, raw))

def most_freq_helper(first_el, second_el): #basically max function but max() doesn't work because of arguments???
    if first_el > second_el:
        return first_el
    else:
        return second_el

def most_freq():
    word_freq = {}
    for cur_word in raw:
        if cur_word in word_freq:
            word_freq[cur_word] += 1
        else:
            word_freq[cur_word] = 0
    values = word_freq.values()
    amount_of_occurences = reduce(most_freq_helper, values)
    for item in word_freq:
        if word_freq[item] == amount_of_occurences:
            return item

#TEST CASES
print freq("the")

print freq("crime")

print freq("punishment")

test_case = ["the", "crime", "punishment"]

print total_freq(test_case)

print most_freq()