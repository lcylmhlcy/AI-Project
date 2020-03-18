# Project-Arrangement

## 主任务
1. ~~标注数据~~
2. ~~基于已搭建好的tensorflow环境，用ssd+mobilenet训练模型，并在安卓端部署。~~
3. ~~对仪表数据进行标注，完成仪表识别和仪表读数。~~
4. ~~对其余数据进行标注，并训练模型。~~

## 试验型任务（支线任务）
- ~~tensorflow android开源的demo有三种目标目标检测模型，其它两种为yolo和multibox，试验一下yolo效果。~~
- ~~将tensorflow pb模型转为lite，安卓部署试验。~~
- [tf_lite](https://tensorflow.google.cn/lite) 除了 ssd + mobilenet，是否还有支持的目标检测模型？
- [tf_lite](https://tensorflow.google.cn/lite) 支持的其他任务模型（最近又开源了一些，尤其是行为识别）
- **阿里巴巴的 [MNN](https://github.com/alibaba/MNN)**
- **腾讯的 [ncnn](https://github.com/Tencent/ncnn)** 例子：[ncnnforandroid_objectiondetection_Mobilenetssd](https://github.com/chehongshu/ncnnforandroid_objectiondetection_Mobilenetssd)

## 主要问题：
画面有被检测目标时，能框出目标。但是只有背景时，会出现大物体被误检。  
<p>
	<img src="https://github.com/lcylmhlcy/Project-Arrangement/raw/master/img/3.jpg" alt="Sample" height=600>
	<img src="https://github.com/lcylmhlcy/Project-Arrangement/raw/master/img/4.jpg" alt="Sample" height=600>
</p>  

## website
[Detecting Pikachu on Android using Tensorflow Object Detection](https://towardsdatascience.com/detecting-pikachu-on-android-using-tensorflow-object-detection-15464c7a60cd)  
  
[Building a Toy Detector with Tensorflow Object Detection API](https://towardsdatascience.com/building-a-toy-detector-with-tensorflow-object-detection-api-63c0fdf2ac95)  
  
[tensorflow-android 官方demo源码分析](https://blog.csdn.net/u013510838/article/details/79827119)  
  
[TensorFlow Lite Object Detection Android Demo](https://github.com/tensorflow/examples/blob/master/lite/examples/object_detection/android/README.md)  
  
[tensorflow-android get started object detection](https://tensorflow.google.cn/lite/models/object_detection/overview)  
  
[Running on mobile with TensorFlow Lite](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_mobile_tensorflowlite.md)  
  
[tensorflow 源码安装](https://www.tensorflow.org/install/source)  
  
[TensorFlow Android Camera Demo](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android)
