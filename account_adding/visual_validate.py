import shutil
from data import instas, tiktok_account_data
import os
import time


## First remove all files
subfolder = "aaa_visual_validation"
for file in os.listdir(f'insta_screenshots/{subfolder}'):
    os.remove(f"insta_screenshots/{subfolder}/{file}")
time.sleep(2)


## Then add all files
count = 1
for i in range(len(instas)):
    orig_file = instas['Instagram Screenshot'][i]
    if instas['Instagram Result'][i] is True and len(str(orig_file)) > 6:
        orig_parts = orig_file.split('/')
        new_parts = [orig_parts[0], subfolder, f"{count}_{tiktok_account_data[instas['Tiktok username'][i]]['ig_username']}_{orig_parts[1]}"]
        
        new_file = '/'.join(new_parts)
        shutil.copy(orig_file, new_file)

        count += 1


## Then calculate the success rate so far
total = max([i for i in range(len(instas)) if instas['Instagram Result'][i] in [True, False]])+1
print('Successful: ', count, '\tTotal: ', total, '\tRatio: ', round(count/total, 2))