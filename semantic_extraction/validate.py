# STL
import json
import logging
import argparse
from typing import Set, Iterable

# PDM
from gensim.models import Word2Vec

LOG = logging.getLogger(__name__)


def write_results(
    fp: str,
    missing_terms: Iterable[str],
    extra_terms: Iterable[str],
    precision: float,
    recall: float,
    f1: float,
):
    # make dictionary of results
    results = {
        "missing_terms": list(missing_terms),
        "extra_terms": list(extra_terms),
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }
    # write results to file as json
    with open(fp, "w") as f:
        json.dump(results, f)


def main(args):
    # open gold standard term list and create set of terms
    gold_standard_terms = set()
    with open(args.gold_standard, "r") as f:
        gold_standard_terms = set(line.strip() for line in f)
    LOG.debug("Gold standard terms: %s" % gold_standard_terms)

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
    LOG.debug("Top terms: %s" % top_terms)
    LOG.debug("Top Terms set: %s" % top_terms_set)
    missing_terms = gold_standard_terms - top_terms_set
    extra_terms: Set[str] = top_terms_set - gold_standard_terms
    LOG.debug("Missing terms: %s" % missing_terms)
    LOG.debug("Extra terms: %s" % extra_terms)
    precision = len(top_terms_set & gold_standard_terms) / len(top_terms_set)
    recall = len(top_terms_set & gold_standard_terms) / len(gold_standard_terms)
    f1 = 0
    if (precision + recall) != 0:
        f1 = 2 * precision * recall / (precision + recall)
    LOG.info("Precision: {}".format(precision))
    LOG.info("Recall: {}".format(recall))
    LOG.info("F1: {}".format(f1))
    write_results(args.output, missing_terms, extra_terms, precision, recall, f1)


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
    parser.add_argument(
        "-l",
        "--log",
        dest="log_level",
        default="INFO",
        type=str.upper,
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help=("NOTSET, DEBUG, INFO, WARNING, ERROR, or CRITICAL (default=INFO)"),
        metavar="LVL",
    )
    args = parser.parse_args()

    logging.basicConfig(
        format="[%(asctime)s] [%(filename)22s:%(lineno)-4s] [%(levelname)8s]   %(message)s",
        level=logging.getLevelName(args.log_level),
    )
    main(args)
