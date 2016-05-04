# Generate files
# import tempfile, os
#
# path = "../../resources/lab1/files"
# step = 10
# suff = 1
# for i in range(50):
#     name = tempfile.NamedTemporaryFile().name.split("/")[-1]
#     with open(path+os.sep+name, "a") as f:
#         f.write("location: dir"+str(suff))
#
#     if i+1 > suff*step:
#         suff += 1

import os, shutil

source = "../../resources/lab1/files"

for f in os.listdir(source):
    with open(source+os.sep+f, "r") as rf:
        dirname = rf.read().replace(' ', '').split(':')[1]

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    shutil.copyfile(source+os.sep+f, dirname+os.sep+f)
