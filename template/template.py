import os

def structure(project_name):
    try:
        os.mkdir(project_name)
        print(f"Directory '{project_name}' created successfully.")

        directories = ['data', 'src', 'notebooks', 'docs', 'logs', 'utils']

        for directory in directories:
            directory_path = os.path.join(project_name, directory)
            os.mkdir(directory_path)
            print(f"Directory '{directory}' created inside '{project_name}'.")

        data_subdirectories = ['raw', 'processed', 'output']
        for subdirectory in data_subdirectories:
            subdirectory_path = os.path.join(project_name, 'data', subdirectory)
            os.mkdir(subdirectory_path)
            print(f"Directory '{subdirectory}' created inside '{project_name}/data'.")

        with open(os.path.join(project_name, 'config.py'), 'w') as config_file:
            config_file.write("# Configuration file")

        with open(os.path.join(project_name, 'init.py'), 'w') as init_file:
            init_file.write("# Initialization file")

        with open(os.path.join(project_name, 'log.txt'), 'w') as log_file:
            log_file.write("# Activity log")

        print("Folder structure for data engineering project created successfully!")

    except FileExistsError:
        print(f"The directory '{project_name}' already exists.")

if __name__ == "__main__":
    project_name = input("Enter the name of the data engineering project: ")
    structure(project_name)