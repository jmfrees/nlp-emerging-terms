# STL
import os
import argparse


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
    models_path = argv.map_dir
    filename = argv.file
    file_ext = argv.extension
    filepath = os.path.join(".", "datasets", filename + file_ext)
    model_type = argv.type  # "tfidf" or "w2v"

    data = list(CorpusReader(filepath))

    print("Creating phrase Model")
    phrase_model_path = os.path.join(models_path, f"{filename}-phrase-model.pkl")
    if not os.path.isfile(phrase_model_path):
        phrase_model = Phrases(
            data, min_count=5, threshold=1, connector_words=ENGLISH_CONNECTOR_WORDS
        )

        print("Saving phrase model")
        frozen_model = phrase_model.freeze()
        frozen_model.save(phrase_model_path)

    phrase_model = Phrases.load(phrase_model_path)

    if model_type == "tfidf":
        print("Creating TFIDF Model")
        tfidf_model_path = os.path.join(models_path, f"{filename}-tfidf-model.pkl")
        if not os.path.isfile(tfidf_model_path):
            dct = Dictionary(phrase_model[data])
            model = TfidfModel(dictionary=dct)
            model.save(tfidf_model_path)
        model = TfidfModel.load(tfidf_model_path)
    if model_type == "w2v":
        print("Creating Word2Vec Model")
        # model = Word2Vec.load(os.path.join(models_path, "g4boyz6m-prejuly4phrases.model"))
        w2v_model_path = os.path.join(models_path, f"{filename}-w2v-model.pkl")
        if not os.path.isfile(w2v_model_path):
            model = Word2Vec(
                sentences=phrase_model[data],
                vector_size=256,
                window=5,
                min_count=10,
                workers=4,
                sg=1,
            )
            # model.train(data, total_examples=len(data), epochs=1)
            print("Saving Word2Vec model")
            model.save(w2v_model_path)
        model = Word2Vec.load(w2v_model_path)


if __name__ == "__main__":
    # TODO: Add argparse
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
        default="tfidf",
        help="Model type",
    )
    parser.add_argument(
        "-m",
        "--map-dir",
        type=str,
        default=os.path.join(".", "models"),
        help="Path to models dir",
    )
    argv = parser.parse_args()
    main(argv)
