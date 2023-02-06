import speech_recognition as sr

audioFile = sr.AudioFile("./audio_files/stylez.wav")


def speech_from_audio(audioFile):

    speech = sr.Recognizer()
    
    with audioFile as source:
        speech.adjust_for_ambient_noise(source)
        audio = speech.record(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = speech.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response




speech_from_audio(audioFile)
