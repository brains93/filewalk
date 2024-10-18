
import os
import shutil
import subprocess


def copy_file(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print(f"File copied from {source_path} to {destination_path}")
    except:
        print(f"Error copying file:")
        pass
       
     


def run_binary(binary_path, *args):
    try:
        result = subprocess.run([binary_path, *args], check=True, capture_output=True, text=True)
        print(f"Output:\n{result.stdout}")
        print(f"Errors:\n{result.stderr}")
        if result.returncode == 0:
            write_file(binary_path)   
            print(f"Binary ran successfully")

    except:
        print(f"Error running binary:")
        pass




def loop_through_directories(drive_path):
    for root, dirs, files in os.walk(drive_path):
        print(f"Current directory: {root}")
        for dir_name in dirs:
            copy_file(source_path, os.path.join(root, dir_name))
            try:
                run_binary(os.path.join(root, dir_name, 'test'))
                if os.path.join(root, dir_name, 'test') != source_path:
                    os.remove(os.path.join(root, dir_name, 'test'))   
            except:
                pass
       

def write_file(success_dir):
    with open('success_directories.txt', 'a') as file:
        file.write(success_dir + '\n')


source_path = 'SOURCEPATH/test'
drive_path = 'ROUTEPATH'

loop_through_directories(drive_path)
