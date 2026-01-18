import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
from deep_translator import GoogleTranslator
from colorama import Fore, init
import time

init(autoreset=True)

# Typewriter-style slow print
def slow_print(text, color=Fore.WHITE, delay=0.04):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()

# Text-to-speech
def speak(text, language="en"):
    try:
        tts = gTTS(text=text, lang=language)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_file = fp.name
        tts.save(temp_file)
        os.system(f"start {temp_file}")
    except Exception as e:
        slow_print(f"❌ Error in text-to-speech: {e}", Fore.RED)

# Speech-to-text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        slow_print("\n🎤 Please speak in English...", Fore.CYAN, 0.03)
        audio = recognizer.listen(source)

    try:
        slow_print("⏳ Recognizing...", Fore.YELLOW, 0.04)
        text = recognizer.recognize_google(audio, language='en-US')
        slow_print(f"🗣 You said: {text}", Fore.GREEN, 0.03)
        return text
    except sr.UnknownValueError:
        slow_print("❌ Sorry, I could not understand the audio.", Fore.RED, 0.03)
    except sr.RequestError as e:
        slow_print(f"⚠ API Error: {e}", Fore.RED, 0.03)
    return ""

# Translate text
def translate_text(text, target_language='es'):
    translater = GoogleTranslator(source='en', target=target_language)
    translated_text = translater.translate(text)
    slow_print(f"🌍 Translated text: {translated_text}", Fore.LIGHTGREEN_EX, 0.03)
    return translated_text

# Display language options
def display_language_options():
    slow_print("\n🌐 Choose target language:", Fore.CYAN, 0.04)
    slow_print("1. Urdu", Fore.RED)
    slow_print("2. Spanish", Fore.BLUE)
    slow_print("3. Chinese", Fore.GREEN)
    slow_print("4. French", Fore.WHITE)
    slow_print("5. German", Fore.MAGENTA)
    slow_print("6. Italian", Fore.CYAN)
    slow_print("7. Russian", Fore.RED)
    slow_print("8. Japanese", Fore.YELLOW)

    choice = input(Fore.LIGHTMAGENTA_EX + "\n👉 Enter your choice: ")

    language_dict = {
        '1': 'ur',
        '2': 'es',
        '3': 'zh-CN',
        '4': 'fr',
        '5': 'de',
        '6': 'it',
        '7': 'ru',
        '8': 'ja',
    }
    return language_dict.get(choice, 'es')

# Main function
def main():
    target_language = display_language_options()
    original_text = speech_to_text()
    if original_text:
        translated_text = translate_text(original_text, target_language)
        speak(translated_text, language=target_language)
        slow_print("✅ Finished speaking the translated text.", Fore.GREEN, 0.04)

if __name__ == "__main__":
    main()
