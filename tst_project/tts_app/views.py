from django.shortcuts import render
import pyttsx3
import os
from pydub import AudioSegment
from django.conf import settings
from datetime import datetime

def index(request):
    audio_file = None
    filename = None
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_options = [{'id': v.id, 'name': v.name} for v in voices]

    if request.method == 'POST':
        text = request.POST.get('text')
        voice_id = request.POST.get('voice_id')

        engine.setProperty('voice', voice_id)
        engine.setProperty('rate', 150)

        # Generate unique file name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"speech_{timestamp}.mp3"
        wav_path = os.path.join(settings.MEDIA_ROOT, f"speech_{timestamp}.wav")
        mp3_path = os.path.join(settings.MEDIA_ROOT, filename)

        # Save and convert
        engine.save_to_file(text, wav_path)
        engine.runAndWait()

        sound = AudioSegment.from_wav(wav_path)
        sound.export(mp3_path, format="mp3")

        # Set audio file URL for playback
        audio_file = settings.MEDIA_URL + filename

    return render(request, 'new.html', {
        'voices': voice_options,
        'audio_file': audio_file,
        'filename': filename
    })
