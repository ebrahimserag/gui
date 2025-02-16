import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp
from moviepy  import VideoFileClip


def download_video(url, quality="high"):
    ydl_opts = {
        'format': 'best' if quality == 'high' else 'worst',
        'outtmpl': '%(title)s.%(ext)s',  
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("success", f"The video has been uploaded successfully in{quality}")
    except Exception as e:
        messagebox.showerror("error", f"An error occurred: {str(e)}")

def extract_audio():
    video_path = filedialog.askopenfilename(title="Select video", filetypes=[("Video Files", "*.mp4;*.mkv;*.avi")])
    if video_path:
        video = VideoFileClip(video_path)
        
        audio = video.audio
        
        audio_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")], title="Save audio")
        
        if audio_path:
            audio.write_audiofile(audio_path)
            print(f"The audio was successfully extracted and saved to: {audio_path}")
        else:
            print("not Audio saved ")

def on_download_video_high_click():
    url = url_entry.get()
    if url:
        download_video(url, "high")
    else:
        messagebox.showwarning("error", "Please enter YouTube link.")

def on_download_video_low_click():
    url = url_entry.get()
    if url:
        download_video(url, "low")
    else:
        messagebox.showwarning("error", "Please enter YouTube link.")


root = tk.Tk()
root.title("Download video from YouTube and extract it")

tk.Label(root, text="Enter YouTube link:").grid(pady=10 , columnspan=2)
url_entry = tk.Entry(root, width=50 )
url_entry.grid(pady=10 ,columnspan=2)

tk.Button(root, text="download high Resultion", command=on_download_video_high_click ).grid(row=3,column=0 ,padx=5,pady=5 ,ipadx=4,ipady=4  )
tk.Button(root,  text="download low Resultion", command=on_download_video_low_click ).grid(row=3,column=1 ,padx=5,pady=5 ,ipadx=4,ipady=4 )
tk.Button(root, text="Video extraction", command=extract_audio ).grid(pady=5 ,columnspan=2)

root.mainloop()
