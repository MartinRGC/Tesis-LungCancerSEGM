# En terminal
# python -m venv lungcanc
# lungcanc\Scripts\activate
# pip install kaggle
# kaggle competitions download -c vinbigdata-chest-xray-abnormalities-detection
#
import os
os.environ['KAGGLE_CONFIG_DIR'] = os.getcwd()
os.system('kaggle competitions download -c vinbigdata-chest-xray-abnormalities-detection')