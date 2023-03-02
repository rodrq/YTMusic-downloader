import tkinter as tk
import pytube
import os
import clipboard
import settings

if os.path.exists(settings.DOWNLOAD_FOLDER) == False:
    os.makedirs(settings.DOWNLOAD_FOLDER)
    print('Created download dir')

def paste():
    entry_text.set(clipboard.paste() )
    print(clipboard.paste())
def download():
    link = entry.get()
    try:
        yt = pytube.YouTube(link, use_oauth = True, allow_oauth_cache = True)
        stream = yt.streams.get_by_itag(140)
        size = (f'{stream.filesize/1000000} MBs')
        if os.path.exists(settings.DOWNLOAD_FOLDER + f"\{yt.title}.mp3"):
            print('Song already exists in folder')
        else:
            print(f'Trying to download {yt.title}. Size = {size}')
            stream.download(output_path= f'{settings.DOWNLOAD_FOLDER}')
            print(f'{size} downloaded.')
            os.rename((settings.DOWNLOAD_FOLDER + f"\{yt.title}.mp4"), (settings.DOWNLOAD_FOLDER + f"\{yt.title}.mp3"))
            print('Format changed from MP4 to MP3')
            print(f'{yt.title} downloaded')
    except:
        print('Wrong link or something went wrong.')

ui = tk.Tk()

entry_text = tk.StringVar()
ui.title('YOUTUBE MP3 DOWNLOADER')
ui.geometry('300x150+50+50')
text1 = tk.Label(ui, text='Link')
text1.pack()
entry = tk.Entry( ui, textvariable=entry_text )
entry.pack()
tk.Button(ui, text='Copy', command = paste).pack(side= tk.TOP)
tk.Button(ui, text='Download', command = download).pack()

tk.mainloop()



