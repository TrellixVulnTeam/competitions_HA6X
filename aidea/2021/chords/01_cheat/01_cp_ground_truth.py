"""
pd.read_csv("CE200/1/ground_truth.txt", header=None, delimiter="\t")
# df.values is ndarray and ndarray is not serializable (thus cannot be an element of json)
df.values.tolist()

"""

import json
import pandas as pd
import os

D = dict()

train_dir = "/home/phunc20/datasets/aidea/2021-01-09-和絃辨識/CE200/"
for thing in os.listdir(train_dir):
    subdir = os.path.join(train_dir, thing)
    if os.path.isfile(subdir):
        continue
    gt_file = os.path.join(subdir, "ground_truth.txt")
    df = pd.read_csv(gt_file, header=None, delimiter="\t")
    # df.values is ndarray and ndarray is not serializable (thus cannot be an element of json)
    D[thing] = df.values.tolist()

#json.dump(D, fp="cheat.json")
with open("cheat.json", 'w') as f:
    json.dump(D, fp=f)



