# import libraries
import pandas as pd
import re
import gc
# import emoji
from bs4 import BeautifulSoup
import nltk
import itertools
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize, wordpunct_tokenize
import warnings
warnings.filterwarnings("ignore")


# text cleaning functions

# remove tags
def remove_tag(text):
    return ' '.join(re.sub("(@[A-Za-z0-9-_]+)", " ", text).split())


# remove pattern
def remove_pattern(text, pattern):
    r = re.findall(pattern, text)
    for i in r:
        text = re.sub(i, ' ', text)
    return text


# remove punctuations
def remove_punctuation(text, punct):
    text = "".join([char for char in text if char not in punct])
    # text = re.sub('[0-9]+', '', text)
    return text


# remove stopwords
def stop_word_remove(text, tokens):
    temp = [token for token in tokens if token not in STOP_WORDS]
    return ' '.join(word for word in temp)


# contractions dictionary
CONTRACTION_MAP = {
    "ain't": "is not",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "I'd": "I would",
    "I'd've": "I would have",
    "I'll": "I will",
    "I'll've": "I will have",
    "I'm": "I am",
    "I've": "I have",
    "i'd": "i would",
    "i'd've": "i would have",
    "i'll": "i will",
    "i'll've": "i will have",
    "i'm": "i am",
    "i've": "i have",
    "isn't": "is not",
    "it'd": "it would",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she would",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so as",
    "that'd": "that would",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there would",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you would",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have"
}


# Expand contraction
def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),
                                      flags=re.IGNORECASE | re.DOTALL)

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match) \
            if contraction_mapping.get(match) \
            else contraction_mapping.get(match.lower())
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text


# remove non-ascii characters
def remove_non_ascii_character(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])


# Replacing the Repeating words or jargons like loooovee, saddd
class RepeatReplacer(object):

    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'

    def replaceword(self, word, orig_word):
        if wordnet.synsets(word):
            # print("matched")
            if len(word) > 1:
                return word
            else:
                return orig_word
        repl_word = self.repeat_regexp.sub(self.repl, word)
        if repl_word != word:
            return self.replaceword(repl_word, orig_word)
        else:
            return orig_word


def replacerepeat(text, tokens):
    rplc = RepeatReplacer()
    text = tokens
    # text = wordpunct_tokenize(text)
    # print(text)

    j = 0
    for _str in text:
        # _str = re.sub('’','\'', _str)
        # _str = re.sub('[^a-zA-Z0-9-_\'@#/]', '', _str)
        if not _str.startswith(('@', '#')):
            if not bool(re.search(r'\d', _str)):
                orig = _str
                _str = re.sub('[^a-zA-Z0-9-_\']', '', _str)
                # print(_str)
                text[j] = rplc.replaceword(_str, orig_word=orig)
                # print(text[j])
                # print(orig)
        j = j + 1

    return ' '.join(text)
    # return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in text]).strip()


# Handling Emoticons and Emojis
SMILEYS = {":‑)": "smiley",
           ":-]": "smiley",
           ":-3": "smiley",
           ":->": "smiley",
           "8-)": "smiley",
           ":-}": "smiley",
           ":)": "smiley",
           ":]": "smiley",
           ":3": "smiley",
           ":>": "smiley",
           "8)": "smiley",
           ":}": "smiley",
           ":o)": "smiley",
           ":c)": "smiley",
           ":^)": "smiley",
           "=]": "smiley",
           "=)": "smiley",
           ":-))": "smiley",
           ":‑D": "smiley",
           "8‑D": "smiley",
           "x‑D": "smiley",
           "X‑D": "smiley",
           ":D": "smiley",
           "8D": "smiley",
           "xD": "smiley",
           "XD": "smiley",
           ":‑(": "sad",
           ":‑c": "sad",
           ":‑<": "sad",
           ":‑[": "sad",
           ":(": "sad",
           ":c": "sad",
           ":<": "sad",
           ":[": "sad",
           ":-||": "sad",
           ">:[": "sad",
           ":{": "sad",
           ":@": "sad",
           ">:(": "sad",
           ":'‑(": "sad",
           ":'(": "sad",
           ":‑P": "playful",
           "X‑P": "playful",
           "x‑p": "playful",
           ":‑p": "playful",
           ":‑Þ": "playful",
           ":‑þ": "playful",
           ":‑b": "playful",
           ":P": "playful",
           "XP": "playful",
           "xp": "playful",
           ":p": "playful",
           ":Þ": "playful",
           ":þ": "playful",
           ":b": "playful",
           "<3": "love"}


# replace emoji with text
def replaceEmojiEmoticons(text, tokens):
    words = tokens
    reformed = [SMILEYS[word] if word in SMILEYS else word for word in words]
    text = " ".join(reformed)
    text = emoji.demojize(text)
    # text = text.replace(":"," ")
    return ' '.join(text.split())


def data_cleaning(text, **params):
    # HTML decoding
    if params['htmldecode']:
        text = BeautifulSoup(str(text), 'lxml').get_text()

    # Tag Removal
    if params['remove_tags']:
        text = remove_tag(text)

    # Remove Hashtags
    if params['remove_hashtags']:
        text = remove_pattern(text, "#")

    # Remove Links
    if params['remove_links']:
        text = remove_pattern(text, "https?://[A-Za-z0-9./]+")

    # Remove Punctuations
    if params['remove_punct']:
        text = remove_punctuation(text, params['punct'])

    # Contraction Correction
    if params['contraction_correction']:
        text = expand_contractions(text, contraction_mapping=CONTRACTION_MAP)

    # Slang Correction
    if params['slang_correction']:
        text = slag_corrections(text, 'ShortendText.json')

    tokens = text.split(' ')

    # Replace Emoji
    if params['replace_emoji']:
        text = replaceEmojiEmoticons(text, tokens)

    # Replace Repeating words/jargon's (new method)
    if params['replace_repeat']:
        # print("repeating")
        text = replacerepeat(text, tokens)

    # Remove Stopwords
    if params['remove_stopwds']:
        text = stop_word_remove(text, tokens)

    # Remove Non-ASCII Character
    if params['remove_non_ascii']:
        text = remove_non_ascii_character(text)

    # Remove Non-ASCII Character
    if params['remove_RT']:
        if text[:2] == 'RT':
            text = text[3:]

    return text
