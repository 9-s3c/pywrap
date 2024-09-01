# pywrap
This program encapsulates Python scripts within a C program, enabling them to be executed as standalone executables. It is designed to work exclusively with modules that are included with the default Python installation.

The process is as follows: A compressed, portable Python installation is encapsulated within a .tar archive. This .tar file is then converted into a .h header file. The header file is incorporated into a C program, making its data part of the compiled executable.

Before the C program is compiled, the main.py script base64-encodes the input Python script and embeds it as a string within the C file. Upon execution, the program writes the header file's data to a .tar file in the current working directory.

Subsequently, the C program extracts the portable Python installation from the .tar file and places it into a new directory. The base64-encoded string is then decoded and saved as a .py file in the same directory as the portable Python installation. Finally, the executable uses python.exe from the portable Python installation to execute the .py file.
