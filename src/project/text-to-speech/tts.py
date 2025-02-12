from transformers import (
    SpeechT5Processor,
    SpeechT5ForTextToSpeech,
    SpeechT5HifiGan,
)
from datasets import load_dataset
import torch
import soundfile as sf
from pydub import AudioSegment

# Read text that will be converted to speech from a file
# with open("input.txt", "r") as file:
#     text_for_tts = file.read()

text_for_tts = """Centuries ago, in a small village of Kaladi in Kerala, a prodigious boy named Adi Shankaracharya was born. From a young age, he showed remarkable wisdom and a deep desire for spiritual knowledge."""


# Function to split text into smaller chunks
def split_text(text, max_length=200):
    sentences = text.split(".")
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
        if current_chunk:
            chunks.append(current_chunk.strip())
    return chunks


def main():
    # Load speaker embeddings
    embeddings_dataset = load_dataset(
        "Matthijs/cmu-arctic-xvectors", split="validation"
    )

    speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    # Split the text into manageable chunks
    text_chunks = split_text(text_for_tts, max_length=200)
    # Debugging: Print the chunks
    print(f"Total Chunks: {len(text_chunks)}")
    for i, chunk in enumerate(text_chunks):
        print(f"Chunk {i + 1}: {chunk}")

    # Load models and vocoder
    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

    # Generate speech for each chunk
    speech_outputs = []
    for idx, chunk in enumerate(text_chunks):
        print(f"Processing chunk {idx + 1}/{len(text_chunks)}: {chunk}")
        inputs = processor(text=chunk.strip(), return_tensors="pt")
        speech = model.generate_speech(
            inputs["input_ids"], speaker_embedding, vocoder=vocoder
        )

        # Save individual chunk audio
        speech_outputs.append(speech.numpy())

    sf.write(f"chunk_{idx}.wav", speech.numpy(), samplerate=16000)

    # Combine all audio chunks into one file
    combined_audio = AudioSegment.empty()
    for idx in range(len(text_chunks)):
        audio_chunk = AudioSegment.from_file(f"chunk_{idx}.wav")
        combined_audio += audio_chunk
    # Export the combined audio
    combined_audio.export("final_speech.wav", format="wav")
    print("Full speech has been saved as 'final_speech.wav'")


if __name__ == "__main__":
    main()

#
