# Semantic Extraction

## Requirements

Execution of this project requires the use of the Python Development Master
([pdm](https://github.com/pdm-project/pdm)).
Please install `pdm` before continuing. See installation instructions [here](https://pdm.fming.dev/#installation).

## Running the code

Running the code is as simple as running some [make commands](#make-targets)

1. `$ make init`
2. You can now run any of the `train`, `validate`, or `test-emerging` targets

Training will take some time. But you can run the first couple of training
iterations if you would like to test that.

`validate` and `test-emerging` will work right away because of the inclusion
of the pre-trained models.

## Make targets

Most of the major methods of execution are covered by targets within a `Makefile`.

- `make download`: Download datasets and trained models
- `make install`: Install dependencies with `pdm`
- `make init`: Run `download` and `install` targets
- `make train`: Train month-to-month word2vec models
- `make validate`: Run validation script on all channels trained model
- `make test-emerging`: Test emerging terms script between two models

All scripts can be run with `pdm run python <script.py> --help` to see options
for running.

---

#### NOTE: training on the full dataset consumed over 110 GB of ram. And took 7+ hours

---

### Authors: Jonathan Frees (jmfrees@uab.edu), Jan Foksinski (jkf@uab.edu)
