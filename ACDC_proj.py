#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

print("Current working directory:", os.getcwd())

file_path = 'Medical images/heart/database/testing/patient101/patient101_frame01_gt.nii'


# In[ ]:


import os
import gzip
import shutil


# In[ ]:


training_path = r'/home/jovyan/Medical images/heart/database/training'


# In[ ]:


training_list = os.listdir(training_path)

# Check length of patient list
print(len(training_list))

# Keep only the patients
training_list.remove('MANDATORY_CITATION.md')
print(len(training_list))


# In[ ]:


# Unzip the files in each patient folder
for patient in training_list:
    patient_path = os.path.join(training_path, patient)
    
    # Create list of files in the patient folder
    zipped_imgs = os.listdir(patient_path)
    
    # Unizp the images
    for zipped_img in zipped_imgs:
        if zipped_img.endswith('.nii.gz'):
            zipped_img_path = os.path.join(patient_path, zipped_img)
            output_img_path = zipped_img_path[:-3]

            with gzip.open(zipped_img_path, 'rb') as f_in:
                with open(output_img_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

