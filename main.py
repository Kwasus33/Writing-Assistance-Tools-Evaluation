import DataPreparer, SpellingEvaluator
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
        # textblob_counter, spellchecker_counter, total_counter = evaluator.UseSpellCheckers()
        # print(evaluator.sample_data)
        print(evaluator.UseSpellCheckers())


if __name__ == "__main__":
    main()