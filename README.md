# File Organizer Script

This repository contains a Python script that helps you organize files on your desktop automatically. It sorts files based on their file types into designated directories. Additionally, you can choose to organize files within subdirectories or only in the top-level directory.

## Features

1. Organize files based on their file types: The script categorizes files into different directories based on their file extensions, such as images, documents, videos, etc.

2. Custom Rules: You can define custom rules in the `config.json` file to specify additional categorization for specific file names. For example, you can create rules to move files containing specific keywords into a separate folder.

3. Organize Files Within Subdirectories (Optional): The script can be run with the `--organize-sub` command-line argument to enable organizing files within subdirectories.

## How to Use

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

```git clone https://github.com/bensonbjacob/File-Organizer.git```


2. **Configuration**

The `config.json` file contains the configuration settings for the file organizer script. It defines target directories for different file extensions and allows you to create custom rules for additional categorization. Modify the `config.json` file to customize the behavior of the file organizer script as per your requirements.

Example `config.json`:

```json
{
  "target_directories": {
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
    ".zip": "Archives"
  },
  "custom_rules": {
    "resume": ["Documents", "Resumes"],
    "screenshot": ["Images", "Screenshots"]
  },
  "ignore_folders": ["web_dev"]
}
```

3. **Running the Script**

    Open a terminal (command prompt) and navigate to the directory containing the file_organizer.py script.

    To organize files only in the top-level directory:

    ```python file_organizer.py```

    To organize files within subdirectories:

    ```python file_organizer.py --organize-sub```

    The script will automatically categorize and move files based on their types and any custom rules defined in the config.json file.

## Important Notes
* The script will move files from your desktop to appropriate directories based on the configuration provided in config.json. Make sure to review the configuration carefully to ensure it matches your requirements.

* The ```--organize-sub``` option is optional and can be used to enable organizing files within subdirectories. If not specified, the script will only organize files in the top-level directory.

* It is recommended to create a backup of your files before running the script, especially if you are using the ```--organize-sub``` option, to avoid unintended consequences.

* Please be cautious with the custom rules you define in the config.json file, as incorrect rules may cause files to be moved to unexpected locations.

* This script assumes you are using it on a Mac or Linux system. If you are using Windows, some modifications may be required in the script.

## License
This project is licensed under the MIT License - see the LICENSE file for details.