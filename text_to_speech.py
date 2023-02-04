from gtts import gTTS

text = "Hello, I am a text-to-speech engine."

# Create a TTS object
tts = gTTS(text=text, lang='en')

# Save the TTS object as an MP3 file
tts.save("hello.mp3")
