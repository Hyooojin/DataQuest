from string import punctuation


def no_punc(txt):
    return ''.join(a for a in txt if not a in punctuation).rstrip().lower()
    # return ''.join(a if not a in punctuation else ' ' for a in txt).rstrip().lower()

with open('dictionary.txt', 'r') as f:
    # [print(a.rstrip()) for a in f.read().split()]
    normalized_dictionary_tokens = [no_punc(a) for a in f.read().split()]

with open('story.txt', 'r') as f:
    normalized_story_tokens = [no_punc(a) for a in f.read().split()]

correct = list()
misspelled = list()

[correct.append(a) if a in normalized_dictionary_tokens
 else misspelled.append(a) for a in normalized_story_tokens]
