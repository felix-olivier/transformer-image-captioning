import os
from glob import glob
from tqdm import tqdm
import torchvision.transforms.functional as F
from PIL import Image

input_dir = '/data/images/480_sample'
output_dir = '/data/images/480_sample_preprocessed'
image_paths = glob(f'{input_dir}/*.jpg')

print('Start', flush=True)
for path in tqdm(image_paths):

    image_name = os.path.basename(path)
    out_path = os.path.join(output_dir, image_name)

    try:
        with Image.open(path) as image:
            image = image.convert('RGB')
            image = F.resize(image, 256, Image.ANTIALIAS)
            image = F.center_crop(image, (224, 224))
            image.save(out_path, image.format)
    except OSError as e:
        print(e)

print('Done', flush=True)