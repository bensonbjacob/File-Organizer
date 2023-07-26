import os
import shutil


def organize_files_on_desktop():
    desktop_path = os.path.expanduser("~/Desktop")
    target_directories = {
        ".jpeg": "Images",
        ".jpg": "Images",
        ".png": "Images",
        ".gif": "GIFs",
        ".pdf": "PDFs",
        ".docx": "Documents",
        ".pages": "Documents",
        ".xlsx": "Documents",
        ".mp4": "Videos",
        ".mov": "Videos",
        # Add more file suffixes and corresponding directories as needed
    }

 # Define custom categorization rules
    custom_rules = {
        # Files containing "resume" in their name go to 'PDFs/Resumes' directory
        "resume": ("PDFs", "Resumes"),
        # Add more custom rules as needed
    }

    # Merge the custom_rules into target_directories
    target_directories.update(custom_rules)

    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        if os.path.isfile(file_path):
            file_suffix = os.path.splitext(filename)[1].lower()
            target_directory = target_directories.get(file_suffix, "Other")
            target_directory_path = os.path.join(
                desktop_path, target_directory)

            # Check for custom categorization rules
            for keyword, rule in custom_rules.items():
                if keyword.lower() in filename.lower():
                    custom_category, custom_subcategory = rule
                    target_directory_path = os.path.join(
                        desktop_path, custom_category, custom_subcategory)
                    break

            # Create the target directory if it doesn't exist
            if not os.path.exists(target_directory_path):
                os.makedirs(target_directory_path)

            # Move the file to the target directory
            shutil.move(file_path, os.path.join(
                target_directory_path, filename))


if __name__ == "__main__":
    organize_files_on_desktop()
