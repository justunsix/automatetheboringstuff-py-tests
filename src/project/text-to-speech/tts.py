from transformers import pipeline
from datasets import load_dataset
import torch
import soundfile as sf

text_for_tts = "Hello world, Toronto, Go LEAFS!, Go! Lorem Ipsum"


def main():
    # Initialize the TTS pipeline
    synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts", device="cuda")

    # Load speaker embeddings
    embeddings_dataset = load_dataset(
        "Matthijs/cmu-arctic-xvectors", split="validation"
    )

    speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    speech = synthesiser(
        text_for_tts,
        forward_params={"speaker_embeddings": speaker_embedding},
    )

    sf.write("speech.mp3", speech["audio"], samplerate=speech["sampling_rate"])


if __name__ == "__main__":
    main()

#
