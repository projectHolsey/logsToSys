import os
import time

# Assign directory
startdir = r"./extracted_logs"

tmpDir = "./tmpdir"

def iterateFile(directory):

    global tmpDir

    # Iterate over files in directory
    for name in os.listdir(directory):
        # time.sleep(0.5)
        # Open file
        if os.path.isfile(directory + "/" + name):
            tmp = str(directory).replace("./extracted_logs","")
            # os.system(f"touch {os.path.join(tmpDir, tmp, name)}")

            newFile = f"{tmpDir}{tmp}/{name}"

            with open(newFile, "w") as file:
                print(f"Created file : {tmpDir}/{tmp}/{name}")
                with open(f"{tmpDir}/{tmp}/{name}", "r") as f:
                    print(f"Content of '{name}'")
                    file.write(f.read())

        elif os.path.isdir(directory + "/" + name): 
            print(f"{name} is a directory")
            print(directory + "/" + name + "/")
            print(tmpDir + "/" + str(directory).replace("./extracted_logs", "") + "/" + name)
            os.makedirs(tmpDir + "/" + str(directory).replace("./extracted_logs", "") + "/" + name)
            iterateFile(directory + "/" + name + "/")
        else:
            print(f"{name} is not a file or a directory")


os.system(f"rm -rf {tmpDir}")
os.makedirs(tmpDir)
iterateFile(directory=startdir)