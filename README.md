# C++ Visual Studio Solution Generator

## Overview
This Python script automates the creation of a structured project directory and generates necessary solution files using templates. It is particularly useful for developers working on C++ projects with Visual Studio.

## Features
- **Folder Structure Creation**: Automatically creates a standard directory layout for your project.
- **Solution and Project File Generation**: Generates `.sln` and `.vcxproj` files based on templates.
- **Templates**: Reads solution and project file templates from specified paths.
- **PascalCase Conversion**: Converts the project name to PascalCase format for consistent naming.
- **UUID Generation**: Generates unique GUIDs for the solution and project.
- **Example Files**: Creates example header, source, and `Main.cpp` files.

## Prerequisites
- Python 3.x

Ensure the template files are stored in the `./templates` directory relative to the script.

## Usage
1. **Clone the Repository**: Clone this repository to your local machine.

2. **Run the Script**:
   ```bash
   python generate_solution.py <solution_name>
   ```
   Replace `<solution_name>` with the desired name of your project.

## Folder Structure
The script creates the following folder structure:
```
<solution_name_pascal>/
├── include/
│   └── <solution_name_pascal>.hpp
├── src/
│   └── <solution_name_pascal>.cpp
├── tests/
├── third_party/
├── docs/
└── Main.cpp
```

## Example
### Input:
```bash
python generate_solution.py example_project
```
### Output Directory Structure:
```
ExampleProject/
├── include/
│   └── ExampleProject.hpp
├── src/
│   └── ExampleProject.cpp
├── tests/
├── third_party/
├── docs/
└── Main.cpp
```

## Customization
To customize the templates:
1. Open `solution_template.txt` or `project_template.txt`.
2. Replace or add placeholders, e.g., `{project_name}`, `{project_guid}`.
3. The script replaces these placeholders with the actual values during runtime.

## Error Handling
- If the template files are not found, the script will terminate with an error message.
- Ensure the required templates exist in the specified directory before running the script.

## Future Improvements
- Add support for additional file formats or IDEs.
- Include tests for verifying the generated files.
- Implement a configuration file for easier customization.

---
For any questions or contributions, feel free to submit an issue or pull request on the repository!