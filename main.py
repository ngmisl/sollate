import csv

tract = "test.sol"


def main(contract):
    with open(contract, "r") as f1, open("keywords.csv", "r") as f2:
        st = csv.reader(f2, delimiter=",")
        keywords = [item[0] for item in st][1:]

        # TODO: Add Line Number
        # TODO: Add respective comment from keywords.csv to output

        for line in f1:
            for keyword in map(str.split, keywords):
                if all([key in line for key in keyword]):
                    print("Found: {}Keywords: {}".format(line, keyword))
    return


if __name__ == "__main__":
    main("{}".format(tract))
