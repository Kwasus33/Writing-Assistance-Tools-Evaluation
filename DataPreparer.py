class DataPreparer:
    def __init__(self):
        self.data = {}

    def readData(self, path):
        with open(path) as fh:
            for line in fh:
                line = line.strip()
                if line.startswith('$'):
                    correct_spelling = line[1:]
                    self.data[correct_spelling] = []
                elif correct_spelling:
                    self.data[correct_spelling].append(line)

        

