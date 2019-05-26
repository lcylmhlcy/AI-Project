# coding: utf-8

import cv2
import numpy as np

def output_xml(img_filename, xml_filename, w, h, xmin, xmax, ymin, ymax):
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
		<name>meter</name>
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
</annotation>''' %(img_filename.split('/')[1], img_filename,
                    w, h, xmin, ymin, xmax, ymax)
  f = open(xml_filename, 'w+')
  f.write(content)
  f.close()


def merge(meter_filename, bg_filename, output_filename, offset_x, offset_y):
  '''将仪表合并至背景中，偏移 (offset_x, offset_y)'''
  meter = cv2.imread(meter_filename)
  h,w,_ = meter.shape

  bg = cv2.imread(bg_filename)
  bg[offset_x:offset_x+h, offset_y:offset_y+w] = meter
  h1,w1,_ = bg.shape

  xmin, xmax, ymin, ymax = offset_y, offset_y+w, offset_x, offset_x+h
  cv2.imwrite(output_filename, bg)
  output_xml(output_filename, output_filename.split('.')[0]+'.xml',
    w1, h1,
    xmin, xmax, ymin, ymax)

  # bg = cv2.flip(bg, 0, dst=None) #垂直镜像
  # output_filename = output_filename.split('.')[0] + '_v.jpg'
  # cv2.imwrite(output_filename, bg)
  # output_xml(output_filename, output_filename.split('.')[0]+'.xml',
  #   w1, h1,
  #   xmin, xmax, h1-ymax, h1-ymin)


for i in range(1, 26): # meter
  for j in range(1, 29):
    meter_filename = 'meter/%d.jpg' %(i)
    bg_filename = 'bg/%d.jpg' %(j)

    for k in range(3):
      output_filename = 'imgs/m%d_b%d_%d.jpg' %(i,j,k)
      print(output_filename)
      merge(meter_filename, bg_filename, output_filename, 100, 100+k*200)

    for k in range(3):
      output_filename = 'imgs/m%d_b%d_%d2.jpg' %(i,j,k)
      print(output_filename)
      merge(meter_filename, bg_filename, output_filename, 250, 100+k*200)