import os
import uuid
import sys

# Function to create folders
def create_folders(base_path, folder_list):
    for folder in folder_list:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)

# Function to create files
def create_files(base_path, solution_name_pascal, project_guid, main_guid, solution_template, project_template):

    # Write solution file
    sln_content = solution_template.format(
        project_name=solution_name_pascal, project_guid=project_guid, main_guid=main_guid
    )
    with open(os.path.join(base_path, f"{solution_name_pascal}.sln"), "w") as sln_file:
        sln_file.write(sln_content)

    # Write project file
    project_content = project_template.format(
        project_name=solution_name_pascal, project_guid=project_guid, main_file=solution_name_pascal
    )
    with open(os.path.join(base_path, f"{solution_name_pascal}.vcxproj"), "w") as vcxproj_file:
        vcxproj_file.write(project_content)
    
    # Create example header and source files
    with open(os.path.join(base_path, "include", f"{solution_name_pascal}.hpp"), "w") as header_file:
        header_file.write(f"#ifndef {solution_name_pascal.upper()}_HPP\n#define {solution_name_pascal.upper()}_HPP\n\n#endif")
    with open(os.path.join(base_path, "src", f"{solution_name_pascal}.cpp"), "w") as source_file:
        source_file.write(f'#include "{solution_name_pascal}.hpp"')
    with open(os.path.join(base_path, "./", f"Main.cpp"), "w") as source_file:
        source_file.write(f'int main() {{\n    return 0;\n}}')

def read_template(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Template file {file_path} not found!")
        sys.exit(1)

def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python generate_solution.py <solution_name>")
        sys.exit(1)
    
    solution_name = sys.argv[1]
    folders = ["include", "src", "tests", "third_party", "docs"]

    # Convert solution name to PascalCase
    solution_name_pascal = ''.join(word.capitalize() for word in solution_name.split('_'))

    # Generate a new GUID for the project
    main_guid = str(uuid.uuid4()).upper()
    project_guid = str(uuid.uuid4()).upper()

    # Read templates
    solution_template = read_template("./templates/solution_template.txt")
    project_template = read_template("./templates/project_template.txt")

    # Create base directory and populate it
    base_directory = os.path.abspath(solution_name_pascal)
    create_folders(base_directory, folders)
    create_files(base_directory, solution_name_pascal, project_guid, main_guid, solution_template, project_template)

    print(f"Project {solution_name_pascal} structure created successfully!")
    print(f"Generated Main GUID: {main_guid}")
    print(f"Generated Project GUID: {project_guid}")

if __name__ == "__main__":
    main()
