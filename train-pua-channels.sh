#!/usr/bin/env bash
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-210101-210201.csv -t w2v
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-210201-210301.csv -t w2v --retrain semantic_extraction/models/pua-channels-210101-210201-w2v-model.model 
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-210301-210401.csv -t w2v --retrain semantic_extraction/models/pua-channels-210201-210301-w2v-model.model 
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-210401-210501.csv -t w2v --retrain semantic_extraction/models/pua-channels-210301-210401-w2v-model.model 
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-210501-210601.csv -t w2v --retrain semantic_extraction/models/pua-channels-210401-210501-w2v-model.model 
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-210601-210701.csv -t w2v --retrain semantic_extraction/models/pua-channels-210501-210601-w2v-model.model 
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-210701-210801.csv -t w2v --retrain semantic_extraction/models/pua-channels-210601-210701-w2v-model.model 
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-210801-210901.csv -t w2v --retrain semantic_extraction/models/pua-channels-210701-210801-w2v-model.model 
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-210901-211001.csv -t w2v --retrain semantic_extraction/models/pua-channels-210801-210901-w2v-model.model 
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-211001-211101.csv -t w2v --retrain semantic_extraction/models/pua-channels-210901-211001-w2v-model.model 
pdm run python semantic_extraction/train.py semantic_extraction/datasets/pua-channels-211101-211201.csv -t w2v --retrain semantic_extraction/models/pua-channels-211001-211101-w2v-model.model 
