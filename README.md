# File Organizer

This is a Python script that helps you organize your files on the Desktop and Downloads folder automatically. You can customize the organization rules by editing the `config.json` file.

## Features

- Organize files on the Desktop folder based on their file types into designated subfolders.
- Optionally organize files within subdirectories on the Desktop folder.
- Organize files in the Downloads folder based on their file types into designated subfolders.
- Ignore specified folders from being organized on both the Desktop and Downloads folder.

## Configuring the Organization Rules

Before running the script, you can configure the organization rules by editing the `config.json` file. The `config.json` file contains two main sections:

1. `target_directories`: This section defines the target directories for each file type. When organizing files, the script will check the file's extension and move it to the corresponding folder. If the file type is not listed, it will be moved to the "Other" folder.

2. `custom_rules`: This section allows you to specify custom rules for organizing specific files based on keywords in their names. You can define custom categories and subcategories for better organization.

3. `ignore_folders`: This section allows you to specify a list of folders that you want to ignore when organizing files. Files within these folders will not be moved or organized.

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

## How to Use

1. Make sure you have Python installed on your system.

2. Clone this repository to your local machine using the following command:

    ```git clone https://github.com/bensonbjacob/File-Organizer.git```

3. Place the `file_organizer.py` and `config.json` files in the same directory where you want to run the organization process.

4. Open a terminal (or command prompt) and navigate to the directory containing the `file_organizer.py` and `config.json` files.

5. To organize files on the Desktop, run the following command:

    ```python file_organizer.py --desktop --sub```


      * The `--sub` argument is optional. If provided, the script will also organize files within subdirectories on the Desktop. Omit this argument if you don't want to organize subdirectories.

6. To organize files in the Downloads folder, run the following command:

    ```python file_organizer.py --downloads --sub```

      * The `--sub` argument is optional. If provided, the script will also organize files within subdirectories on the Desktop. Omit this argument if you don't want to organize subdirectories.

7. The script will automatically organize the files based on the rules defined in the `config.json` file. It will create the necessary folders and move the files accordingly.

8. After running the script, check the Desktop and Downloads folders to see the organized files.

9. If you want to change the organization rules, edit the `config.json` file accordingly and rerun the script.

10. To ignore specific folders from being organized, add the folder names to the `ignore_folders` list in the `config.json` file.

## Important Notes
* The script will move files from your desktop to appropriate directories based on the configuration provided in config.json. Make sure to review the configuration carefully to ensure it matches your requirements.

* The ```--sub``` option is optional and can be used to enable organizing files within subdirectories. If not specified, the script will only organize files in the top-level directory.

* It is recommended to create a backup of your files before running the script, especially if you are using the ```--sub``` option, to avoid unintended consequences.

* Please be cautious with the custom rules you define in the config.json file, as incorrect rules may cause files to be moved to unexpected locations.

* This script assumes you are using it on a Mac or Linux system. If you are using Windows, some modifications may be required in the script.

## License
This project is licensed under the MIT License - see the LICENSE file for details.