### 框架: 腾讯ncnn
### Android Studio版本: 3.6
### 模拟机:
    <img src="https://github.com/lcylmhlcy/Project-Arrangement/raw/master/img/ncnn_win_1.png" alt="Sample" height=200>

### SDK:  
    <img src="https://github.com/lcylmhlcy/Project-Arrangement/raw/master/img/ncnn_win_2.png" alt="Sample" height=200>

### NDK: 20.1  
### 环境: Window10  
### 处理器: AMD R5 3550H  

**主要参考：https://blog.csdn.net/qq_14845119/article/details/104997098**

### 具体步骤
1. 新建工程：Native C++，C++ Standard：c++11
2. 下载必需文件：（1）ncnn平台支持文件和依赖库；（2）yolo模型加密后的.id.h文件与模型文件
    <img src="https://github.com/lcylmhlcy/Project-Arrangement/raw/master/img/ncnn_win_3.png" alt="Sample" height=200>

    注：只找到了linux系统编译方法，现在的电脑安虚拟机带不动，故直接找的已编译好的文件。
    教程：https://blog.csdn.net/qq_33431368/article/details/84990390

3. 将ncnn的头文件支持加入到项目include文件夹中，并添加平台支持文件（选择具体对应平台即可）  
    <img src="https://github.com/lcylmhlcy/Project-Arrangement/raw/master/img/ncnn_win_4.png" alt="Sample" height=200>

4. 添加转换后的模型文件，其中words文件存放label  
    <img src="https://github.com/lcylmhlcy/Project-Arrangement/raw/master/img/ncnn_win_5.png" alt="Sample" height=200>

5. 添加模型头文件，添加识别图片，修改layout
6. 在java文件夹中添加新类并实现
7. 修改MainActivity文件（项目重要文件），实现初始化和label读取
8. 在cpp文件中，修改yolov3_jni.cpp中的2个接口函数（具体详见代码） Java_com_example_mobilev2yolov3_YOLOV3_Init（parm与bin） Java_com_example_mobilev2yolov3_YOLOV3_Detect
9. 修改CMakeList（以CMakeList.txt作为基准文件坐标，去寻找其他目录文件，添加一些其他需要的文件，查找和生成动态库，最后连接库）
    include_directories （具体详见代码）
    add_library 
    set_target_properties 
    add_library 
    find_library 
    target_link_libraries
10. 修改build.gradle，其中abiFilters里面根据需要添加所需。
### 运行情况
### 其他注意事项
1. 模型转换：
    腾讯开源的ncnn中不能直接加载我们自己训练好的文件，而是加载其自己定义的param和bin模型文件。
    Pytorch转ncnn参考：
    https://blog.csdn.net/qq_24946843/article/details/99629417
    https://www.jianshu.com/p/eab266828555
2. 建设中…
