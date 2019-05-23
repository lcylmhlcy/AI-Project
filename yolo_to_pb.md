## 转换 yolo, tiny-yolo
**darkflow**: https://github.com/lcylmhlcy/darkflow

## 转换 yolov2, yolov2-tiny, yolov3, yolov3-tiny
**Darknet to TensorFlow**: https://github.com/lcylmhlcy/darkflow

## android 部署
1. 拷贝到本机 [tensorflow android 项目](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android) assests 路径中.
2. 打开Android studio，编辑 [tensorflow android 项目](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android):
- DetectorActivity 文件75行替换成自己的pb文件
- TensorFlowYoloDetector中的 LABELS 定义为自己的标签。
- 运行项目，安装app到安卓手机。
