import os
import shutil
import random
import numpy as np
from tqdm import tqdm

cat_train_dir = "./data/train/cat"
cat_val_dir = "./data/validation/cat"
dog_train_dir = "./data/train/dog"
dog_val_dir = "./data/validation/dog"

train_samples = 10000
val_samples = 1000

cat_train_files = []
cat_val_files = []
dog_train_files = []
dog_val_files = []
for filename in os.listdir(cat_train_dir):
    if filename.endswith(".jpg"):
        cat_train_files.append(os.path.join(cat_train_dir, filename))

for filename in os.listdir(cat_val_dir):
    if filename.endswith(".jpg"):
        cat_val_files.append(os.path.join(cat_val_dir, filename))

for filename in os.listdir(dog_train_dir):
    if filename.endswith(".jpg"):
        dog_train_files.append(os.path.join(dog_train_dir, filename))

for filename in os.listdir(dog_val_dir):
    if filename.endswith(".jpg"):
        dog_val_files.append(os.path.join(dog_val_dir, filename))

if len(cat_train_files) != train_samples:
    print("Error: Incorrect training cat samples. Expected %d, found %d" \
          %(train_samples, len(cat_train_files)))

if len(cat_val_files) != val_samples:
    print("Error: Incorrect validating cat samples. Expected %d, found %d" \
          %(val_samples, len(cat_val_files)))

if len(dog_train_files) != train_samples:
    print("Error: Incorrect training dog samples. Expected %d, found %d" \
          %(train_samples, len(dog_train_files)))

if len(dog_val_files) != val_samples:
    print("Error: Incorrect validating dog samples. Expected %d, found %d" \
          %(val_samples, len(dog_val_files)))

common_files = [filename for filename in cat_train_files if filename in cat_val_files]
if len(common_files) > 0:
    print("Error: Train and Validation set have %d common files" %len(common_files))
else:
    print("FOR CAT:\n Dataset is clean: No common files")
    print(" Training files: %d, Validation files: %s" \
          %(len(cat_train_files), len(cat_val_files)))

common_files = [filename for filename in dog_train_files if filename in dog_val_files]
if len(common_files) > 0:
    print("Error: Train and Validation set have %d common files" %len(common_files))
else:
    print("FOR DOG:\n Dataset is clean: No common files")
    print(" Training files: %d, Validation files: %s" \
          %(len(dog_train_files), len(dog_val_files)))
