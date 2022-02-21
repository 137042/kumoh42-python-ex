class FileIO :
    def openFile(self, fileName):
        with open(fileName, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                lines[i] = line.strip()
        return lines


    def saveFile(self, fileName, list):
        with open(fileName, 'w') as f:
            for line in list:
                f.write(line + "\n")