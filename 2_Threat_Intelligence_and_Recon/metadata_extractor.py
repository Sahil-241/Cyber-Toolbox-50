from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(file_path):
    print(f"\n--- [ Extracting Metadata for: {file_path} ] ---")
    try:
        # Sirf image files ke liye example
        image = Image.open(file_path)
        exifdata = image.getexif()

        if not exifdata:
            print("No Metadata found.")
            return

        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            print(f"{tag:25}: {data}")

    except Exception as e:
        print(f"Error: {e}. (Note: Yeh tool images ke liye best hai.)")

if __name__ == "__main__":
    # Library install karein: pip install Pillow
    path = input("File ka path enter karein: ")
    extract_metadata(path)