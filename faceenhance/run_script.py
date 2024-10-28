import os
import subprocess

# Set the path for the NPZ folder npz_path = 'C:\\Users\\user\\Desktop\\ethos\\archive\\photos\\Aaron_Eckhart_0.npz'
# npz_path = 'C:\\Users\\user\\Desktop\\ethos\\archive\\photos\\Aaron_Eckhart_0.npz'
npz_folder = 'C:\\Users\\user\\Desktop\\ethos\\archive\\photos' #enter your own path

# Set the corresponding output folder
output_folder = 'C:\\Users\\user\\Desktop\\3d\\output'#enter your own path

# Define the CSV path
# csv_path = 'C:\\Users\\user\\Desktop\\ethos\\archive\\youtube_faces_with_keypoints_full.csv'
csv_path = 'C:\\Users\\user\\Desktop\\ethos\\archive\\youtube_faces_with_keypoints_full.csv'#enter your own path

# Print the base folder
base_folder = os.path.dirname(npz_folder)
print(f"Base folder set to: {base_folder}")

# Run download_photos.py
print("Running download_photos.py...")
subprocess.run(['python', 'download_photos.py', csv_path, npz_folder, output_folder], check=True)

# Run resize.py
print("Running resize.py...")
subprocess.run(['python', 'resize.py', output_folder], check=True)

# Run automate.py
print("Running automate.py...")
subprocess.run(['python', 'automate.py', output_folder], check=True)

print("Processing complete. Check the output folder for results.")
