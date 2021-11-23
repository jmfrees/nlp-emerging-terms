# STL
import os

# PDM
from gensim.models import Phrases, Word2Vec, TfidfModel
from gensim.corpora import Dictionary
from gensim.models.phrases import ENGLISH_CONNECTOR_WORDS

# LOCAL
from semantic_extraction.preprocess import CorpusReader


def main():
    print("Reading data")
    models_path = os.path.join(".", "models")
    filename = "g4boyz5m"
    file_ext = ".csv"
    filepath = os.path.join(".", "datasets", filename + file_ext)
    model_type = "tfidf"  # "tfidf" or "w2v"

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
    main()
