# STL
import logging
import argparse
from typing import Set

# PDM
from gensim.models import Word2Vec

LOG = logging.getLogger(__name__)


def main(args):
    # open gold standard term list and create set of terms
    gold_standard_terms = set()
    with open(args.gold_standard, "r") as f:
        gold_standard_terms = set(line.strip() for line in f)
    print(gold_standard_terms)

    # load w2v model and get top x terms related to our chosen term
    w2v_model = Word2Vec.load(args.model)

    # compare and graph cosine similarity and f2 score between top 2 terms to find
    # cosine similarity threshold
    # TODO: Not sure what to do with this yet
    # this is supposed to be based on some sort of optimization run of
    # something? Read the paper?

    top_terms = w2v_model.wv.most_similar(positive=[args.term], topn=100)
    top_terms_set = set(
        str(term[0]) for term in top_terms
    )  # cast to `str` is just for type checking
    print(top_terms)
    print(top_terms_set)
    missing_terms = gold_standard_terms - top_terms_set
    extra_terms: Set[str] = top_terms_set - gold_standard_terms
    print(missing_terms)
    print(extra_terms)
    precision = len(top_terms_set & gold_standard_terms) / len(top_terms_set)
    recall = len(top_terms_set & gold_standard_terms) / len(gold_standard_terms)
    f1 = 0
    if (precision + recall) != 0:
        f1 = 2 * precision * recall / (precision + recall)
    print("Precision: {}".format(precision))
    print("Recall: {}".format(recall))
    print("F1: {}".format(f1))
    with open(args.output, "w") as f:
        f.write("\n".join(missing_terms))
        f.write("\n")
        f.write("\n".join(extra_terms))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default="semantic_extraction/models/w2v_model.model",
    )
    parser.add_argument(
        "-T",
        "--gold-standard",
        type=str,
        default="semantic_extraction/gold_standard.txt",
    )
    parser.add_argument("--top_terms", type=int, default=100)
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="output.txt",
    )
    parser.add_argument(
        "--cosine-similarity-threshold",
        type=float,
        default=0.5,
    )
    parser.add_argument(
        "-t",
        "--term",
        type=str,
        default="",
    )
    args = parser.parse_args()
    main(args)
