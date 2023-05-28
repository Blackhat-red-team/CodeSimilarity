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

# Function to calculate similarity ratio between two strings
def calculate_similarity_ratio(string1, string2):
    matcher = difflib.SequenceMatcher(None, string1, string2)
    return matcher.ratio()

# Function to check if variables and functions have similar names
def check_name_similarity(file1, file2):
    with open(file1, 'r', encoding='latin-1') as f1, open(file2, 'r', encoding='latin-1') as f2:
        content1 = f1.read()
        content2 = f2.read()
        # Extract function names from file1
        functions1 = re.findall(r'def\s+(\w+)', content1)
        # Extract variable names from file1
        variables1 = re.findall(r'\b(\w+)\s*=', content1)

        # Extract function names from file2
        functions2 = re.findall(r'def\s+(\w+)', content2)
        # Extract variable names from file2
        variables2 = re.findall(r'\b(\w+)\s*=', content2)

        # Compare function names
        function_similarity = calculate_similarity_ratio(' '.join(functions1), ' '.join(functions2))
        # Compare variable names
        variable_similarity = calculate_similarity_ratio(' '.join(variables1), ' '.join(variables2))

        return function_similarity, variable_similarity

# Function to check if file follows the "Betty Style"
def check_betty_style(file_path):
    with open(file_path, 'r', encoding='latin-1') as f:
        content = f.read()
        # Implement your "Betty Style" check logic here
        # Return True if the file follows the "Betty Style", False otherwise
        # Example: Checking if the file contains a specific pattern or format

        return True  # Placeholder, replace with your implementation

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
                    print(f"Files '{file1}' and '{file2}' are identical.")

                # Compare number of lines
                with open(file1_path, 'r', encoding='latin-1') as f1, open(file2_path, 'r', encoding='latin-1') as f2:
                    lines1 = len(f1.readlines())
                    lines2 = len(f2.readlines())
                    if lines1 == lines2:
                        print(f"Files '{file1}' and '{file2}' have the same number of lines.")
                    else:
                        print(f"Files '{file1}' and '{file2}' have a different number of lines.")

                # Compare file content
                if compare_function_names(file1_path, file2_path):
                    print(f"Files '{file1}' and '{file2}' have similar function names.")
                else:
                    print(f"Files '{file1}' and '{file2}' have different function names.")

                # Check if files follow the "Betty Style"
                if check_betty_style(file1_path) and check_betty_style(file2_path):
                    print(f"Files '{file1}' and '{file2}' follow the 'Betty Style'.")
                else:
                    print(f"Files '{file1}' and '{file2}' do not follow the 'Betty Style'.")

                # Check name similarity for functions and variables
                function_similarity, variable_similarity = check_name_similarity(file1_path, file2_path)
                if function_similarity == 1.0 and variable_similarity == 1.0:
                    print(f"Files '{file1}' and '{file2}' have identical function and variable names.")
                else:
                    print(f"Files '{file1}' and '{file2}' have different function and variable names.")
