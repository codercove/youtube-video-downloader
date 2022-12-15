from pytube import YouTube, Playlist


class DownloadYoutube:
    def downloadVideo(link):
        if link != "":
            video = YouTube(link)
            video = video.streams.get_lowest_resolution()
            try:
                print(f'\nTitle {video.title}\n')
                print(f'\nVideo Location:{video.get_file_path()}\n')
                video.download('./downloadedVideos/')
            except:
                print('Error')
            print("Video Downloaded Succesfully...")

    def downloadPlaylist(links):
        p = Playlist(links)
        try:
            for video in p.videos:
                video.streams.first().download('./downloadedPlaylists')
        except:
            print('Error')


def start():
    print('\nMENU')
    print('Download Video    : 1')
    print('Download Playlist : 2')
    x = int(input('\nEnter the number to continue:'))
    try:
        if x == 1:
            y = input('\nPaste the URL of Video:')
            if y != "":
                DownloadYoutube.downloadVideo(y)
        elif x == 2:
            y = input('\nPaste the URL od Playlist:')
            if y != "":
                DownloadYoutube.downloadPlaylist(y)
    except:
        print('Invalid Option Try Again')


start()
