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
- *fc_triu.npy* 为145个人的功能连接矩阵，其中71个精神分裂症患者，74个正常对照。功能连接矩阵为246个节点间的时间序列的Pearson's相关矩阵，我只纳入了上三角部分，共30135（246*245/2）个特征。  [注：文件名一定要和targets.xlsx中的ID对应]

- 若想获取 *fc_triu.npy* 的原始246*246的数据，请转到百度云盘下载链接：https://pan.baidu.com/s/177aIKoxuZWDUTMVxW5kw8Q 
提取码：doey   

- *targets.xlsx* 为每个被试对应的ID/唯一识别码/唯一名称和类别，0为正常，1为精神分裂症

- *BNA_subregions.xlsx* 为脑246分区的信息[http://atlas.brainnetome.org/]

- *workshop.ipynb* 为演示代码的jupyter-n*otebook版本

- *workshop.py* 为演示代码的普通版本

- *requirements.txt* 为项目依赖的Python包  

- *easylearn操作视频.zip* 为使用easylearn图形界面完成精神分裂症诊断的操作视频

- <font color=red>注</font>：Demo数据为COBRE数据集 <http://fcon_1000.projects.nitrc.org/indi/retro/cobre.html>

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

#### easylearn安装方法
`pip install eslearn`
