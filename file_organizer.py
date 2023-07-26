import os
import shutil
import json


def load_config():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    return config


def organize_files_in_directory(directory, config, original_parent=None):
    if original_parent is None:
        original_parent = directory

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            if item in config["ignore_folders"]:
                print(f"Ignoring files in the folder: {item_path}")
                continue

            organize_files_in_directory(item_path, config, original_parent)

        elif os.path.isfile(item_path):
            custom_category = None
            custom_subcategory = None

            for rule, target_folder in config["custom_rules"].items():
                if rule.lower() in item.lower():
                    custom_category, custom_subcategory = target_folder
                    break

            if custom_category and custom_subcategory:
                target_directory = os.path.join(
                    original_parent, custom_category, custom_subcategory)
            else:
                extension = os.path.splitext(item)[-1]
                target_directory = os.path.join(
                    original_parent, config["target_directories"].get(extension, "Other"))

            os.makedirs(target_directory, exist_ok=True)

            try:
                shutil.move(item_path, os.path.join(target_directory, item))
                print(f"Moved '{item}' to '{target_directory}'.")
            except FileNotFoundError:
                print(
                    f"Error moving '{item}' to '{target_directory}'. File not found.")


if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Desktop")
    config = load_config()
    organize_files_in_directory(desktop_path, config)
