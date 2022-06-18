import numpy as np


class Video:
    def __init__(self,title, link):
        self.title = title
        self.link = link


def read_video():
    title = input('nhap title : ')
    link = input('nhap link : ')
    video = Video(title,link)
    return video


def print_video(video):
    print('title video: ',video.title,end='')
    print('link video : ',video.link,end='')


def read_videos():
    user = int(input('nhap so luong video: '))
    videos = []
    for i in range(user):
        print(f'video thu: {i + 1}')
        a = read_video()
        videos.append(a)
    return videos


def print_videos(videos):
    for i in range(len(videos)):
        print(f'video thu: {i + 1}')
        print_video(videos[i])


def wile_file(f,videos):
    for i in range(len(videos)):
        f.write(str(videos[i].title) + '\n')
        f.write(str(videos[i].link) + '\n')


def write_file(x,videos):
    with open(x,mode='w') as f:
        f.write(str(len(videos)) + '\n')
        wile_file(f,videos)


def read_file(x):
    xx = []
    with open(x,mode='r') as f:
        n = f.readline()
        n = int(n)
        for i in range(n):
            title = f.readline()
            link = f.readline()
            videos = Video(title,link)
            xx.append(videos)
    return xx


def main():
    videos = read_videos()
    print('**'*40)
    # print_videos(videos)
    x = 'D:/Data4.txt'
    write_file(x,videos)
    videoxx = read_file(x)
    print_videos(videoxx)

main()