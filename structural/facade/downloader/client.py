from structural.facade.downloader.downloaders.media import MediaDownloader


def run():
    MediaDownloader.download_mp3(filename='music.mp3', url='http://www.example.com/music.mp3')
    MediaDownloader.download_mp4(filename='movie.mp4', url='http://www.example.com/movie.mp4')


if __name__ == '__main__':
    run()
