def getPath():
    import os
    return os.environ['HOME']
    #return os.path.expanduser('~')

if __name__ == "__main__":
    print(getPath())