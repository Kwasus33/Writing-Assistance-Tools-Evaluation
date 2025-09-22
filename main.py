from src import data_reader, metrics_plotter, spelling_evaluator
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True)
    parser.add_argument("--sample", "-s", type=int, default=50)

    return parser.parse_args()


def main():
    args = parse_args()

    if os.path.exists(args.path):
        reader = data_reader.DataReader()
        reader.read_data(args.path)
        data = reader.data

        evaluator = spelling_evaluator.SpellingEvaluator(data, args.sample)
        evaluator.prep_sample()

        textblob_counter, spellchecker_counter, total_counter = evaluator.get_accuracy()
        precision, recall, f1 = evaluator.get_f1()

        textblob_precision, spellchecker_precision = precision
        textblob_recall, spellchecker_recall = recall
        textblob_f1, spellchecker_f1 = f1

        metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
        textblob_values = [
            textblob_counter / total_counter,
            textblob_precision,
            textblob_recall,
            textblob_f1,
        ]
        spellchecker_values = [
            spellchecker_counter / total_counter,
            spellchecker_precision,
            spellchecker_recall,
            spellchecker_f1,
        ]

        plotter = metrics_plotter.Plotter(metrics)
        plotter.plot_bar_chart("PySpellChecker", spellchecker_values)
        plotter.plot_bar_chart("TextBlob", textblob_values)


if __name__ == "__main__":
    main()
