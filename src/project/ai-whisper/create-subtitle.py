import whisper
import os
import subprocess


def select_file():
    # Get the list of files in the current directory
    files = [f for f in os.listdir(".") if os.path.isfile(f)]

    if not files:
        print("No files found in the current directory.")
        return None

    # Display the list of files
    print("Select a file from the following list:")
    for index, file in enumerate(files):
        print(f"{index + 1}: {file}")

    # Prompt the user to select a file
    while True:
        try:
            choice = int(input("Enter the number of the file you want to select: "))
            if 1 <= choice <= len(files):
                selected_file = files[choice - 1]
                print(f"You selected: {selected_file}")
                return selected_file
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


def convert_to_wav(selected_file):
    # Construct the output file name
    output_file = f"{os.path.splitext(selected_file)[0]}.wav"

    # Construct the ffmpeg command
    command = ["ffmpeg", "-i", selected_file, "-q:a", "0", "-map", "a", output_file]

    try:
        # Run the ffmpeg command
        subprocess.run(command, check=True)
        print(f"Conversion successful! Output file: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during conversion: {e}")


def transcribe_audio(
    audio_file, model="small", language="English", output_format="srt"
):
    """
    Transcribe audio using Whisper.

    Parameters:
    audio_file (str): Path to the audio file (e.g., 'audio.wav').
    model (str): Whisper model to use (default is 'small').
    language (str): Language of the audio (default is 'English').
    output_format (str): Output format (default is 'srt').

    Returns:
    str: Output of the command execution.
    """
    command = [
        "whisper",
        audio_file,
        "--model",
        model,
        "--language",
        language,
        "--output_format",
        output_format,
        "--task",
        "translate",
    ]
    print(command)

    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")
        return None


# Call the function to select a file
selected_file = select_file()
if selected_file:
    wav_file = ""
    wav_file = convert_to_wav(selected_file)

    transcribe_audio(wav_file, model="small", language="German")
