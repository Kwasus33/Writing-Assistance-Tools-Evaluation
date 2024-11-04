import random
from textblob import TextBlob
from spellchecker import SpellChecker
from sklearn.metrics import precision_score, recall_score, f1_score



class SpellingEvaluator:
    def __init__(self, data, sample):
        self.data = data
        self.sample = sample

    def prepSample(self):
        sample_keys = random.sample(list(self.data.keys()), self.sample)
        self.sample_data = {sample_key: self.data[sample_key] for sample_key in sample_keys}

    def GetAccuracyMetric(self):
        total_counter = 0
        textblob_counter = 0
        spellchecker_counter = 0
        spell_checker = SpellChecker()
        for key in self.sample_data:
            textblob_counter += sum(1 for word in self.sample_data[key] if key == str(TextBlob(word).correct()))
            spellchecker_counter += sum(1 for word in spell_checker.unknown(self.sample_data[key]) if key == str(spell_checker.correction(word)))
            total_counter+=len(self.sample_data[key])

        return (textblob_counter, spellchecker_counter, total_counter)

    def GetF1_Score(self):
        pass
