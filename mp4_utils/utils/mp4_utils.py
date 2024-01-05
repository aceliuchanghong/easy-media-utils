import subprocess
import os
from PIL import Image


def get_video_info(video_path, frame_output_path='temp_frame.jpg'):
    command = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration,size', '-of',
               'default=noprint_wrappers=1:nokey=1', video_path]
    output = subprocess.check_output(command).decode('utf-8').strip().split('\n')
    duration = float(output[0])
    size = int(output[1])

    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # 使用 ffmpeg 截取视频的第一帧
    cmd = ['ffmpeg', '-i', video_path, '-ss', '00:00:01.000', '-vframes', '1', frame_output_path, '-y']
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 确保截图成功生成
    if not os.path.exists(frame_output_path):
        print("Failed to capture frame from video.")
        return None

    # 使用 PIL 打开图像并获取尺寸
    with Image.open(frame_output_path) as img:
        width, height = img.size

    # 清理临时文件
    os.remove(frame_output_path)

    video_info = {
        'name': video_name,
        'duration': duration,
        'size': size,
        'path': video_path,
        'width': width,
        'height': height
    }
    return video_info


def split_video(video_path, duration, output_dir=None):
    if output_dir is None:
        output_dir = os.path.dirname(video_path)
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    command = ['ffmpeg', '-i', video_path, '-c', 'copy', '-segment_time', str(duration), '-f', 'segment',
               '-reset_timestamps', '1', '-map', '0', os.path.join(output_dir, f'{video_name}_%03d.mp4')]
    subprocess.run(command)

    split_files = []
    for file in os.listdir(output_dir):
        if file.startswith(f'{video_name}_') and file.endswith('.mp4'):
            split_files.append(output_dir + "/" + file)

    return split_files


# 使用示例
if __name__ == "__main__":
    video_path = '../../testfiles/out/onboard_cover.mp4'
    info = get_video_info(video_path)
    if info:
        print(f"Video size: {info['size']} bytes")
        print(f"Video duration: {info['duration']} seconds")
        print(f"Video resolution: {info['name']} {info['path']}")
        print(f"Video resolution: {info['width']} {info['height']}")
