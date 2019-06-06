## tensorflow模型训练
1. 将 `601服务器` 上 `/home/computer/LCY/czar/` 路径下的 `sample` 文件夹复制到自己的文件夹下。
2. 首先使用 [labelImg](https://github.com/tzutalin/labelImg/files/2638199/windows_v1.8.1.zip) 标注数据。注：一张图片一个xml，标注完图片名字不能更改，否则与xml对应不上。
3. 将数据上传到 `sample` 文件夹下，数据可分为两个文件夹，一个文件夹重命名为 `train` ，另一个重命名为 `test` 。
4. cd到这个sample文件夹下，激活虚拟环境 `conda activate tf` ，编辑 `generate_tfrecord.py` 文件，第32行改成 **自己的标签名字** 。
5. 编辑 `object-detection.pbtxt` 文件，同样改为 **自己的标签名字** ，注意 id 的序号应与 `generate_tfrecord.py` 的一致。
6. 修改 `ssd_mobilenet_v1_pets.config` , 参考下下面注意事项的第一个。
7. 运行 `mytrain.sh` 。注：没有测试数据可将 `mytrain.sh` 中的有关 `test` 的都注释掉。
8. 训练模型会存在 `train` 文件下，有关训练参数的设置都在 `ssd_mobilenet_v1_pets.config` 文件内。
9. 编辑 `ckpt_to_pb.sh` 中的最后一个语句中的 `trained_checkpoint_prefix` ，改为自己 `train` 文件夹中的模型。运行这个sh文件。 
10. `output` 文件夹中得到 `frozen_inference_graph.pb` ，拷贝到本机android项目 `assests` 路径中，自定义一个 `labels.txt` ，格式参照已有的 `meter_labels.txt` 。
11. 打开Android studio，编辑 [tensorflow android 项目](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android) 中的 `DetectorActivity` 文件，66行和68行替换成自己的pb文件和txt文件，运行项目，安装app到安卓手机。


## 注意事项
1. `ssd_mobilenet_v1_pets.config` 文件：
    - 第9行 num_classes 要检测的数目
    - 第143行 batch_size
    - 第148行 initial_learning_rate
    - 第158行 fine_tune_checkpoint
        - "../ssd_mobilenet_v1_coco_11_06_2017/model.ckpt"
        - 不加载，从头训练
    - 第159行 num_steps 最大迭代次数
    - 第173，175，187，189行 需要按自己的目录更改
    - 第161，165行 数据增强策略，应该可以添加。默认水平翻转和随机切割
    - **第85行 depth_multiplier 模型压缩比率 默认为1不压缩，网上压缩设为0.3时模型文件在1M以内，且20ms**
2. 运行 tensorboard
    - 激活虚拟环境，进入sample路径下
    - 运行 `tensorboard --logdir=./train --port=6006` 不写port默认为6006

## 其它
1. 运行程序断开与服务器连接也可运行。
      ```如果是首次登录，可用screen启动会话，保持异常断开后，程序仍在运行：
      screen -S screen_name #可通过-S指定会话名称，方便恢复

      恢复：
      screen -r screen_name
      ```

2. 使用 `nohup` 命令也可。
      ```
      nohup python3 ??? > log.txt 2>&1 @
      ```
      终端的输出会重定向到log.txt文件中。
