from pathlib import Path
import traceback
from watchgod import watch
from watchgod.watcher import Change
from mp4_to_gif import video_to_gif
import win10toast


def handle_changes(changes):
    for change_type, file_path in changes:
        if change_type == Change.deleted:
            continue
        print(f"Изменение: {change_type} в файле {file_path}")
        file_path = Path(file_path)
        if file_path.name.endswith('.mp4'):
            output_path = file_path.parent / \
                file_path.name.replace('.mp4', '.gif')

            try:
                video_to_gif(str(file_path), str(output_path), fps=30)
            except Exception:
                traceback.print_exc()
            else:
                toaster = win10toast.ToastNotifier()
                toaster.show_toast(
                    "Video to gif", f"Добавлен новый gif:\n{output_path}")


def listen_to_directory(path):
    for changes in watch(path):
        handle_changes(changes)


def main():
    path = Path(input('LISTENER: ').strip('"').strip())
    if not path.is_dir():
        return

    print(f"Начинаю отслеживание изменений в папке: {path}")
    listen_to_directory(path)


if __name__ == "__main__":
    main()
