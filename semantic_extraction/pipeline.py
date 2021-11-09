# STL
import os

# PDM
from gensim.models import Word2Vec
from gensim.models.phrases import ENGLISH_CONNECTOR_WORDS, Phrases

# LOCAL
from semantic_extraction.preprocess import CorpusReader


def main():
    print("Reading data")
    models_path = os.path.join(".", "models")
    filename = "g4boyz6m-1day"
    file_ext = ".csv"
    filepath = os.path.join(".", "datasets", filename + file_ext)

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

    print("Creating Word2Vec model")
    model = Word2Vec.load(os.path.join(models_path, "g4boyz6m-prejuly4phrases.model"))
    wv_model_path = os.path.join(models_path, f"{filename}phrases.model")
    if not os.path.isfile(wv_model_path):
        # model = Word2Vec(
        #     sentences=phrase_model[data],
        #     vector_size=256,
        #     window=5,
        #     min_count=10,
        #     workers=4,
        # )
        model.train(data, total_examples=len(data), epochs=1)
        print("Saving Word2Vec model")
        model.save(wv_model_path)


if __name__ == "__main__":
    main()
