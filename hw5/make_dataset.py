import os
import shutil
import random
import numpy as np
from tqdm import tqdm

data_dir = "./data/dataset/train"
train_dir = "./data/train"
val_dir = "./data/validation"
cat_train_dir = os.path.join(train_dir, "cat/")
dog_train_dir = os.path.join(train_dir, "dog/")
cat_val_dir = os.path.join(val_dir, "cat/")
dog_val_dir = os.path.join(val_dir, "dog/")

train_samples = 10000
val_samples = 1000

cat_files = []
dog_files = []
for filename in os.listdir(data_dir):
    if filename.endswith(".jpg"):
        if filename.startswith("cat" ):
            cat_files.append(os.path.join(data_dir, filename))
        if filename.startswith("dog"):
            dog_files.append(os.path.join(data_dir, filename))

if len(cat_files) < train_samples + val_samples:
    print("Error: Not enough dataset cat samples")

if len(dog_files) < train_samples + val_samples:
    print("Error: Not enough dataset dog samples")

random.shuffle(cat_files)
random.shuffle(dog_files)
cat_train_files = cat_files[:train_samples]
dog_train_files = dog_files[:train_samples]
cat_val_files = cat_files[-val_samples:]
dog_val_files = dog_files[-val_samples:]

# Make directories if they don't exist
if not os.path.exists(train_dir):
    os.makedirs(train_dir)

if not os.path.exists(cat_train_dir):
    os.makedirs(cat_train_dir)

if not os.path.exists(dog_train_dir):
    os.makedirs(dog_train_dir)

if not os.path.exists(val_dir):
    os.makedirs(val_dir)

if not os.path.exists(cat_val_dir):
    os.makedirs(cat_val_dir)

if not os.path.exists(dog_val_dir):
    os.makedirs(dog_val_dir)


print("Copying cat train files to %s" %cat_train_dir)
for filename in tqdm(cat_train_files):
    # print("Copying %s to %s" %(filename, train_dir))
    shutil.copy(filename, cat_train_dir)

print("Copying dog train files to %s" %dog_train_dir)
for filename in tqdm(dog_train_files):
    # print("Copying %s to %s" %(filename, train_dir))
    shutil.copy(filename, dog_train_dir)

print("Copying cat validation files %s" %cat_val_dir)
for filename in tqdm(cat_val_files):
    # print("Copying %s to %s" %(filename, train_dir))
    shutil.copy(filename, cat_val_dir)

print("Copying dog validation files %s" %dog_val_dir)
for filename in tqdm(dog_val_files):
    # print("Copying %s to %s" %(filename, train_dir))
    shutil.copy(filename, dog_val_dir)


