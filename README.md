# image-utils

When I am doing my job, I always want some utils to help me work better

```
研究下这个:
https://github.com/BetaSu/second-curve/blob/main/docs/idea/flow.md
```

## mp4处理

* 转png/jpg等
* 转mp3
* 转gif
* 转竖屏
* 其他格式视频转mp4

## mp3处理

* 转文字
* 转srt
* mp3裁剪
* mp3其他格式,eg:flac,WAV,AAC,Ogg,等互相转换

## 图片png/jpg处理

* 添加文字
* 图片文字识别
* 图片按比例放缩/图片旋转
* 图片转灰白
* 图片按比例剪切
* 图片格式相互转换

# install

```
# pip freeze > requirements.txt
conda create -n dealMedia python=3.11
conda activate dealMedia
pip install -r requirements.txt
```

前往ffmpeg官网,下载对应版本的文件,解压放在本地文件并且配置环境变量,确保可以访问到

```
ffmpeg -version
```
