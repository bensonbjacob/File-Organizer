import os
import shutil
import json
import argparse


def load_config():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    return config


def organize_files_in_directory(directory, config, organize_subdirectories=False, original_parent=None):
    if original_parent is None:
        original_parent = directory

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            if item in config["ignore_folders"]:
                print(f"Ignoring files in the folder: {item_path}")
                continue

            if organize_subdirectories:
                organize_files_in_directory(
                    item_path, config, organize_subdirectories, original_parent)

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
    parser = argparse.ArgumentParser()
    parser.add_argument("--organize-subdirectories", action="store_true",
                        help="Organize files within subdirectories")
    args = parser.parse_args()

    desktop_path = os.path.expanduser("~/Desktop")
    downloads_path = os.path.expanduser("~/Downloads")

    config = load_config()

    print("Organizing files on Desktop...")
    organize_files_in_directory(
        desktop_path, config, args.organize_subdirectories)

    print("\nOrganizing files in Downloads...")
    organize_files_in_directory(
        downloads_path, config, args.organize_subdirectories)
