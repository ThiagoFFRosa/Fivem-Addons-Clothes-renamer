import os

# Define the path of the root folder
root_folder_path = 'path'

# Get a list of all folders within the root folder
folders = os.listdir(root_folder_path)

# Initialize a counter
counter = 1

# Loop through each folder in the list and rename it to a three-digit numerical sequence
for folder in folders:
    # Define the new folder name with a three-digit numerical sequence
    new_name = '{0:03d}'.format(counter)
    
    # Construct the full path of the old and new folder names
    old_path = os.path.join(root_folder_path, folder)
    new_path = os.path.join(root_folder_path, new_name)
    
    # Rename the folder
    os.rename(old_path, new_path)
    
    # Increment the counter
    counter += 1
