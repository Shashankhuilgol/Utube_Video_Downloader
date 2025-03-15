from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

# Function to Download YouTube Video
def download_video(url):
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save in 'downloads/' folder
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return f"downloads/{info['title']}.mp4"

# Route for Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Route to Handle Video Download
@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']  # Get URL from form
    video_path = download_video(video_url)  # Download Video

    # Return the downloaded file
    return send_file(video_path, as_attachment=True)




def download_video(url):
    ydl_opts = {
    'format': 'best',  # Download the best single format
    'outtmpl': 'downloads/%(title)s.%(ext)s',
}


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_path = f"downloads/{info['title']}.mp4"
        os.startfile(video_path)  # Open video automatically (Windows only)
        return video_path


# Run Flask App
if __name__ == '__main__':
    if not os.path.exists("downloads"):
        os.makedirs("downloads")  # Create 'downloads' folder if not exists
    app.run(debug=True)
