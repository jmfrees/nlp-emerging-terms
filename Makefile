download:
	@echo "Downloading and unzipping dataset..."
	curl -L -o telegram_dataset.zip https://lab-bucket-for-uab.s3.amazonaws.com/telegram_dataset.zip
	@echo "Download complete."
	@echo "Unzipping dataset..."
	unzip telegram_dataset.zip -d semantic_extraction/


install:
	@echo "Installing dependencies..."
	pdm sync --prod
	@echo "Done."

init: download install


train:
	@echo "Training model..."
	bash train-pua-channels.sh
	@echo "Done."

validate:
	@echo "Testing model..."
	pdm run python semantic_extraction/validate.py --model semantic_extraction/models/pua-channels-all-w2v-model.model -T fraud_terms -t pua --top-n 200
	@echo "Done."

test-emerging:
	@echo "Testing model..."
	pdm run python semantic_extraction/emerging.py -m1 semantic_extraction/models/pua-channels-210701-210801-w2v-model.model -m2 semantic_extraction/models/pua-channels-210901-211001-w2v-model.model -t pua
	@echo "Done."
