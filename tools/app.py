import os


# Specify the path for the new folder
folder_path = 'tools'

# Check if the folder "tools" already exists
if not os.path.exists(folder_path):
    # Create the folder "tools"
    os.makedirs(folder_path)
    print(f'The folder "{folder_path}" has been created.')
else:
    print(f'The folder "{folder_path}" already exists.')
