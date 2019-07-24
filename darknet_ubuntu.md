1. 下载darknet框架。
    `git clone git@github.com:AlexeyAB/darknet.git`
2. 修改根目录下的`Makefile`文件。
    ```
    GPU=1
    CUDNN=1
    LIBSO=1
    ```
3. 根目录下执行`make`命令。
4. 将编译后根目录下生成的`darknet`和`libdarknet.so`拷贝到目录`/build/darknet/x64`下
5. 将`my-train.sh`、`my-test.sh`、`my-model`整个文件夹放在目录`/build/darknet/x64`下。
6. 在`my-test.sh`中更改测试图片的路径后，执行，结果为目录`/build/darknet/x64`下的`predictions.jpg`。
  
**训练过程请参考[AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)库。**
