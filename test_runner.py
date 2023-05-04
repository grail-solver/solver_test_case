import os
import json
from xtractor.core.helper import grail_extractor
from solver.solver import solve

def run_test():
    test_folder_path = 'case'
    for folder_name in os.listdir(test_folder_path):
        folder_path = os.path.join(test_folder_path, folder_name)
        if os.path.isdir(folder_path):
            # For each problem file
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.txt'):
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'r') as file:
                        text = file.read()

                    # Extract relevant data from the text
                    print(folder_path, ':Launch request')
                    result = grail_extractor(text)
                    print(folder_path, ':Launch done')

                    # Save text output in file
                    result_file_path = os.path.join(folder_path, 'result.json')
                    with open(result_file_path, 'w') as result_file:
                        json.dump(result, result_file)

                    # Save solution in file
                    if result['llm_status'] == 'success':
                        solution = solve(result['variables'], result['constraints'], [])
                        solution_file_path = os.path.join(folder_path, 'solution.json')
                        with open(solution_file_path, 'w') as solution_file:
                            json.dump(solution, solution_file)



def run_specific_test(folder: str):
    folder_path = os.path.join('case', folder)
    if os.path.isdir(folder_path):
            # For each problem file
            for file_name in os.listdir(folder_path):
                if file_name.endswith('problem.txt'):
                    file_path = os.path.join(folder_path, file_name)
                    with open(file_path, 'r') as file:
                        text = file.read()

                    # Extract relevant data from the text
                    print(folder, ':Launch request')
                    result = grail_extractor(text)
                    print(folder, ':Launch done')

                    print("TEST: SEE OUTPUT IN RESULT.TXT FILE")

                    # Save text output in file
                    result_file_path = os.path.join(folder_path, 'result.json')
                    with open(result_file_path, 'w') as result_file:
                        json.dump(result, result_file)

                    if result['llm_status'] == 'success':
                        solution = solve(result['variables'], result['constraints'], [])
                        solution_file_path = os.path.join(folder_path, 'solution.json')
                        with open(solution_file_path, 'w') as solution_file:
                            json.dump(solution, solution_file)


if __name__ == '__main__':
    # run_test()
    run_specific_test('case_38_sudoku')