import os
import difflib
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
    with open(file1, 'r', encoding='latin-1') as f1, open(file2, 'r', encoding='latin-1') as f2:
        content1 = f1.read()
        content2 = f2.read()
        functions1 = re.findall(r'def\s+(\w+)', content1)
        functions2 = re.findall(r'def\s+(\w+)', content2)
        variable1 = re.findall(r'\w+\s*=', content1)
        variable2 = re.findall(r'\w+\s*=', content2)
        function_similarity = difflib.SequenceMatcher(None, functions1, functions2).ratio()
        variable_similarity = difflib.SequenceMatcher(None, variable1, variable2).ratio()
        return function_similarity, variable_similarity

# Function to check Betty style similarity
def check_betty_style(file1, file2):
    with open(file1, 'r', encoding='latin-1') as f1, open(file2, 'r', encoding='latin-1') as f2:
        content1 = f1.read()
        content2 = f2.read()
        betty_style1 = re.findall(r'^\w', content1, re.MULTILINE)
        betty_style2 = re.findall(r'^\w', content2, re.MULTILINE)
        betty_style_similarity = difflib.SequenceMatcher(None, betty_style1, betty_style2).ratio()
        return betty_style_similarity

# Function to print matching results
def print_matching_results(file1, file2, similarity):
    if similarity == 1.0:
        print(f"Files '{file1}' and '{file2}' are identical.")
    else:
        print(f"Files '{file1}' and '{file2}' have similar content.")

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
                # Compare files for similarity
                if compare_files(file1_path, file2_path):
                    print_matching_results(file1, file2, 1.0)

                # Compare number of lines
                with open(file1_path, 'r', encoding='latin-1') as f1, open(file2_path, 'r', encoding='latin-1') as f2:
                    lines1 = len(f1.readlines())
                    lines2 = len(f2.readlines())
                    if lines1 == lines2:
                        print_matching_results(file1, file2, 1.0)

                # Compare file content
                if compare_function_names(file1_path, file2_path):
                    print_matching_results(file1, file2, 1.0)

                # Check name similarity
                function_similarity, variable_similarity = check_name_similarity(file1_path, file2_path)
                print(f"Function similarity between '{file1}' and '{file2}': {function_similarity}")
                print(f"Variable similarity between '{file1}' and '{file2}': {variable_similarity}")

                # Check Betty style similarity
                betty_style_similarity = check_betty_style(file1_path, file2_path)
                print(f"Betty style similarity between '{file1}' and '{file2}': {betty_style_similarity}")
