import os
import re
import difflib

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

# Function to check if files follow the 'Betty Style'
def check_betty_style(file):
    with open(file, 'r', encoding='latin-1') as f:
        content = f.read()
        if "Betty" in content:
            return True
        else:
            return False

# Function to calculate similarity percentage
def calculate_similarity(file1, file2):
    with open(file1, 'r', encoding='latin-1') as f1, open(file2, 'r', encoding='latin-1') as f2:
        content1 = f1.read()
        content2 = f2.read()
        similarity_ratio = difflib.SequenceMatcher(None, content1, content2).ratio()
        similarity_percentage = similarity_ratio * 100
        return similarity_percentage

# Function to compare the number of loops
def compare_loops(file1, file2):
    with open(file1, 'r', encoding='latin-1') as f1, open(file2, 'r', encoding='latin-1') as f2:
        content1 = f1.read()
        content2 = f2.read()
        loops1 = content1.count('for')
        loops2 = content2.count('for')
        if loops1 == loops2:
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
                # Compare file names
                file1_name = os.path.basename(file1_path)
                file2_name = os.path.basename(file2_path)
                if file1_name == file2_name:
                    print(f"File '{file1_name}' has the same name in project2.")

                # Compare files for similarity
                if compare_files(file1_path, file2_path):
                    print(f"Files '{file1_name}' and '{file2_name}' are identical.")
                    # Compare number of lines
                    with open(file1_path, 'r', encoding='latin-1') as f1, open(file2_path, 'r', encoding='latin-1') as f2:
                        lines1 = f1.readlines()
                        lines2 = f2.readlines()
                        if lines1 == lines2:
                            print(f"Files '{file1_name}' and '{file2_name}' have the same number of lines.")

                    # Compare function names
                    if compare_function_names(file1_path, file2_path):
                        print(f"Files '{file1_name}' and '{file2_name}' have similar function names.")

                    # Check Betty Style
                    if check_betty_style(file1_path):
                        print(f"File '{file1_name}' follows the 'Betty Style'.")
                    else:
                        print(f"File '{file1_name}' does not follow the 'Betty Style'.")

                    # Calculate similarity percentage
                    similarity_percentage = calculate_similarity(file1_path, file2_path)
                    print(f"Similarity percentage between '{file1_name}' and '{file2_name}': {similarity_percentage}%")

                    # Compare number of loops
                    if compare_loops(file1_path, file2_path):
                        print(f"Files '{file1_name}' and '{file2_name}' have the same number of loops.")

                    print()
