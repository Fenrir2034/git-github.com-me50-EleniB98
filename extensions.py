import mimetypes
from pathlib import Path

def get_media_type(file_name):
    # Extract file extension and make it case-insensitive
    file_extension = Path(file_name.strip()).suffix.lower()

    # Define the supported suffixes and their corresponding MIME types
    supported_suffixes = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip',
    }

    # Get the MIME type based on the file extension
    return supported_suffixes.get(file_extension, 'application/octet-stream')

def main():
    # Prompt user for the name of the file
    file_name = input("Enter the name of the file: ")

    # Get the media type based on the file's suffix
    media_type = get_media_type(file_name)

    # Output the result
    print(f"{media_type}")

if __name__ == "__main__":
    main()
