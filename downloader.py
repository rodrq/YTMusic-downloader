import tkinter as tk
import pytube
import os
import clipboard

def paste():
    entry_text.set( clipboard.paste() )
    print(clipboard.paste())
def download():
    link = entry.get()
    try:
        yt = pytube.YouTube(link, use_oauth = True, allow_oauth_cache = True)
        stream = yt.streams.get_by_itag(140)
        size = (f'{stream.filesize/1000000} MBs')
        if os.path.exists(f'D:\Programacion\YTMusic downloader\{yt.title}.mp3'):
            print('Song already exists in folder')
        else:
            print(f'Trying to download {yt.title}. Size = {size}')
            stream.download(output_path= 'D:\Programacion\YTMusic downloader')
            print(f'{size} downloaded. {yt.title} ready')
            os.rename(f'D:\Programacion\YTMusic downloader\{yt.title}.mp4', f'D:\Programacion\YTMusic downloader\{yt.title}.mp3')
            print('Format changed from MP4 to MP3')
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



