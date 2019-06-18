import xml.dom.minidom as dom
import os
from PIL import Image
import numpy as np
import random

def output_xml_base(img_filename, xml_filename, w, h):
    xml_filename = os.path.join(save_dir, xml_filename)
    content = '''<annotation>
    <folder>result</folder>
    <filename>%s</filename>
    <path>%s</path>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>%d</width>
        <height>%d</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>''' %(img_filename, xml_filename, w, h)
    f = open(xml_filename, 'a+')
    f.write(content)
    f.close()

def output_xml(xml_filename, obj_name, box):
    # print(box)
    xml_filename = os.path.join(save_dir, xml_filename)
    content = '''
    <object>
		<name>%s</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>%d</xmin>
			<ymin>%d</ymin>
			<xmax>%d</xmax>
			<ymax>%d</ymax>
		</bndbox>
	</object>''' %(obj_name, box[0], box[1], box[2], box[3])
    f = open(xml_filename, 'a+')
    f.write(content)
    f.close()

def output_xml_end(xml_filename):
    # print(box)
    xml_filename = os.path.join(save_dir, xml_filename)
    content = '''
</annotation>'''
    f = open(xml_filename, 'a+')
    f.write(content)
    f.close()

def fun(xml_path, save_dir, filename):
    DOMTree = dom.parse(xml_path)
    root = DOMTree.documentElement
    # image_name = root.getElementsByTagName("filename")[0]
    # image_name = image_name.firstChild.data
    basename, _ = filename.split('.')
    # image_path = os.path.join(path_dir, image_name)
    # ori_img = Image.open(image_path)
    
    img_crop_name = basename + '.jpg'
    print('basename', basename)
    img_crop_xml_filename = basename + '.xml'
    print('xml_name', img_crop_xml_filename)
    
    image_size = root.getElementsByTagName("size")[0]
    image_width = int(image_size.getElementsByTagName("width")[0].childNodes[0].data)
    image_height = int(image_size.getElementsByTagName("height")[0].childNodes[0].data)
    # print(image_width, image_height)
    # ori_img_copy = ori_img.crop([0, 0, image_width, image_height])

    output_xml_base(img_crop_name, img_crop_xml_filename, image_width, image_height)
    objects = root.getElementsByTagName("object")

    for object in objects:
        obj_name = object.getElementsByTagName("name")[0].childNodes[0].data
        obj_name = obj_name.strip()

        box = object.getElementsByTagName("bndbox")
        # print(type(box[0]))
       
        xmin = int(box[0].getElementsByTagName("xmin")[0].childNodes[0].data)
        ymin = int(box[0].getElementsByTagName("ymin")[0].childNodes[0].data)
        xmax = int(box[0].getElementsByTagName("xmax")[0].childNodes[0].data)
        ymax = int(box[0].getElementsByTagName("ymax")[0].childNodes[0].data)

        box = (xmin, ymin, xmax, ymax)
        # img_crop = ori_img.crop(box)
        
        # img_crop_savepath = os.path.join(save_dir, img_crop_name)
        # img_crop.save(img_crop_savepath)
        
        output_xml(img_crop_xml_filename, obj_name, box)

    output_xml_end(img_crop_xml_filename)   
            
if __name__ == '__main__':
    
    path_dir = 'C:\\Users\\ssss\\Documents\\data_use\\02\\ups_all'
    save_dir = 'C:\\Users\\ssss\\Documents\\data_use\\02\\ups_final'

    for filename in os.listdir(path_dir):
        if os.path.splitext(filename)[1] == ".xml":   # 筛选csv文件
            print(filename)
            file_path = os.path.join(path_dir, filename)
            fun(file_path, save_dir, filename)
    print('Done!')
