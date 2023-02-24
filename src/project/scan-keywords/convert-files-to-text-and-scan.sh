# Using pandoc, convert all files in a directory to text files
# Usage: convert-files-to-text.sh <directory> <output-directory>
# Example: convert-files-to-text.sh .\input .\output
# Note: This script will create the output directory if it does not exist

# Check that the input directory exists
if [ ! -d "$1" ]; then
    echo "Input directory does not exist"
    exit 1
fi

# Check that the output directory exists
if [ ! -d "$2" ]; then
    echo "Output directory does not exist"
    echo "Creating output directory"
    mkdir "$2"
fi

# Create a list of all files in the input directory
files=$(ls "$1")

# Convert each file in the input directory to a text file
for file in $files
do
    echo "Converting $file to text"
    pandoc "$1/$file" -o "$2/$file.txt"
done

# Using keywords.txt location and output directory, scan all text files for keywords
python3 scan-keywords.py "examples/keywords.txt" "$2"