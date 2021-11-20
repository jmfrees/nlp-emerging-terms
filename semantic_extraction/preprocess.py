# STL
import subprocess

# PDM
import nltk
from tqdm import tqdm
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer, sent_tokenize

nltk.download("stopwords")
nltk.download("punkt")
# all languages available:
all_available_langs = stopwords.fileids()
lang_stopwords = set()
for lang in all_available_langs:
    lang_stopwords = lang_stopwords.union(set(stopwords.words(lang)))


class CorpusReader:
    def __init__(self, filepath):
        self.fp = filepath
        self.tokenizer = TweetTokenizer()

        self.linecount = int(subprocess.check_output(["wc", "-l", filepath]).split()[0])

    def __iter__(self):
        with open(self.fp, "r", encoding="utf-8") as f:
            for line in tqdm(f, total=self.linecount):
                if not line:  # ingore blank lines
                    continue
                for s in sent_tokenize(line):
                    yield list(
                        filter(
                            lambda w: w not in lang_stopwords,
                            self.tokenizer.tokenize(s),
                        )
                    )


if __name__ == "__main__":
    filepath = "./datasets/g4boyz5m.csv"
    data = CorpusReader(filepath)
