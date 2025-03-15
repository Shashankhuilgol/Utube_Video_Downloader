"# YouTube Video Downloader" 
# YouTube Video Downloader

This is a simple web application built with Flask that allows users to download YouTube videos by providing the video URL.

## Project Structure

```
.gitignore
app.py
requirements.txt
downloads/
static/
    style.css
templates/
    index.html
youtube_downloader/
```

## Requirements

- Python 3.x
- Flask
- yt-dlp
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/youtube_video_downloader.git
    cd youtube_video_downloader
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter the YouTube video URL in the input box and click the "Download" button.

4. The video will be downloaded to the `downloads` folder.
