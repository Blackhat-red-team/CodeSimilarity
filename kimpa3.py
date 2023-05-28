import os

# Function to compare two files
def compare_files(file1, file2):
    with open(file1, 'r', encoding='latin-1') as f1, open(file2, 'r', encoding='latin-1') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        if lines1 == lines2:
            return True
        else:
            return False

# Function to compare function names
def compare_function_names(file1, file2):
    with open(file1, 'r', encoding='latin-1') as f1, open(file2, 'r', encoding='latin-1') as f2:
        content1 = f1.read()
        content2 = f2.read()
        if content1 == content2:
            return True
        else:
            return False

# Function to check name similarity
def check_name_similarity(file1, file2):
    filename1 = os.path.basename(file1)
    filename2 = os.path.basename(file2)
    if filename1 == filename2:
        return True
    else:
        return False

# Directory paths for the two projects
project1_dir = '/home/robot/all/project1'
project2_dir = '/home/robot/all/project2'

# Loop through files in project1 directory
for file1 in os.listdir(project1_dir):
    file1_path = os.path.join(project1_dir, file1)
    if os.path.isfile(file1_path):
        # Loop through files in project2 directory
        for file2 in os.listdir(project2_dir):
            file2_path = os.path.join(project2_dir, file2)
            if os.path.isfile(file2_path):
                # Check file name similarity
                if check_name_similarity(file1_path, file2_path):
                    print(f"Files '{file1}' and '{file2}' have the same name.")

                # Compare files for similarity
                if compare_files(file1_path, file2_path):
                    print(f"Files '{file1}' and '{file2}' are identical.")

                # Compare number of lines
                with open(file1_path, 'r', encoding='latin-1') as f1, open(file2_path, 'r', encoding='latin-1') as f2:
                    lines1 = len(f1.readlines())
                    lines2 = len(f2.readlines())
                    if lines1 == lines2:
                        print(f"Files '{file1}' and '{file2}' have the same number of lines.")

                # Compare file content
                if compare_function_names(file1_path, file2_path):
                    print(f"Files '{file1}' and '{file2}' have similar function names.")
