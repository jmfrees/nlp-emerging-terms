init:
	# curl dataset
	# unzip dataset
	@echo "TODO: PLEASE IMPLEMENT"
	@echo "Downloading and unzipping dataset..."
	# curl -O https://s3.amazonaws.com/text-datasets/nietzsche.txt
	@echo "Download complete."
	@echo "Unzipping dataset..."
	unzip telegram_dataset.zip -d semantic_extraction/
	@echo "Done."


train:
	# train model
	@echo "TODO: PLEASE IMPLEMENT"
	@echo "Training model..."
	bash train-pua-channels.sh
	@echo "Done."

test:
	# test model
	@echo "TODO: PLEASE IMPLEMENT"
	@echo "Testing model..."
	# python3 semantic_extraction/test.py
	@echo "Done."
