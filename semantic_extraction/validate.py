# STL
from typing import Set

# PDM
from gensim.models import Word2Vec

# open gold standard term list and create set of terms
# load w2v model and get top x terms related to our chosen term
# compare and graph cosine similarity and f2 score between top 2 terms to find
# cosine similarity threshold

# compare top x terms to gold standard terms
# print and write out the top x terms
# if any terms are missing, print out the missing terms
# if any terms are extra, print out the extra terms
# print precision, recall, and f1 score as a table


def main():
    # open gold standard term list and create set of terms
    gold_standard_terms = set()
    with open("", "r") as f:
        gold_standard_terms = set(line.strip() for line in f)

    # load w2v model and get top x terms related to our chosen term
    w2v_model = Word2Vec.load("")

    # compare and graph cosine similarity and f2 score between top 2 terms to find
    # cosine similarity threshold
    # TODO: Not sure what to do with this yet
    # this is supposed to be based on some sort of optimization run of
    # something? Read the paper?

    # compare top x terms to gold standard terms
    # print and write out the top x terms
    # if any terms are missing, print out the missing terms
    # if any terms are extra, print out the extra terms
    # print precision, recall, and f1 score as a table
    top_terms = w2v_model.wv.most_similar(positive=[""], topn=100)
    top_terms_set = set(
        str(term[0]) for term in top_terms
    )  # cast to `str` is just for type checking
    missing_terms = gold_standard_terms - top_terms_set
    extra_terms: Set[str] = top_terms_set - gold_standard_terms
    precision = len(top_terms_set & gold_standard_terms) / len(top_terms_set)
    recall = len(top_terms_set & gold_standard_terms) / len(gold_standard_terms)
    f1 = 2 * precision * recall / (precision + recall)
    print("Precision: {}".format(precision))
    print("Recall: {}".format(recall))
    print("F1: {}".format(f1))
    with open("", "w") as f:
        f.write("\n".join(missing_terms))
        f.write("\n")
        f.write("\n".join(extra_terms))


if __name__ == "__main__":
    # TODO: Add argparse
    # get model path from argparse default to model in semantic_extraction/models
    # get gold standard path from argparse default to list in base directory
    # get top x terms from argparse default to 100
    # get output path from argparse default to output in base directory
    # get cosine similarity threshold from argparse default to 0.5?
    # get
    # TODO: Add logging

    main()
