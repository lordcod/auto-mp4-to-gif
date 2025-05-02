import ffmpeg


def video_to_gif(input_video, output_gif, fps):
    ffmpeg.input(input_video).output(
        output_gif, vf=f"fps={fps}", y=None).run()
    print(f"GIF сохранён: {output_gif}")


if __name__ == '__main__':
    from pathlib import Path
    input = Path(r"C:\Users\2008d\Videos\Movavi Library\Новый проект.mp4")
    output = input.parent / input.name.replace('.mp4', '.gif')
    output = "output.gif"
    video_to_gif(input, output, fps=30)
