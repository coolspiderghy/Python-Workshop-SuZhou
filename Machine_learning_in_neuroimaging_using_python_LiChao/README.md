# Python在神经影像机器学习中的应用  
> 作者：黎超  
> Email: lichao19870617@163.com  
> easylearn为一站式机器学习图形界面软件，网址：https://github.com/lichao312214129/easylearn  
> easylearn微信交流群:    
> <img src="./easylearn交流群.jpg" width = "200" height = "200" div align=top />    
  
### 神经影像机器学习一般流程
链接：https://www.processon.com/view/link/5fb4f37a1e085368771b301a  
微信二维码:    
<img src="./一般流程.png" width = "200" height = "200" div align=top />   
<font color=red>**密码：F5tU**</font>

### 文件说明
- fc_triu.npy为145个人的功能连接矩阵，其中71个精神分裂症患者，74个正常对照。功能连接矩阵为246个节点间的时间序列的Pearson's相关矩阵，我只纳入了上三角部分，共30135（246*245/2）个特征。  [注：文件名一定要和targets.xlsx中的ID对应]

- 若想获取fc_triu.npy的原始246*246的数据，请转到百度云盘下载链接：https://pan.baidu.com/s/177aIKoxuZWDUTMVxW5kw8Q 
提取码：doey   

- targets.xlsx为每个被试对应的ID/唯一识别码/唯一名称和类别，0为正常，1为精神分裂症

- workshop.ipynb为演示代码的jupyter-notebook版本

- workshop.py为演示代码的普通版本

- requirements.txt为项目依赖的Python包  

### 版本
Python3.7  

### 依赖包
os  
scipy  
pandas  
numpy  
matplotlib 
seaborn  
collections  
scikit-learn  
nilearn  
pyecharts  
jupyter   

#### 安装方法
切换到本目录，在终端使用如下命令安装所有依赖  
`pip install -r requirements.txt`
