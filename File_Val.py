import parameter as p
def file_validation():
    import os.path
    if os.path.isfile(p.file_loc):
        print("File is available")
    else:
        print("File is not available in cuurent location")
file_validation()