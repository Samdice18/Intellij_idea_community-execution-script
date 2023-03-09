import subprocess
import os
import sys

#finds the IDE path and returns it
IDEA_PATH = subprocess.run(['which', 'intellij-idea-community'], capture_output=True, text=True).stdout.strip()
CURRENT_DIRECTORY = os.getcwd()


def open_new_ide_window():
    # hides any print while opening the IDE
    subprocess.Popen([f"{IDEA_PATH}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def open_folder_in_ide(arg):
    # hides any print while opening the IDE
    subprocess.Popen([f"{IDEA_PATH}", f"{arg}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            open_new_ide_window()

        elif len(sys.argv) == 2:
            if sys.argv[1] == ".":
                open_folder_in_ide(CURRENT_DIRECTORY)

            elif os.path.exists(sys.argv[1]):
                open_folder_in_ide(sys.argv[1])
            else:
                print(f"{sys.argv[1]} folder does not exist")
        
        else:
            print("No argument is required...")
    except:
        """failed to execute application

probably due to one of the following reasons:
- Application is not installed
- Application was not installed using snap, the the following command
    # sudo snap install intellij-idea-community.       
"""

    
    