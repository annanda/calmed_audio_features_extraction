import pathlib
import os.path

from decouple import config

main_folder = pathlib.Path(__file__).parent.parent.absolute()

MAIN_FOLDER = config('MAIN_FOLDER', default=main_folder)
raw_files_folder = os.path.join(MAIN_FOLDER, 'raw_files')
annotation_files_folder = os.path.join(MAIN_FOLDER, 'annotation_files')

# EMOTION_ANNOTATION_FOLDER = config('EMOTION_ANNOTATION_FOLDER', default=emotion_folder)
# EMOTION_ANNOTATION_FILE = config('EMOTION_ANNOTATION_FILE', default=emotions_file)
# DATASET_VIDEO_AU_FOLDER = config('DATASET_VIDEO_AU', default=os.path.join(MAIN_FOLDER, 'dataset/video/AU'))
# DATASET_VIDEO_FOLDER = config('DATASET_VIDEO_FOLDER', default=os.path.join(MAIN_FOLDER, 'dataset/video'))

RAW_FILES_FOLDER = config('RAW_FILES_FOLDER', default=raw_files_folder)
ANNOTATION_FILES_FOLDER = config('ANNOTATION_FILES_FOLDER', default=annotation_files_folder)
