import argparse
import csv
import numpy as np
import collections


def get_cli_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("test_data")
    parser.add_argument("difficulties")
    return parser


def main():
    cli_args = get_cli_parser().parse_args()
    level_dict = collections.defaultdict(list)
    with open(cli_args.test_data, "r", encoding="utf-8", newline="") as fo_test, \
            open(cli_args.difficulties, "r", encoding="utf-8") as fo_diff:
        reader = csv.reader(fo_test, delimiter="\t", quotechar=None)
        for (level_str, _), score_str in zip(reader, fo_diff):
            level_dict[int(level_str)].append(float(score_str))
    sorted_items = sorted(level_dict.items(), key=lambda pair: pair[0])
    for level, scores in sorted_items:
        print("{}\t{}".format(level, np.mean(scores)))


if __name__ == "__main__":
    main()
