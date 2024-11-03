import random

class SpellingEvaluator:
    def __init__(self, data, sample):
        self.data = data
        self.sample = sample

    def prepSample(self):
        sample_keys = random.sample(list(self.data.keys()), self.sample)
        self.sample_data = {sample_key: self.data[sample_key] for sample_key in sample_keys}

    def UseSpellChecker(self):
        pass