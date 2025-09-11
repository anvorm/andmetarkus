class FileFunctions:

    def add_line_to_file(self, file_path, line):
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(line + "\n")

    def read_file(self, file_path): # loeb faili read ja tagastab listina
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
        
    # Add this to your file_functions.py

""" class FileFunctions:
    # ...existing code...

    def get_last_n_lines(self, file_path, n=3):
        with open(file_path, encoding="utf-8") as f:
            lines = f.readlines()
        return [line.rstrip('\n') for line in lines[-n:]] """