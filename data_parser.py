import os

import pandas as pd

# path = "data/train_256x256"
# file_list = os.listdir(path)

# for old_filename in file_list:
#     new_filename = old_filename[:old_filename.find('_')] + '.png'
    
#     old_filepath = os.path.join(path, old_filename)
#     new_filepath = os.path.join(path, new_filename)
#     os.rename(old_filepath, new_filepath)

change = pd.read_csv("data/train_lables.csv")
change["Image"] = change["Image"].apply(lambda x: x[:x.find('_')])
change.sort_values(by="Image", inplace=True, ignore_index=True)
for x in change["Image"]:
    print(x)
change.to_csv("data/train_labels.csv", index=False)

