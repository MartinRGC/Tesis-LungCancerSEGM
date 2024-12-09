# En terminal
# python -m venv lungcanc
# lungcanc\Scripts\activate
# pip install kaggle
# kaggle competitions download -c vinbigdata-chest-xray-abnormalities-detection
#
#import os
#import zipfile
#os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()
#os.system('kaggle competitions download -c vinbigdata-chest-xray-abnormalities-detection')
#zip_file_path = 'vinbigdata-chest-xray-abnormalities-detection.zip'
#extract_dir = 'vinbigdata_chest_xray'

#os.makedirs(extract_dir, exist_ok=True)

#with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#    zip_ref.extractall(extract_dir)

#print(f"Archivos descomprimidos en {extract_dir}")