import os
import sys

# Asks the user to specify the path to the folder containing the .vtt files to be merged
folder = input('Please specify the path of the folder containing the .vtt files to be merged: ')

# Checks if the folder exists
if not os.path.isdir(folder):
    print(f'The specified folder ({folder}) does not exist or isn\'t accessible.')
    exit()

# Defines the name of the output file
output_file = input('Please specify the desired name of the output file (without .vtt): ')
output_file = output_file + '.vtt'

# Counts the number of merged files
nb_merged_files = 0

# Opens the output file in write mode
with open(output_file, 'w') as f_out:

    # Browses all files in the folder and its subfolders
    for current_directory, subdirectories, files in os.walk(folder):

        # Browses all files in the current directory
        for file in files:

            # Checks that the file is a .vtt file
            if file.endswith('.vtt') and file != output_file:

                # Opens file in read mode
                with open(os.path.join(current_directory, file), 'r') as f_in:

                    # Reads file content
                    content = f_in.read()

                    # Writes file content to output file
                    f_out.write(content)
					
					# Adds a newline after each file's content
                    f_out.write('\n')

                    # Increments the number of merged files
                    nb_merged_files += 1

# Displays a confirmation message
if nb_merged_files > 0:
    print(f'{nb_merged_files} files have been successfully merged into {output_file}.')
else:
    print(f'No .vtt files were found in the {folder} folder.')

# Waits for the user to press a key to close the console window
input('Press a key to close the window...')
