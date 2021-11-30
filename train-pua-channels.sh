#!/usr/bin/env bash
pdm run python semantic_extraction/train.py pua-channels-210101-210201 -t w2v
pdm run python semantic_extraction/train.py pua-channels-210201-210301 -t w2v --retrain semantic_extraction/models/pua-channels-210101-210201-w2v-model.model 
pdm run python semantic_extraction/train.py pua-channels-210301-210401 -t w2v --retrain semantic_extraction/models/pua-channels-210201-210301-w2v-model.model 
pdm run python semantic_extraction/train.py pua-channels-210401-210501 -t w2v --retrain semantic_extraction/models/pua-channels-210301-210401-w2v-model.model 
pdm run python semantic_extraction/train.py pua-channels-210501-210601 -t w2v --retrain semantic_extraction/models/pua-channels-210401-210501-w2v-model.model 
pdm run python semantic_extraction/train.py pua-channels-210601-210701 -t w2v --retrain semantic_extraction/models/pua-channels-210501-210601-w2v-model.model 
pdm run python semantic_extraction/train.py pua-channels-210701-210801 -t w2v --retrain semantic_extraction/models/pua-channels-210601-210701-w2v-model.model 
pdm run python semantic_extraction/train.py pua-channels-210801-210901 -t w2v --retrain semantic_extraction/models/pua-channels-210701-210801-w2v-model.model 
pdm run python semantic_extraction/train.py pua-channels-210901-211001 -t w2v --retrain semantic_extraction/models/pua-channels-210801-210901-w2v-model.model 
pdm run python semantic_extraction/train.py pua-channels-211001-211101 -t w2v --retrain semantic_extraction/models/pua-channels-210901-211001-w2v-model.model 
pdm run python semantic_extraction/train.py pua-channels-211101-211201 -t w2v --retrain semantic_extraction/models/pua-channels-211001-211101-w2v-model.model 
