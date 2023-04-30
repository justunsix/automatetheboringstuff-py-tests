import os
import shutil
import datetime

# Path to Downloads folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# Path to to_delete folder
to_delete_folder = os.path.join(os.path.expanduser('~'), 'to_delete')

# Create to_delete folder if it doesn't exist
if not os.path.exists(to_delete_folder):
    os.makedirs(to_delete_folder)

# Get current date
now = datetime.datetime.now()

# Go through all files in Downloads folder
for filename in os.listdir(downloads_folder):
    # Get file path
    file_path = os.path.join(downloads_folder, filename)
    # Get file modification time
    file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    # Calculate difference between current date and file modification time
    diff = now - file_mtime
    # If file is older than 30 days
    if diff.days > 30:
        # Move file to to_delete folder
        shutil.move(file_path, to_delete_folder)