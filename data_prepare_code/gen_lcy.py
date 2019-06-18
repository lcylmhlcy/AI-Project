import xml.dom.minidom as dom
import os
from PIL import Image
import numpy as np
import random

def img_transform(img):
    img_v = np.flip(img, axis = 0)
    img_v = Image.fromarray(img_v)
    img_h = np.flip(img, axis = 1)
    img_h = Image.fromarray(img_h)
    img_hv = np.flip(img_v, axis = 1)
    img_hv = Image.fromarray(img_hv)
    # print(type(img_v))    
    return img_v, img_h, img_hv

def output_xml(img_filename, xml_filename, w, h, box, x, y):
    # print(box)
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
	<segmented>0</segmented>
	<object>
		<name>qitijianceyi</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>%d</xmin>
			<ymin>%d</ymin>
			<xmax>%d</xmax>
			<ymax>%d</ymax>
		</bndbox>
	</object>
    </annotation>''' %(img_filename, xml_filename, w, h, x, y, x+box[2]-box[0], y+box[3]-box[1])
    f = open(xml_filename, 'w+')
    f.write(content)
    f.close()

def fun(xml_path, path_dir, save_dir):
    DOMTree = dom.parse(xml_path)
    root = DOMTree.documentElement
    image_name = root.getElementsByTagName("filename")[0]
    image_name = image_name.firstChild.data
    basename, _ = image_name.split('.')
    image_path = os.path.join(path_dir, image_name)
    ori_img = Image.open(image_path)
    # image_width, image_height = ori_img.size
    

    image_size = root.getElementsByTagName("size")[0]
    image_width = int(image_size.getElementsByTagName("width")[0].childNodes[0].data)
    image_height = int(image_size.getElementsByTagName("height")[0].childNodes[0].data)
    # print(image_width, image_height)
    ori_img_copy = ori_img.crop([0, 0, image_width, image_height])

    objects = root.getElementsByTagName("object")
    obj_num = 1

    for object in objects:
        box = object.getElementsByTagName("bndbox") 
        xmin = int(box[0].getElementsByTagName("xmin")[0].childNodes[0].data)
        ymin = int(box[0].getElementsByTagName("ymin")[0].childNodes[0].data)
        xmax = int(box[0].getElementsByTagName("xmax")[0].childNodes[0].data)
        ymax = int(box[0].getElementsByTagName("ymax")[0].childNodes[0].data)
        box = (xmin, ymin, xmax, ymax)
        ori_img_copy.paste((102,139,139),box)
    # ori_img_copy.save('H:/project/test2/bg.jpg')

    for object in objects:
        obj_name = object.getElementsByTagName("name")[0].childNodes[0].data
        # obj_name = obj_name.strip()

        box = object.getElementsByTagName("bndbox")
        # print(type(box[0]))
       
        xmin = int(box[0].getElementsByTagName("xmin")[0].childNodes[0].data)
        ymin = int(box[0].getElementsByTagName("ymin")[0].childNodes[0].data)
        xmax = int(box[0].getElementsByTagName("xmax")[0].childNodes[0].data)
        ymax = int(box[0].getElementsByTagName("ymax")[0].childNodes[0].data)

        box = (xmin, ymin, xmax, ymax)
        img_crop = ori_img.crop(box)
        # img_crop_name = basename + '_' + obj_name + '_' + str(obj_num) + '.jpg'
        # img_crop_savepath = os.path.join(save_dir, img_crop_name)
        # img_crop.save(img_crop_savepath)

        # img_crop_xml_filename = basename + '_' + obj_name + '_' + str(obj_num) + '.xml'
        # output_xml(img_crop_name, img_crop_xml_filename, xmax-xmin, ymax-ymin, box)

        image_process(img_crop, ori_img_copy, basename, obj_name, obj_num, box, image_width, image_height)        
        obj_num += 1
            
def image_process(img_crop, ori_img_copy, basename, obj_name, obj_num, box, image_width, image_height):    
    ori_img_copy_v_1 = ori_img_copy.crop([0, 0, image_width, image_height])
    # ori_img_copy_v_2 = ori_img_copy.crop([0, 0, image_width, image_height])
    # ori_img_copy_v_3 = ori_img_copy.crop([0, 0, image_width, image_height])
    ori_img_copy_h_1 = ori_img_copy.crop([0, 0, image_width, image_height])
    # ori_img_copy_h_2 = ori_img_copy.crop([0, 0, image_width, image_height])
    # ori_img_copy_h_3 = ori_img_copy.crop([0, 0, image_width, image_height])
    ori_img_copy_hv_1 = ori_img_copy.crop([0, 0, image_width, image_height])
    # ori_img_copy_hv_2 = ori_img_copy.crop([0, 0, image_width, image_height])
    # ori_img_copy_hv_3 = ori_img_copy.crop([0, 0, image_width, image_height])
    img_crop_v, img_crop_h, img_crop_hv = img_transform(img_crop)

    obj_num += 1
    # img_crop_v_name = basename + '_v_' + obj_name + '_' + str(obj_num) + '.jpg'
    # img_crop_v_savepath = os.path.join(save_dir, img_crop_v_name)
    # img_crop_v.save(img_crop_v_savepath)
    x_r_1 = random.randint(0, image_width-box[2]+box[0])
    y_r_1 = random.randint(0, image_height-box[3]+box[1])
    ori_img_copy_v_1_name = basename + '_bg_v_' + str(obj_num) + '.jpg'
    ori_img_copy_v_1_savepath = os.path.join(save_dir, ori_img_copy_v_1_name)
    # print(type(ori_img_copy_v_1))
    ori_img_copy_v_1.paste(img_crop_v, (x_r_1, y_r_1))
    ori_img_copy_v_1.save(ori_img_copy_v_1_savepath)

    ori_img_copy_v_1_xml_filename = basename + '_bg_v_' + str(obj_num) + '.xml'
    output_xml(ori_img_copy_v_1_name, ori_img_copy_v_1_xml_filename, box[2]-box[0], box[3]-box[1], box, x_r_1, y_r_1)
    
    # x_r_2 = random.randint(0, image_width-box[2]+box[0])
    # y_r_2 = random.randint(0, image_height-box[3]+box[1])
    # ori_img_copy_v_2_name = basename + '_bg_v_2_' + obj_name + '_' + str(obj_num) + '.jpg'
    # ori_img_copy_v_2_savepath = os.path.join(save_dir, ori_img_copy_v_2_name)
    # ori_img_copy_v_2.paste(img_crop_v, (x_r_2, y_r_2))
    # ori_img_copy_v_2.save(ori_img_copy_v_2_savepath)

    # ori_img_copy_v_2_xml_filename = basename + '_bg_v_2_' + obj_name + '_' + str(obj_num) + '.xml'
    # output_xml(ori_img_copy_v_2_name, ori_img_copy_v_2_xml_filename, box[2]-box[0], box[3]-box[1], box)

    # x_r_3 = random.randint(0, image_width-box[2]+box[0])
    # y_r_3 = random.randint(0, image_height-box[3]+box[1])
    # ori_img_copy_v_3_name = basename + '_bg_v_3_' + obj_name + '_' + str(obj_num) + '.jpg'
    # ori_img_copy_v_3_savepath = os.path.join(save_dir, ori_img_copy_v_3_name)
    # ori_img_copy_v_3.paste(img_crop_v, (x_r_3, y_r_3))
    # ori_img_copy_v_3.save(ori_img_copy_v_3_savepath)

    # ori_img_copy_v_3_xml_filename = basename + '_bg_v_3_' + obj_name + '_' + str(obj_num) + '.xml'
    # output_xml(ori_img_copy_v_3_name, ori_img_copy_v_3_xml_filename, box[2]-box[0], box[3]-box[1], box)


    obj_num += 1
    x_r_1 = random.randint(0, image_width-box[2]+box[0])
    y_r_1 = random.randint(0, image_height-box[3]+box[1])
    ori_img_copy_h_1_name = basename + '_bg_h_' + str(obj_num) + '.jpg'
    ori_img_copy_h_1_savepath = os.path.join(save_dir, ori_img_copy_h_1_name)
    ori_img_copy_h_1.paste(img_crop_h, (x_r_1, y_r_1))
    ori_img_copy_h_1.save(ori_img_copy_h_1_savepath)

    ori_img_copy_h_1_xml_filename = basename + '_bg_h_' + str(obj_num) + '.xml'
    output_xml(ori_img_copy_h_1_name, ori_img_copy_h_1_xml_filename, image_width, image_height, box, x_r_1, y_r_1)

    # x_r_2 = random.randint(0, image_width-box[2]+box[0])
    # y_r_2 = random.randint(0, image_height-box[3]+box[1])
    # ori_img_copy_h_2_name = basename + '_bg_h_2_' + obj_name + '_' + str(obj_num) + '.jpg'
    # ori_img_copy_h_2_savepath = os.path.join(save_dir, ori_img_copy_h_2_name)
    # ori_img_copy_h_2.paste(img_crop_v, (x_r_2, y_r_2))
    # ori_img_copy_h_2.save(ori_img_copy_h_2_savepath)

    # ori_img_copy_h_2_xml_filename = basename + '_bg_h_2_' + obj_name + '_' + str(obj_num) + '.xml'
    # output_xml(ori_img_copy_h_2_name, ori_img_copy_h_2_xml_filename, box[2]-box[0], box[3]-box[1], box)

    # x_r_3 = random.randint(0, image_width-box[2]+box[0])
    # y_r_3 = random.randint(0, image_height-box[3]+box[1])
    # ori_img_copy_h_3_name = basename + '_bg_h_3_' + obj_name + '_' + str(obj_num) + '.jpg'
    # ori_img_copy_h_3_savepath = os.path.join(save_dir, ori_img_copy_h_3_name)
    # ori_img_copy_h_3.paste(img_crop_v, (x_r_3, y_r_3))
    # ori_img_copy_h_3.save(ori_img_copy_h_3_savepath)

    # ori_img_copy_v_3_xml_filename = basename + '_bg_h_3_' + obj_name + '_' + str(obj_num) + '.xml'
    # output_xml(ori_img_copy_v_3_name, ori_img_copy_v_3_xml_filename, box[2]-box[0], box[3]-box[1], box)

    obj_num += 1
    x_r_1 = random.randint(0, image_width-box[2]+box[0])
    y_r_1 = random.randint(0, image_height-box[3]+box[1])
    ori_img_copy_hv_1_name = basename + '_bg_hv_' + str(obj_num) + '.jpg'
    ori_img_copy_hv_1_savepath = os.path.join(save_dir, ori_img_copy_hv_1_name)
    ori_img_copy_hv_1.paste(img_crop_hv, (x_r_1, y_r_1))
    ori_img_copy_hv_1.save(ori_img_copy_hv_1_savepath)

    ori_img_copy_h_1_xml_filename = basename + '_bg_hv_' + str(obj_num) + '.xml'
    output_xml(ori_img_copy_h_1_name, ori_img_copy_h_1_xml_filename, box[2]-box[0], box[3]-box[1], box, x_r_1, y_r_1)

    # x_r_2 = random.randint(0, image_width-box[2]+box[0])
    # y_r_2 = random.randint(0, image_height-box[3]+box[1])
    # ori_img_copy_hv_2_name = basename + '_bg_hv_2_' + obj_name + '_' + str(obj_num) + '.jpg'
    # ori_img_copy_hv_2_savepath = os.path.join(save_dir, ori_img_copy_hv_2_name)
    # ori_img_copy_hv_2.paste(img_crop_v, (x_r_2, y_r_2))
    # ori_img_copy_hv_2.save(ori_img_copy_hv_2_savepath)

    # ori_img_copy_hv_2_xml_filename = basename + '_bg_hv_2_' + obj_name + '_' + str(obj_num) + '.xml'
    # output_xml(ori_img_copy_hv_2_name, ori_img_copy_hv_2_xml_filename, box[2]-box[0], box[3]-box[1], box)

    # x_r_3 = random.randint(0, image_width-box[2]+box[0])
    # y_r_3 = random.randint(0, image_height-box[3]+box[1])
    # ori_img_copy_hv_3_name = basename + '_bg_hv_3_' + obj_name + '_' + str(obj_num) + '.jpg'
    # ori_img_copy_hv_3_savepath = os.path.join(save_dir, ori_img_copy_hv_3_name)
    # ori_img_copy_hv_3.paste(img_crop_v, (x_r_3, y_r_3))
    # ori_img_copy_hv_3.save(ori_img_copy_hv_3_savepath)

    # ori_img_copy_v_3_xml_filename = basename + '_bg_hv_3_' + obj_name + '_' + str(obj_num) + '.xml'
    # output_xml(ori_img_copy_v_3_name, ori_img_copy_v_3_xml_filename, box[2]-box[0], box[3]-box[1], box)
    
if __name__ == '__main__':
    
    path_dir = 'H:/project/00_all/qitijianceyi/'
    save_dir = 'H:/project/test2/'

    for filename in os.listdir(path_dir):
        if filename.find('xml') >= 0:
            xml_path = os.path.join(path_dir, filename)
            fun(xml_path, path_dir, save_dir)

    print('4 Done!')
