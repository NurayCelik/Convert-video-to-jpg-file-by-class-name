import os
import random
from pathlib import Path
import shutil

folder_paths = "images/D61_2_1-1.mp4/"

count = 1
directCount = 1
    
for f in os.listdir(folder_paths):
    Path("klasor__"+ str(directCount)+"/").mkdir(parents=True, exist_ok=True,mode=0o755)
    des = "Convert-video-to-jpg-file-by-class-name/klasor__"+ str(directCount)+"/"+str(f)
    old_path = folder_paths+str(f)
    if f.endswith('.jpg'):
            print(f)
            file_count = len([name for name in os.listdir(folder_paths) if os.path.isfile(os.path.join(folder_paths, name))])
            if count %559 != 0: ### the number of files we want to separate
              shutil.move(old_path, str(des))
            else:
              directCount +=1 
              shutil.move(old_path, str(des))
             
    if file_count<=559 & count %559 == 0:
       shutil.move(old_path, str(des))
    print("file_count")
    print(file_count)         
    count +=1
    print(count)
    print(directCount)
