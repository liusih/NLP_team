import csv
import pathlib
import argparse
import numpy as np
from sklearn.model_selection import train_test_split


def get_cli_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("all_tsv", type=pathlib.Path)
    parser.add_argument("output_dir", type=pathlib.Path)
    parser.add_argument("--splits", nargs="+", type=float)
    return parser


def main():
    cli_args = get_cli_parser().parse_args()
    with cli_args.all_tsv.open("r", encoding="utf-8", newline="") as fo_all:
        reader = csv.reader(fo_all, delimiter="\t", quotechar=None)
        all_data = np.array(list(reader), dtype=object)
        all_y = all_data[:, 0]
        train_num, dev_num, test_num = cli_args.splits
        train_dev_data, test_data = train_test_split(all_data, test_size=test_num / (train_num + dev_num + test_num),
                                                     stratify=all_y)
        train_dev_y = train_dev_data[:, 0]
        train_data, dev_data = train_test_split(train_dev_data, test_size=dev_num / (train_num + dev_num),
                                                stratify=train_dev_y)
        for set_name, data in zip(["train", "dev", "test"], [train_data, dev_data, test_data]):
            with (cli_args.output_dir / (set_name + ".tsv")).open("w", encoding="utf-8", newline="") as fo_out:
                writer = csv.writer(fo_out, delimiter="\t", quotechar=None)
                writer.writerows(data)


if __name__ == "__main__":
    main()
