import random
from textblob import TextBlob
from spellchecker import SpellChecker
from sklearn.metrics import precision_score, recall_score, f1_score



class SpellingEvaluator:
    def __init__(self, data, sample):
        self.data = data
        self.sample = sample if len(data.keys()) >= sample else len(data.keys())

    def prepSample(self):
        sample_keys = random.sample(list(self.data.keys()), self.sample)
        self.sample_data = {sample_key: self.data[sample_key] for sample_key in sample_keys}

    def GetAccuracy(self):
        total_counter = 0
        textblob_counter = 0
        spellchecker_counter = 0
        spell_checker = SpellChecker()
        for key in self.sample_data:
            total_counter+=len(self.sample_data[key])
            for word in self.sample_data[key]:
                textblob_counter += 1 if key == str(TextBlob(word).correct()) else 0
                spellchecker_counter += 1 if key == str(spell_checker.correction(word)) else 0

        return (textblob_counter, spellchecker_counter, total_counter)

    def GetF_Score(self):
        correct_words = []
        textblob_predictions = []
        spellchecker_predictions = []
        spell_checker = SpellChecker()
        for correct_word, misspelings in self.sample_data.items():
            for misspelling in misspelings:
                correct_words.append(correct_word)
                textblob_predictions.append(str(TextBlob(misspelling).correct()))
                spellchecker_predictions.append(str(spell_checker.correction(misspelling)))

        precision = (
            precision_score(correct_words, textblob_predictions, average='micro'),
            precision_score(correct_words, spellchecker_predictions, average='micro')
        )
        recall = (
            recall_score(correct_words, textblob_predictions, average='micro'),
            recall_score(correct_words, spellchecker_predictions, average='micro')
        )
        f1 = (
            f1_score(correct_words, textblob_predictions, average='micro'),
            f1_score(correct_words, spellchecker_predictions, average='micro')
        )
        return (precision, recall, f1)