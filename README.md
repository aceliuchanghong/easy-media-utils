## image-utils

When I am dealing pics,mp3,mp4.. I always want a media utils to help me work, that's why this project start

### mp4����

* תpng/jpg��
* תmp3
* תgif
* ת����
* ������ʽ��Ƶתmp4

### mp3����

* ת����
* תsrt
* mp3�ü�
* mp3������ʽ,eg:flac,WAV,AAC,Ogg,�Ȼ���ת��

### ͼƬpng/jpg����

* �������
* ͼƬ����ʶ��
* ͼƬ����������/ͼƬ��ת
* ͼƬת�Ұ�
* ͼƬ����������
* ͼƬ��ʽ�໥ת��

### install
```
pip install easy-media-utils
```
<details>
<summary>Դ�밲װ(���չ��) </summary>
# pip freeze > requirements.txt

git clone https://github.com/aceliuchanghong/easy-media-utils.git

conda create -n dealMedia python=3.11

conda activate dealMedia

pip install -r requirements.txt
</details>

### ffmpeg
ǰ������,���ض�Ӧ�汾���ļ�,��ѹ���ڱ����ļ��������û�������,ȷ�����Է��ʵ�
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