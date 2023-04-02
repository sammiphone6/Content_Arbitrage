import shutil
from data import instas, tiktok_account_data

count = 1
for i in range(len(instas)):
    
    orig_file = instas['Screenshot'][i]

    if instas['Result'][i] == 'TRUE' and len(orig_file) > 6:
        orig_parts = orig_file.split('/')
        new_parts = [orig_parts[0], "visual_validation", f"{count}_{tiktok_account_data[instas['Tiktok username'][i]]['ig_username']}_{orig_parts[1]}"]
        
        new_file = '/'.join(new_parts)
        shutil.copy(orig_file, new_file)

        count += 1