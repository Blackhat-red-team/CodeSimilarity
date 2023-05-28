import chardet
import difflib
import os
import re

def calculate_similarity(content1, content2):
    similarity_percentage = difflib.SequenceMatcher(None, content1, content2).ratio() * 100
    return similarity_percentage

def check_name_similarity(content1, content2):
    functions1 = re.findall(r'def\s+(\w+)', content1)
    functions2 = re.findall(r'def\s+(\w+)', content2)
    
    variables1 = re.findall(r'\b(\w+)\s*=', content1)
    variables2 = re.findall(r'\b(\w+)\s*=', content2)
    
    function_similarity = difflib.SequenceMatcher(None, functions1, functions2).ratio() * 100
    variable_similarity = difflib.SequenceMatcher(None, variables1, variables2).ratio() * 100
    
    return function_similarity, variable_similarity

def compare_code(project1_path, project2_path):
    for file1_name in os.listdir(project1_path):
        file1_path = os.path.join(project1_path, file1_name)
        file2_path = os.path.join(project2_path, file1_name)
        
        if not os.path.exists(file2_path):
            print(f"File '{file1_name}' does not exist in project2.")
            continue
        
        with open(file1_path, 'rb') as file1:
            raw_data = file1.read()
            encoding1 = chardet.detect(raw_data)['encoding']
        
        with open(file2_path, 'rb') as file2:
            raw_data = file2.read()
            encoding2 = chardet.detect(raw_data)['encoding']
        
        with open(file1_path, 'r', encoding=encoding1, errors='ignore') as file1, open(file2_path, 'r', encoding=encoding2, errors='ignore') as file2:
            content1 = file1.read()
            content2 = file2.read()
        
        similarity_percentage = calculate_similarity(content1, content2)
        function_similarity, variable_similarity = check_name_similarity(content1, content2)
        
        file2_name = file2_path.split('/')[-1]
        is_betty_style = file1_name.lower() == file2_name.lower()
        
        print(f"File '{file1_name}' exists in both project1 and project2.")
        print(f"Files '{file1_path}' and '{file2_path}' are identical.")
        print(f"Similarity Percentage: {similarity_percentage}%")
        print(f"Function Name Similarity: {function_similarity}%")
        print(f"Variable Name Similarity: {variable_similarity}%")
        if not is_betty_style:
            print(f"File '{file1_name}' does not follow the 'Betty Style'.")
        print()

# Example usage of the compare_code function
project1_path = '/home/robot/all/project1'
project2_path = '/home/robot/all/project2'

compare_code(project1_path, project2_path)
