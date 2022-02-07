import os
from glob import glob

inputs_path = '/data/inputs'
outputs_path = '/data/outputs/'

zip_files = glob(os.path.join(inputs_path, '*.zip'))

if len(zip_files) > 0:
    for path in zip_files:
        import zipfile
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(outputs_path)

else:
    raise Exception('No zip files present')
