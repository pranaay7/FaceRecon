import os
import subprocess

# Define paths"C:\Users\user\Desktop\3d\NextFace\top 50 enhanced output"
#C:\Users\user\Desktop\3d\photos_out_enhanced
input_dir = "C:\\Users\\user\\Desktop\\3d\\photos_out_enhanced" #enter your own path
output_dir = "C:\\Users\\user\\Desktop\\3d\\NextFace\\OUTPUT"  # Folder to save optimized images#enter your own path

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get list of all image files in the directory
image_files = [f for f in os.listdir(input_dir) if f.endswith('.png')]

# Loop through each image and run the command
for image_file in image_files:
    input_image_path = os.path.join(input_dir, image_file)
    
    # Create output path for the optimized image with '_3d' appended
    file_name, file_extension = os.path.splitext(image_file)
    output_image_path = os.path.join(output_dir, f'{file_name}_3d{file_extension}')
    
    # Run the optimizer command
    command = f'python optimizer.py --input "{input_image_path}" --output "{output_image_path}"'
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f'Optimized {image_file} successfully as {output_image_path}.')
    except subprocess.CalledProcessError as e:
        print(f'Error optimizing {image_file}: {e}')