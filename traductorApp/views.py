from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from googletrans import Translator
from gtts import gTTS
import os 
from django.conf import settings


class TranslateView(APIView):
    """
    API View to translate a given text to a specified language.

    Methods
    -------
    post(request):
        Translates the provided text to the specified language and returns the translated text.
    """

    def post(self, request):
        """
        Handles POST requests for translating text.

        Parameters
        ----------
        request : Request
            The incoming HTTP request containing the text to be translated and the target language.

        Returns
        -------
        Response
            A JSON response containing the translated text or an error message if the input is invalid.

        Request Data
        ------------
        - text : str
            The text that needs to be translated (required).
        - lang : str, optional
            The target language code for translation (default is 'en' for English).
        
        Response JSON
        -------------
        - translated : str
            The translated text if successful.
        - error : str
            An error message if the translation fails or if the input text is missing.
        
        HTTP Status Codes
        -----------------
        - 200 OK : When translation is successful.
        - 400 Bad Request : When the input text is missing.
        """
        text = request.data.get('text')
        lang = request.data.get('lang', 'en')

        if not text:
            return Response({'error': 'No se proporcionó texto'}, status=status.HTTP_400_BAD_REQUEST)

        translator = Translator()
        translated = translator.translate(text, dest=lang)

        return Response({'translated': translated.text})

class PronounceView(APIView):
    """
    API View to generate an audio pronunciation of a given text in a specified language.

    Methods
    -------
    post(request):
        Converts the provided text into a speech audio file and returns the URL to access the audio.
    """

    def post(self, request):
        """
        Handles POST requests for generating text pronunciation.

        Parameters
        ----------
        request : Request
            The incoming HTTP request containing the text to be pronounced and the target language.

        Returns
        -------
        Response
            A JSON response containing the URL to access the generated audio file.

        Request Data
        ------------
        - text : str
            The text to be converted to speech (required).
        - lang : str, optional
            The language code for pronunciation (default is 'en' for English).
        
        Response JSON
        -------------
        - audio_url : str
            The absolute URL to access the generated audio file.
        
        HTTP Status Codes
        -----------------
        - 200 OK : When the audio generation is successful.
        - 400 Bad Request : When the input text is missing or invalid.
        """
        text = request.data.get('text')
        lang = request.data.get('lang', 'en')

        # Generate the audio file with the provided text and language.
        tts = gTTS(text=text, lang=lang)
        audio_name = "pronunciation.mp3"
        audio_name_path = os.path.join(settings.MEDIA_ROOT, audio_name)
        
        # Save the generated audio file to the specified path.
        tts.save(audio_name_path)

        # Construct the absolute URL for accessing the audio file.
        audio_url = request.build_absolute_uri(os.path.join(settings.MEDIA_URL, audio_name))

        return Response({'audio_url': audio_url})
