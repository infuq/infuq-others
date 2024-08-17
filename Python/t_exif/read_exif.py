#!/usr/bin/env python3

import exifread

'''
pip install exifread
'''



if __name__ == '__main__':
    origin_file_path = 'C:/Users/infuq/Desktop/1.jpg'

    try:
        with open(origin_file_path, "rb") as image_file:
            tags = exifread.process_file(image_file)

            for key in tags.keys():
                value = str(tags[key])
                print('{0}:{1}'.format(key, value))
    except:
        print('Error...') 