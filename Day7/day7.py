class File:
    def __init__(self, name=None, size=None):
        self.name = name
        self.parentDir = None
        self.size = size
        
class Directory:
    def __init__(self, name=None, parentDir=None):
        self.name = name
        self.parentDir = parentDir
        self.childDir = {}
        self.files = {}
        self.size = 0
    
    def addDir(self, directory):
        self.childDir[directory.name] = directory
        self.size += directory.getSize()

    def getDirs(self):
        return self.childDir

    def addFile(self, file):
        self.files[file.name] = file.size
        self.size += file.size

    def getFiles(self):
        return self.files
    
    def getSize(self):
        return self.size
    
    def getItems(self):
        return self.childDir | self.files
    
    def getParentDir(self):
        return self.parentDir
        

if __name__ == '__main__':
    directory = Directory('/')
    currentDir = directory
    with open('test.txt') as file:
        for line in file:
            line = line.strip().split(" ")
            if line[1] == 'ls':
                while True:
                    line = file.readline().strip().split(" ")
                    if line[0] == '$' or line[0] == '':
                        break
                    if line[0] != 'dir':
                        currentDir.addFile(File(name=line[1], size=int(line[0]))) 
                    else:
                        currentDir.addDir(Directory(name=line[1], parentDir=currentDir))
            if line[0] == '':
                break
            if line[1] == 'cd':
                if line[2] == '/':
                    continue
                if line[2] != '..':
                    currentDir = currentDir.getDirs()[line[2]]
                else:
                    currentDir = currentDir.getParentDir()

    print(directory.getSize())
            
            