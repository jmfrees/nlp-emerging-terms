download:
	@echo "TODO: Finish this"
	@echo "Downloading and unzipping dataset..."
	# curl -O https://s3.amazonaws.com/text-datasets/nietzsche.txt
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
	pdm run python semantic_extraction/validate.py --model semantic_extraction/models/pua-channels-all-w2v-model.model -T fraud_terms -t pua
	@echo "Done."
