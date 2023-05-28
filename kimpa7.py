import os
import re

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
    return filename1 == filename2

# Function to check Betty Style similarity
def check_betty_style(file_path):
    with open(file_path, 'r', encoding='latin-1') as f:
        content = f.read()
        if 'Betty' in content:
            return True
        else:
            return False

# Function to compare comments
def compare_comments(file1, file2):
    with open(file1, 'r', encoding='latin-1') as f1, open(file2, 'r', encoding='latin-1') as f2:
        content1 = f1.read()
        content2 = f2.read()
        comments1 = re.findall(r'#(.+)', content1)
        comments2 = re.findall(r'#(.+)', content2)
        if comments1 == comments2:
            return True
        else:
            return False

# Function to count loops
def count_loops(file_path):
    with open(file_path, 'r', encoding='latin-1') as f:
        content = f.read()
        loops = re.findall(r'for\s+\w+\s+in', content)
        return loops

# Directory paths for the two projects
project1_dir = '/home/robot/all/project1'
project2_dir = '/home/robot/all/project2'

# Loop through files in project1 directory
for file1 in os.listdir(project1_dir):
    file1_path = os.path.join(project1_dir, file1)
    if os.path.isfile(file1_path):
        # Check if file1 exists in project2 directory
        file2_name = os.path.basename(file1)
        file2_path = os.path.join(project2_dir, file2_name)
        if os.path.isfile(file2_path):
            print(f"File '{file1}' exists in both project1 and project2.")
            # Compare file names for similarity
            if check_name_similarity(file1_path, file2_path):
                print(f"File '{file1}' has the same name in project2.")

            # Compare Betty Style similarity
            if check_betty_style(file1_path) and check_betty_style(file2_path):
                print(f"Files '{file1}' and '{file2_name}' follow the 'Betty Style'.")
            else:
                print(f"Files '{file1}' and '{file2_name}' do not follow the 'Betty Style'.")

            # Compare comments
            if compare_comments(file1_path, file2_path):
                print(f"Files '{file1}' and '{file2_name}' have similar comments.")
            else:
                print(f"Files '{file1}' and '{file2_name}' have different comments.")

            # Compare number of loops
            loops1 = count_loops(file1_path)
            loops2 = count_loops(file2_path)
            if loops1 == loops2:
                print(f"Files '{file1}' and '{file2_name}' have the same number of loops.")
                if loops1:
                    print(f"Loops in file '{file1}': {', '.join(loops1)}")
            else:
                print(f"Files '{file1}' and '{file2_name}' have a different number of loops.")
                if loops1:
                    print(f"Loops in file '{file1}': {', '.join(loops1)}")
                if loops2:
                    print(f"Loops in file '{file2_name}': {', '.join(loops2)}")

        else:
            print(f"File '{file1}' does not exist in project2.")
