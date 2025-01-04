# Create Subtitles

Create subtitles in an srt format from an existing video file using [OpenAI Whisper](https://github.com/openai/whisper)

## Pre-requisites

- Python
- ffmpeg
- Rust tools if needed

## About Script

- Asks user to select a video file from the current working directory.
- Creates English subtitles from an existing video.

## Example using commands only instead of script

```sh
python -m virtualenv ./venv
# or uv init; uv venv

source ./venv/bin/activate

pip install -U openai-whisper
# or uv pip install -r requirements.in

# Create audio from existing video
ffmpeg -i input_video.mp4 -q:a 0 -map a audio.wav

# Create subtitle file with audio using a model
# See Whisper documentation on which model to use and with languages
whisper audio.wav --model small --language English --output_format srt
## audio.srt file will be created

```
