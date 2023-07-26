import os
import shutil
import json


def load_configurations():
    with open("config.json") as json_file:
        data = json.load(json_file)
        return data["target_directories"], data["custom_rules"]


def organize_files_on_desktop():
    desktop_path = os.path.expanduser("~/Desktop")

    # Load configurations from config.json
    target_directories, custom_rules = load_configurations()

    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        if os.path.isfile(file_path):
            file_suffix = os.path.splitext(filename)[1].lower()
            target_directory = target_directories.get(file_suffix, "Other")
            target_directory_path = os.path.join(
                desktop_path, target_directory)

            # Create the target directory if it doesn't exist
            if not os.path.exists(target_directory_path):
                os.makedirs(target_directory_path)

            # Check for custom categorization rules
            for keyword, rule in custom_rules.items():
                if keyword.lower() in filename.lower():
                    custom_category, custom_subcategory = rule
                    custom_directory_path = os.path.join(
                        desktop_path, custom_category, custom_subcategory)

                    # Create the custom subdirectory if it doesn't exist
                    if not os.path.exists(custom_directory_path):
                        os.makedirs(custom_directory_path)

                    target_directory_path = custom_directory_path
                    break

            # Check if the file already exists in the target directory
            if os.path.exists(os.path.join(target_directory_path, filename)):
                print(
                    f"File '{filename}' already exists in the target directory. Skipping...")
            else:
                # Move the file to the target directory
                shutil.move(file_path, os.path.join(
                    target_directory_path, filename))
                print(f"Moved '{filename}' to '{target_directory_path}'")


if __name__ == "__main__":
    organize_files_on_desktop()
