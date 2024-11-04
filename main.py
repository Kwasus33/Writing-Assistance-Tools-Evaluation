import DataPreparer, SpellingEvaluator, Plotter
import argparse
import os


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', type=str, required=True)
    parser.add_argument('--sample', '-s', type=int, default=50)

    return parser.parse_args()

def main():
    args = parseArgs()

    if os.path.exists(args.path):
        dataPreparer = DataPreparer.DataPreparer()
        dataPreparer.readData(args.path)
        data = dataPreparer.data

        evaluator = SpellingEvaluator.SpellingEvaluator(data, args.sample)
        evaluator.prepSample()

        textblob_counter, spellchecker_counter, total_counter = evaluator.GetAccuracy()
        (textblob_precision, spellchecker_precision), (textblob_recall, spellchecker_recall), (textblob_f1, spellchecker_f1) = evaluator.GetF_Score()

        metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
        textblob_values = [textblob_counter/total_counter, textblob_precision, textblob_recall, textblob_f1]
        spellchecker_values = [spellchecker_counter/total_counter, spellchecker_precision, spellchecker_recall, spellchecker_f1]

        plotter = Plotter.Plotter(metrics)
        plotter.plotBarChart("PySpellChecker", spellchecker_values)
        plotter.plotBarChart("TextBlob", textblob_values)



if __name__ == "__main__":
    main()