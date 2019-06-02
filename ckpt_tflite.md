# ssd+mobilenet ckpt转tflite
官方demo：[Running on mobile with TensorFlow Lite](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/running_on_mobile_tensorflowlite.md)

**注意：**  
官方：https://www.tensorflow.org/install/source#linux  

![img](https://github.com/lcylmhlcy/Project-Arrangement/raw/master/img/1.png)  
  
1. 安装 bazel 
    - [安装教程](https://docs.bazel.build/versions/master/install.html#installing-bazel)
    - [bazel下载](https://github.com/bazelbuild/bazel/releases)
2. 下载 **[tf 1.12.0 源代码](https://github.com/tensorflow/tensorflow/archive/v1.12.0-rc2.zip)**
3. 编译：
    ```
    cd tensorflow-1.12.0-rc2/   
    bazel build tensorflow/python/tools:freeze_graph
    bazel build tensorflow/contrib/lite/toco:toco
    ```      
    - 注意：一定要连网，最好挂vpn
4. ckpt 转成 tflite.pb
    ```
    cd ?/models/research/
    export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
    python3 object_detection/export_tflite_ssd_graph.py \
      --pipeline_config_path=/home/computer/LCY/czar/sample2/train/pipeline.config \
      --trained_checkpoint_prefix=/home/computer/LCY/czar/sample2/train/model.ckpt-170841 \
      --output_directory=/home/computer/LCY/czar/sample2/output_lite \
      --add_postprocessing_op=true
    ```
    运行后将在output_directory目录生成tflite_graph.pb 和tflite_graph.pbtxt两个文件。
5. 合成tflite
    ```
    bazel run tensorflow/contrib/lite/toco:toco -- \
      --input_file=/home/computer/LCY/czar/sample2/output_lite/tflite_graph.pb \
      --output_file=/home/computer/LCY/czar/sample2/output_lite/detect_00.tflite \
      --input_shapes=1,300,300,3 \
      --input_arrays=normalized_input_image_tensor \
      --output_arrays='TFLite_Detection_PostProcess','TFLite_Detection_PostProcess:1','TFLite_Detection_PostProcess:2','TFLite_Detection_PostProcess:3' \
      --inference_type=FLOAT \
      --allow_custom_ops
    ```
6. tflite 移植到android项目
    - [tensorflow tflite demo](https://github.com/tensorflow/examples/tree/master/lite)
    - 将模型文件复制到 assests 文件夹下， 仿照demo中的 labelmap.txt 新建自己模型的txt。
    - 在 DetectorActivity 中，如下图所示：
    ![img](https://github.com/lcylmhlcy/Project-Arrangement/raw/master/img/2.png)  
