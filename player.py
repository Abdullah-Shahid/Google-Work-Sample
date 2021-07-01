from .library import VideoLibrary
import re

class VideoPlayer:
    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")
        
    def show_all_videos(self):
        all_videos = self._video_library.get_all_videos()
        sorted_videos = sorted(all_videos, key=lambda x:x.title)
        print("Here's a list of all available videos:")
        for sorted_video in sorted_videos:
             print(sorted_video.title, sorted_video.video_id, sorted_video.tags)
    
    def play_video(self, video_id):
        video = self._video_library.get_video(video_id)
        if video is None:
            print("The video you are looking for does not exist")
        else:
