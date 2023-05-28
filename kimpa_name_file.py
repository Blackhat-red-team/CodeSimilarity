import os

project1_dir = '/home/robot/all/project1'
project2_dir = '/home/robot/all/project2'

# Loop through files in project1 directory
for file1 in os.listdir(project1_dir):
    file1_path = os.path.join(project1_dir, file1)
    if os.path.isfile(file1_path):
        # Check if file1 exists in project2 directory
        file2_path = os.path.join(project2_dir, file1)
        if os.path.isfile(file2_path):
            print(f"File '{file1}' exists in both project1 and project2.")
            # Perform further comparisons if needed
        else:
            print(f"File '{file1}' does not exist in project2.")
