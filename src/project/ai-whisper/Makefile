SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.ONESHELL:
subtitles: ## Create subtitles from input_video
	# Create audio from existing video
	ffmpeg -i input_video.mp4 -q:a 0 -map a audio.wav
	# Create subtitle file with audio using a model
	# See Whisper documentation on which model to use and with languages
	uv run whisper audio.wav --model small --language English --output_format srt
	## audio.srt file will be created

