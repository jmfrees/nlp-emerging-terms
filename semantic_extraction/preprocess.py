# PDM
import nltk
from tqdm import tqdm
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer, sent_tokenize

nltk.download("stopwords")
nltk.download("punkt")
# TODO: This currently only cares about english stopwords
eng_stopwords = set(stopwords.words("english"))


class CorpusReader:
    def __init__(self, filepath):
        self.fp = filepath
        self.tokenizer = TweetTokenizer()

    def __iter__(self):
        with open(self.fp, "r", encoding="utf-8") as f:
            for line in tqdm(f):
                if not line:  # ingore blank lines
                    continue
                for s in sent_tokenize(line):
                    yield from filter(
                        lambda w: w not in eng_stopwords,
                        self.tokenizer.tokenize(s),
                    )


if __name__ == "__main__":
    filepath = "./datasets/g4boyz5m.csv"
    data = CorpusReader(filepath)
