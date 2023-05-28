import os
import difflib
import filecmp
import re

def get_files(path):
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
    return files

def compare_code(project1_path, project2_path):
    project1_files = get_files(project1_path)
    project2_files = get_files(project2_path)

    for file1 in project1_files:
        file1_path = os.path.join(project1_path, file1)
        file2_path = os.path.join(project2_path, file1)

        if file1 in project2_files:
            print(f"File '{file1}' exists in both project1 and project2.")
            try:
                with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
                    content1 = file1.read()
                    content2 = file2.read()

                if filecmp.cmp(file1_path, file2_path):
                    print(f"Files '{file1_path}' and '{file2_path}' are identical.")
                else:
                    print(f"Files '{file1_path}' and '{file2_path}' are different.")

                function_similarity, variable_similarity = check_name_similarity(content1, content2)
                print(f"Function name similarity: {function_similarity * 100}%")
                print(f"Variable name similarity: {variable_similarity * 100}%")

            except UnicodeDecodeError:
                print(f"Error reading file '{file1_path}'. Encoding issue.")
            except IOError:
                print(f"Error reading file '{file1_path}'.")
        else:
            print(f"File '{file1_path}' only exists in project1.")

    for file2 in project2_files:
        if file2 not in project1_files:
            file2_path = os.path.join(project2_path, file2)
            print(f"File '{file2_path}' only exists in project2.")

def check_name_similarity(content1, content2):
    # Extract function names
    functions1 = re.findall(r'def\s+(\w+)', content1)
    functions2 = re.findall(r'def\s+(\w+)', content2)

    # Extract variable names
    variables1 = re.findall(r'\b(\w+)\b', content1)
    variables2 = re.findall(r'\b(\w+)\b', content2)

    # Compare function names
    function_similarity = difflib.SequenceMatcher(None, functions1, functions2).ratio()

    # Compare variable names
    variable_similarity = difflib.SequenceMatcher(None, variables1, variables2).ratio()

    return function_similarity, variable_similarity

project1_path = "/home/robot/all/project1"
project2_path = "/home/robot/all/project2"

compare_code(project1_path, project2_path)
