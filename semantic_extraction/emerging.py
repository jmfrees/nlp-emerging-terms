# STL
import logging
import argparse

# PDM
from gensim.models import Word2Vec

LOG = logging.getLogger(__name__)


def get_new_terms(previous_terms, next_terms):
    new_terms = set()
    for term in next_terms:
        if term not in previous_terms:
            new_terms.add(term)
        else:
            LOG.debug(f"Term {term} already in previous model")
    return new_terms


# write emerging terms to file given set of terms
def write_emerging_terms(emerging_terms, output_file):
    LOG.info("Writing results to %s" % output_file)
    with open(output_file, "w") as f:
        for term in emerging_terms:
            f.write(term + "\n")


def main(args):
    LOG.info("Loading word2vec model from: " + args.previous_model)
    previous_model = Word2Vec.load(args.previous_model)
    LOG.info("Loading word2vec model from: " + args.next_model)
    next_model = Word2Vec.load(args.next_model)

    top_previous_terms = previous_model.wv.most_similar(
        positive=[args.term], topn=args.top_n
    )
    top_previous_terms_set = set([term[0] for term in top_previous_terms])
    LOG.debug(f"Top terms for {args.term} in previous model: {top_previous_terms}")

    top_next_terms = next_model.wv.most_similar(positive=[args.term], topn=args.top_n)
    top_next_terms_set = set([term[0] for term in top_next_terms])
    LOG.debug(f"Top terms for {args.term} in next model: {top_next_terms}")

    intersecting_terms = set(top_previous_terms).intersection(set(top_next_terms))

    LOG.debug("Intersecting terms: " + str(intersecting_terms))

    emerging_terms = get_new_terms(top_previous_terms_set, top_next_terms_set)
    LOG.info("Emerging terms: " + str(emerging_terms))

    write_emerging_terms(emerging_terms, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m1",
        "--previous-model",
        type=str,
        default="semantic_extraction/models/w2v_model.model",
    )
    parser.add_argument(
        "-m2",
        "--next-model",
        type=str,
        default="semantic_extraction/models/w2v_model.model",
    )
    parser.add_argument("--top-n", type=int, default=100)
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="emerging-terms-output.txt",
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
