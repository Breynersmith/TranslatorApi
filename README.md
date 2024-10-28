# TranslatorApi
created with django rest framework


```markdown
# Text Translation and Pronunciation API

This project provides a simple API to translate text into different languages and generate audio pronunciations using Django and gTTS (Google Text-to-Speech). It includes two main functionalities: text translation and pronunciation generation.

## Features
- **Text Translation**: Translate text into a specified language using the `/translate/` endpoint.
- **Text Pronunciation**: Generate an audio pronunciation file for a given text using the `/pronounce/` endpoint.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/usuario/proyecto-traduccion-pronunciacion.git
   cd proyecto-traduccion-pronunciacion
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Django settings**:
   Make sure to set the `MEDIA_ROOT` and `MEDIA_URL` in your Django `settings.py` file to define where media files (such as generated audio files) will be stored and accessed.

   ```python
   # Example settings for media files in settings.py
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   MEDIA_URL = '/media/'
   ```

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

### Translate Text

**Endpoint**: `/translate/`  
**Method**: `POST`  
**Description**: Translates the provided text to a specified language.

**Request Data**:
```json
{
  "text": "Hello world",
  "lang": "es"
}
```

**Response**:
```json
{
  "translated": "Hola mundo"
}
```

### Pronounce Text

**Endpoint**: `/pronounce/`  
**Method**: `POST`  
**Description**: Generates an audio pronunciation file for the provided text.

**Request Data**:
```json
{
  "text": "Hola",
  "lang": "es"
}
```

**Response**:
```json
{
  "audio_url": "http://localhost:8000/media/pronunciation.mp3"
}
```

## Project Structure

```
├── app/
│   ├── views.py              # Contains the views: TranslateView and PronounceView
│   ├── urls.py               # Defines API routes for translation and pronunciation
│   └── ...
├── media/                    # Directory for generated audio files (created automatically)
├── requirements.txt          # List of required packages
└── README.md                 # Project documentation
```

## Requirements
- Python 3.x
- Django
- gTTS (Google Text-to-Speech)
- Django REST Framework

## Setup Notes
- Ensure that the server running the application has write permissions for the `media/` folder.
- The `MEDIA_URL` should be properly configured in the Django settings to serve the generated audio files.

## Contributing
Feel free to submit issues or pull requests if you find any bugs or want to add new features.

