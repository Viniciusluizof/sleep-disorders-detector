# %%

import kaggle
import shutil
import zipfile
import os

api = kaggle.KaggleApi()
api.authenticate()


api = kaggle.KaggleApi()
api.authenticate()

api.dataset_download_files(
    dataset="orvile/health-and-sleep-relation-2024",
    path="data",
    unzip=True
)
print(os.listdir("data"))
