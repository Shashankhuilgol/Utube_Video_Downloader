🎬 YouTube Video Downloader
📌 Overview
The YouTube Video Downloader is a Flask-based web application that allows users to download YouTube videos in different resolutions and formats using the pytube library. The application provides a simple and user-friendly interface where users can paste a YouTube URL, choose a resolution, and download videos or audio files with ease.

Whether you want to save videos for offline viewing, extract audio from music videos, or download lectures, this tool is the perfect solution!

🚀 Features
✅ Download YouTube videos in multiple resolutions (144p, 360p, 720p, 1080p)
✅ Extract and download audio from YouTube videos
✅ Supports different formats such as MP4 and MP3
✅ Easy-to-use web interface with a clean design
✅ Error handling for invalid URLs or unavailable videos
✅ Fast and lightweight application

🛠️ Technologies Used
Backend:
Flask (Python framework for web applications)

pytube (Python library for YouTube video downloading)

Frontend:
HTML (Structure of the web pages)

CSS (Styling for a responsive UI)

Other Tools:
Git (Version control)

Virtual Environment (venv) (For package isolation)

📂 Project Structure
php
Copy
Edit
/Utube_Video_Downloader
│── app.py                 # Main Flask application
│── templates/
│   ├── index.html         # Home page
│   ├── download.html      # Download results page
│── static/
│   ├── style.css          # CSS for styling
│── downloads/             # Folder where downloaded files are stored
│── requirements.txt       # List of dependencies
│── README.md              # Documentation
🔧 Installation Guide
Step 1: Clone the Repository
Open a terminal or command prompt and run:

bash
Copy
Edit
git clone https://github.com/Shashankhuilgol/Utube_Video_Downloader.git
cd Utube_Video_Downloader
Step 2: Set Up a Virtual Environment
Create and activate a virtual environment to keep dependencies organized:

bash
Copy
Edit
python -m venv venv  
Activate the environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Step 3: Install Required Dependencies
Run the following command to install the necessary libraries:

bash
Copy
Edit
pip install -r requirements.txt
Step 4: Run the Application
Start the Flask application:

bash
Copy
Edit
python app.py
Once the server is running, open your browser and go to:
📌 http://127.0.0.1:5000/

🎯 How to Use
1️⃣ Open the application in a browser.
2️⃣ Paste the YouTube video URL into the input box.
3️⃣ Select a resolution or audio format.
4️⃣ Click the Download button.
5️⃣ The video/audio will be processed and saved in the downloads/ folder.

⚠️ Handling Large Files
If you are experiencing large file issues when pushing to GitHub, make sure to:

Delete large files from the commit history

Use .gitignore to exclude downloaded videos

Consider using Git LFS (Large File Storage) if necessary

To remove large files from tracking, use:

bash
Copy
Edit
git rm --cached downloads/your_large_file.mp4
Then commit and push again:

bash
Copy
Edit
git commit -m "Removed large files"
git push origin main
💡 Future Improvements
🔹 Add support for playlist downloads
🔹 Implement a progress bar for better user experience
🔹 Allow format conversion (e.g., MP4 to MP3)
🔹 Deploy the application on Render or Heroku


📞 Contact
For any questions, suggestions, or collaborations, feel free to reach out:

📧 Email: Shashank.huilgol22@gmail.com


🚀 Happy Downloading! 🎥🎶