# Filewalk

This is a Python script that checks for any unrestricted file locations where a file can be executed.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/your-username/filewalk.git
    ```

2. Navigate to the project directory:

    ```shell
    cd filewalk
    ```

## Usage

1. Open the `filewalk.py` file.

2. Modify the `source_path` and `drive_path` variables to specify the source file path and the drive path to loop through.

3. Run the script:

    ```shell
    python filewalk.py
    ```

The script will copy the source file to each directory within the specified drive path, run the binary file in each directory, and write the successful directories to the `success_directories.txt` file.

The project has a file to use for testing. this is a GOlang hello world program, the source code and a compile binary are included though if you wish to use your own binary insure it is called 'test' 


### TODO

* Add functionality to rename input file during test to look for specific file name restrictions. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
