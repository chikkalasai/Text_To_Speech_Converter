# 🗣️ Django Text-to-Speech Converter

A Django-based web app that converts input text into speech using `pyttsx3`. Users can choose from available voices, convert text, and download the output as an MP3 file. Audio files are processed using `pydub` and `ffmpeg`.

---

## 🚀 Features

- Convert text input to MP3 audio
- Select from system-installed voices
- Save & download unique audio files
- Web-based user interface
- Offline TTS with `pyttsx3`

---

## 🛠️ Setup Instructions

### 1. 🔁 Clone the Repository

```bash
git clone https://github.com/yourusername/django-tts-app.git
cd django-tts-app


### 2. 📦 Create and Activate Virtual Environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate


3. 📥 Install Dependencies

pip install -r requirements.txt


🎧 Install FFmpeg (Required for pydub)
🔽 Download FFmpeg
Go to: https://ffmpeg.org/download.html
For Windows, use: https://www.gyan.dev/ffmpeg/builds/

🛠 Add FFmpeg to System PATH
Extract the ZIP file (e.g., to C:\ffmpeg)

Copy the full path of the bin folder inside it (e.g., C:\ffmpeg\bin)

Search for "Environment Variables" in Windows

Click Edit Environment Variables

Under System Variables, find and select Path, then click Edit

Click New and paste the FFmpeg bin path

Click OK and restart your terminal



```bash 
✅ Verify FFmpeg Installation

ffmpeg -version
```
📁 Output
Audio files are saved as media/speech_<timestamp>.mp3

Users can play or download audio directly from the browser

🧹 Optional Cleanup
To delete old audio files, you can set up a cron job or a Django command to clean the media/ folder periodically.


