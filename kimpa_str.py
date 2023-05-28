import filecmp
import difflib
import ast
import re

def compare_values(file1_path, file2_path):
    with open(file1_path, 'r', encoding='latin-1') as file1, open(file2_path, 'r', encoding='latin-1') as file2:
        content1 = file1.read()
        content2 = file2.read()

    # Compare values
    return content1 == content2

def compare_variables(file1_path, file2_path):
    with open(file1_path, 'r', encoding='latin-1') as file1, open(file2_path, 'r', encoding='latin-1') as file2:
        content1 = file1.read()
        content2 = file2.read()

    # Extract variable names
    variables1 = re.findall(r'\b(\w+)\b', content1)
    variables2 = re.findall(r'\b(\w+)\b', content2)

    # Compare variable names
    return variables1 == variables2

def compare_code(project1_path, project2_path):
    project1_files = get_files(project1_path)
    project2_files = get_files(project2_path)

    for file1 in project1_files:
        file1_path = project1_path + file1
        file2_path = project2_path + file1

        if file1 in project2_files:
            print(f"File '{file1}' exists in both project1 and project2.")
            if filecmp.cmp(file1_path, file2_path):
                print(f"Files '{file1}' and '{file1}' are identical.")
            else:
                print(f"Files '{file1}' and '{file1}' are different.")

            if compare_values(file1_path, file2_path):
                print(f"Values in files '{file1}' and '{file1}' are the same.")
            else:
                print(f"Values in files '{file1}' and '{file1}' are different.")

            if compare_variables(file1_path, file2_path):
                print(f"Variable names in files '{file1}' and '{file1}' are the same.")
            else:
                print(f"Variable names in files '{file1}' and '{file1}' are different.")
                
        else:
            print(f"File '{file1}' only exists in project1.")
    
    for file2 in project2_files:
        if file2 not in project1_files:
            print(f"File '{file2}' only exists in project2.")

def get_files(directory):
    import os
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Usage example
project1_path = '/home/robot/all/project1/'
project2_path = '/home/robot/all/project2/'
compare_code(project1_path, project2_path)
