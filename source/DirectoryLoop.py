from pathlib import Path

from PIL import Image
from PIL.ExifTags import TAGS

directory_in_str='E:\DCIM'

pathlist = Path(directory_in_str).glob('**/*.jpg')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    #print(path_in_str)

    image = Image.open(path_in_str)

    exifdata = image.getexif()

    print('=================================================')
    # iterating over all EXIF data fields
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes 
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:25}: {data}")


