import os
import time

# Assign directory
startdir = r"./extracted_logs"

tmpDir = "./virtualun"

# bad_files = []

def iterateFile(directory):

    global tmpDir
    global startdir

    # print(os.listdir(directory))

    # Iterate over files in directory
    for name in os.listdir(directory):
        time.sleep(0.1)
        # Open file
        if os.path.isfile(directory + "/" + name):
            print("File Origi : " + directory + "/" + name)
            print("File Equiv : " + str(directory).replace("./extracted_logs", tmpDir) + "/" + name)

            
            newFile = f"{str(directory).replace(startdir, tmpDir)}/{name}"

            with open(newFile, "w") as file:
                # print(f"Created file : {tmpDir}/{tmp}/{name}")
                try: 
                    with open(f"{directory}/{name}", "r") as f:
                        print(f"Content of '{directory}/{name}'")
                        # print(f.read())
                        x = f.read()
                        file.write(x)

                except: 
                    # bad_files.append(f"{startdir}/{tmp}/{name}")
                    pass


        elif os.path.isdir(directory + "/" + name): 
            print("Directory : " + directory + "/" + name + "/")

            # only create the new dir if it doesn't already exist
            if not os.path.isdir(str(directory).replace("./extracted_logs", tmpDir) + "/" + name):
                print("Making dir: " + str(directory).replace("./extracted_logs", tmpDir) + "/" + name + "/")
                os.makedirs(str(directory).replace("./extracted_logs", tmpDir) + "/" + name)

            # Else traverse this directory to continue copying all files over    
            # don't need to traverse over the other drives - at least not yet
            if not str(name).startswith("SN:"):
                iterateFile(directory + "/" + name + "/")
        else:
            print(f"{name} is not a file or a directory")


os.system(f"rm -rf {tmpDir}")
os.makedirs(tmpDir)
iterateFile(directory=startdir)

# print(bad_files)