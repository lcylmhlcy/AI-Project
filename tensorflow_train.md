## tensorflow模型训练
1. 将 `601服务器` 上 `/home/computer/LCY/czar/` 路径下的 `sample` 文件夹复制到自己的文件夹下。
2. 首先使用 [labelImg](https://github.com/tzutalin/labelImg/files/2638199/windows_v1.8.1.zip) 标注数据。注：一张图片一个xml，标注完图片名字不能更改，否则与xml对应不上。
3. 将数据上传到 `sample` 文件夹下，数据可分为两个文件夹，一个文件夹重命名为 `train` ，另一个重命名为 `test` 。
4. cd到这个sample文件夹下，激活虚拟环境 `conda activate tf` ，编辑 `generate_tfrecord.py` 文件，第32行改成 **自己的标签名字** 。
5. 编辑 `object-detection.pbtxt` 文件，同样改为 **自己的标签名字** ，注意 id 的序号应与 `generate_tfrecord.py` 的一致。
6. 运行 `mytrain.sh` 。注：没有测试数据可将 `mytrain.sh` 中的有关 `test` 的都注释掉。
7. 训练模型会存在 `train` 文件下，有关训练参数的设置都在 `ssd_mobilenet_v1_pets.config` 文件内。
8. 编辑 `ckpt_to_pb.sh` 中的最后一个语句中的 `trained_checkpoint_prefix` ，改为自己 `train` 文件夹中的模型。运行这个sh文件。 
9. `output` 文件夹中得到 `frozen_inference_graph.pb` ，拷贝到本机android项目 `assests` 路径中，自定义一个 `labels.txt` ，格式参照已有的 `meter_labels.txt` 。
10. 打开Android studio，编辑android项目中的 `DetectorActivity` 文件，66行和68行替换成自己的pb文件和txt文件，运行项目，安装app到安卓手机。



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
