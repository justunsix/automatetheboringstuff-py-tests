SHELL := /bin/bash

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.ONESHELL:
subtitles: ## Create subtitles from input_video
	# Create audio from existing video
	ffmpeg -i input_video.mp4 -q:a 0 -map a audio.wav
	# Create subtitle file with audio using a model medium, source language is Spanish and translate
	# to English subtitle file
	# See Whisper documentation on which model to use and with languages
	# model examples: tiny, small, turbo (default), large; note use medium or large for best translation
	# audio.srt file will be created
	uv run whisper audio.wav --model medium --language Spanish --task translate --output_format srt

