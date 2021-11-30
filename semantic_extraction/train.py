# STL
import os
import argparse
from typing import List


def main(argv):

    # begin imports (no point in downloading if argv is incorrect)
    # PDM
    from gensim.models import Phrases, Word2Vec, TfidfModel
    from gensim.corpora import Dictionary
    from gensim.models.phrases import ENGLISH_CONNECTOR_WORDS

    # LOCAL
    from semantic_extraction.preprocess import CorpusReader

    # end imports

    print("Reading data")
    models_path = argv.model_dir
    filename = argv.file
    file_ext = argv.extension
    filepath = os.path.join("semantic_extraction", "datasets", filename + file_ext)
    retrain_model_path = argv.retrain
    model_type = argv.type  # "tfidf" or "w2v"

    data: List[List[str]] = list(CorpusReader(filepath))

    if model_type == "tfidf":
        print("Creating TFIDF Model")
        tfidf_model_path = os.path.join(models_path, f"{filename}-tfidf-model.pkl")
        if not os.path.isfile(tfidf_model_path):
            dct = Dictionary()
            # Bag_of_Words is a corpus
            Bag_of_Words = [dct.doc2bow(doc, allow_update=True) for doc in data]
            # word2id = [[(dct[id], count) for id, count in line] for line in Bag_of_Words]
            model = TfidfModel(Bag_of_Words)
            model.save(tfidf_model_path)
        model = TfidfModel.load(tfidf_model_path)
    if model_type == "w2v":
        print("Creating Word2Vec Model")
        model = Word2Vec.load(retrain_model_path) if retrain_model_path else None
        w2v_model_path = os.path.join(models_path, f"{filename}-w2v-model.model")
        if not os.path.isfile(w2v_model_path):
            if not model:
                model = Word2Vec(
                    sentences=phrase_model[data],
                    vector_size=256,
                    window=5,
                    min_count=10,
                    workers=4,
                    sg=1,
                )
            else:  # retrain
                model.build_vocab(phrase_model[data], update=True)
                model.train(
                    phrase_model[data],
                    total_examples=model.corpus_count,
                    epochs=model.epochs,
                )
            print("Saving Word2Vec model")
            model.save(w2v_model_path)
        model = Word2Vec.load(w2v_model_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Semantic-Extraction Pipeline")
    parser.add_argument("file", type=str, help="Name of dataset file in datasets dir")
    parser.add_argument(
        "-x",
        "--extension",
        type=str,
        default=".csv",
        help="Extension of the dataset file",
    )
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        choices=["tfidf", "w2v"],
        default="w2v",
        help="Model type",
    )
    parser.add_argument(
        "-m",
        "--model-dir",
        type=str,
        default=os.path.join("semantic_extraction", "models"),
        help="Path to models dir",
    )
    parser.add_argument(
        "-r",
        "--retrain",
        type=str,
        default=None,
        help="Path to model to retrain (only useful for w2v)",
    )
    argv = parser.parse_args()
    main(argv)
