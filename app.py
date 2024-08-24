import os
from PIL import Image

def rename_and_convert_images(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        if "_PHOTO" in filename:
            # Split the filename and extension
            base, ext = os.path.splitext(filename)
            
            if ext.lower() in ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff']:
                # Remove the '_PHOTO' part from the filename
                new_base = base.replace("_PHOTO", "")
                new_filename = new_base + ".jpeg"
                
                # Full file paths
                old_file_path = os.path.join(input_folder, filename)
                new_file_path = os.path.join(output_folder, new_filename)
                
                # Open the image file
                with Image.open(old_file_path) as img:
                    # Convert image to RGB (JPEG format requirement)
                    rgb_img = img.convert("RGB")
                    # Save the image as JPEG
                    rgb_img.save(new_file_path, "JPEG")
                    print(f'Converted and renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    input_folder = 'input'   # Path to the input folder
    output_folder = 'output' # Path to the output folder
    rename_and_convert_images(input_folder, output_folder)
