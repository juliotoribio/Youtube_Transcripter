from flask import Flask, render_template, request, flash
import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, VideoUnavailable

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class YouTubeScraper:
    def __init__(self, url):
        self.url = url
        self.video_id = self.extract_video_id(url)

    def extract_video_id(self, url):
        video_id = None
        youtube_regex = (
            r'(https?://)?(www\.)?'
            r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
            r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        match = re.match(youtube_regex, url)
        if match:
            video_id = match.group(6)
        if video_id:
            return video_id
        else:
            raise ValueError("URL de YouTube no válida")

    def get_transcript(self, languages=['es']):
        try:
            # Intentar obtener la transcripción en el idioma solicitado
            transcript = YouTubeTranscriptApi.get_transcript(self.video_id, languages)
            transcript_text = " ".join([entry['text'] for entry in transcript])
            return transcript_text
        except TranscriptsDisabled:
            print(f"Los subtítulos/transcripciones están deshabilitados para el video {self.video_id}.")
            return "Los subtítulos/transcripciones están deshabilitados para este video."
        except VideoUnavailable:
            print(f"El video {self.video_id} no está disponible.")
            return "El video no está disponible."
        except Exception as e:
            if "No transcripts were found" in str(e):
                print(f"No hay transcripciones disponibles para el video {self.video_id}.")
                return "No hay transcripciones disponibles para este video."
            else:
                print(f"Error inesperado: {str(e)}")
                return "Ocurrió un error inesperado al obtener la transcripción."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            scraper = YouTubeScraper(url)
            transcript = scraper.get_transcript()
            if transcript:
                return render_template('index.html', transcript=transcript)
            else:
                flash("No se pudo obtener la transcripción. Verifica el video.", "danger")
        except ValueError as e:
            flash(str(e), "danger")
        except Exception as e:
            print(f"Error inesperado en el servidor: {str(e)}")
            flash("Ocurrió un error inesperado. Por favor, inténtalo más tarde.", "danger")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
