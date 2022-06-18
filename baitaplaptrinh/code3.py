import numpy as np


class Video:
    def __init__(self,title,link):
        self.title = title
        self.link = link

def read_video():
    title = input('nhap title: ')
    link = input('nhap link: ')
    video = Video(title,link)
    return video

def print_video(video):
    print('Video title: ',video.title , end='')
    print('Video link: ',video.link )

def print_videos(videos):
    for i in range(len(videos)):
        print(f'video {i+1}')
        print_video(videos[i])

def read_vide_txt(videos,file):
        file.write(videos.title + '\n')
        file.write(videos.link + '\n')

def read_videos():
    videos = []
    user = int(input('nhap so video: '))
    for i in range(user):
        print('video : '+ str(i + 1))
        video = read_video()
        videos.append(video)
    return videos

def print_videos_txt(videos):
    with open('D:/data.txt',mode='w') as f:
        a = len(videos)
        f.write(str(a) + '\n')
        for i in range(a):
            read_vide_txt(videos[i], f)

def read_videos_from_txt(file):
    videos = []
    with open(file,mode='r') as f:
        a = f.readline()
        a = int(a)
        for i in range(a):
            title = f.readline()
            link = f.readline()
            video = Video(title,link)
            videos.append(video)
    return videos
def main():
    videos = read_videos()
    print_videos_txt(videos)
    video = read_videos_from_txt('D:/data.txt')
    print('hien thi video ra man hinh ')
    print('\n')
    print_videos(video)

main()







