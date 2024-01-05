## image-utils

When I am dealing pics,mp3,mp4.. I always want a media utils to help me work, that's why this project start

### mp4处理

* 转png/jpg等
* 转mp3
* 转gif
* 转竖屏
* 其他格式视频转mp4

### mp3处理

* 转文字
* 转srt
* mp3裁剪
* mp3其他格式,eg:flac,WAV,AAC,Ogg,等互相转换

### 图片png/jpg处理

* 添加文字
* 图片文字识别
* 图片按比例放缩/图片旋转
* 图片转灰白
* 图片按比例剪切
* 图片格式相互转换

### install
```
pip install easy-media-utils
```
<details>
<summary>源码安装(点击展开) </summary>
# pip freeze > requirements.txt

git clone https://github.com/aceliuchanghong/easy-media-utils.git

conda create -n dealMedia python=3.11

conda activate dealMedia

pip install -r requirements.txt
</details>

### ffmpeg
前往官网,下载对应版本的文件,解压放在本地文件并且配置环境变量,确保可以访问到
```
ffmpeg -version
```
### e.g.
```
def main(converter_type, file_path='../../testfiles/onboard_cover.mp4') -> MP4Handler:
    """
    Convert MP4 each frame.
    :param converter_type:
    :param file_path:
    """
    Converter = {
        "gif": MP4ToGIFConverter,
        "mp3": MP4ToMP3Converter,
        "img": MP4ToPNGsConverter,
        "other": TVToMP4Converter,
    }
    # converter = Converter[converter_type](file_path)
    converter = Converter.get(converter_type)(file_path)
    return converter

if __name__ == "__main__":
    file_path = '../../testfiles/out/onboard_cover.mp4'
    gif_out_path = '../../testfiles/out/output.gif'
    mp3_out_path = '../../testfiles/out/output.mp3'
    pngs_out_path = '../../testfiles/out/pngs_output'
    mp4_out_path = '../../testfiles/out/Sample.mp4'

    conv_file = '../../testfiles/out/Sample.mkv'

    converter_type = "img"
    ans_path = pngs_out_path
    converter = main(converter_type, file_path)
    converter.process(ans_path)
```