
# 项目介绍
    本项目适用于一般情况下网上可以浏览全屏但是无法直接下载的ppt，作者以长沙理工大学网络教学平台为例编写了此脚本
 
# 环境依赖
    pip安装pyautogui, keyboard
    可以直接使用 pip install -r requirements.txt 安装依赖，推荐使用虚拟环境

# 使用方法
    执行前请修改main.py中 crop_box 的值（裁剪黑边的框）
    第一个参数是裁剪框 左边界 距离屏幕 左边界 的距离
    第二个参数是裁剪框 上边界 距离屏幕 上边界 的距离
    第一个参数是裁剪框 右边界 距离屏幕 左边界 的距离
    第二个参数是裁剪框 下边界 距离屏幕 上边界 的距离（单位均为像素）
    如果不需要请将其改为 (0, 0, x, y)，xy为你所使用的屏幕像素

    执行代码之后按一下回车即可自动开始截图并自动翻页，再按一下回车结束程序

    ***程序运行过程中请勿点击鼠标***

    输出的所有图片会按顺序存放在同级目录中的screenshot文件夹中，
    推荐使用adobe acrobat创建pdf把所有文件全部拖进去合并保存即可

# 注意事项
    该脚本仅供方便各位同学下载ppt复习划重点
    请勿将扒来的ppt上传到各类网站！！
    请尊重老师们的劳动成果与版权！！

# 作者的话
    过几天考完试试试将自动生成pdf的功能集成进来（