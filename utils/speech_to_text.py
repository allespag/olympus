from pathlib import Path

import speech_recognition as sr

WALKERS = Path("app/static/audio/walker").glob("*.wav")

GOOGLE_CLOUD_SPEECH_CREDENTIALS = (
    r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
)


# USE GOOGLE CLOUD SPEECH LIBRARY FOR PYTHON
# https://github.com/Uberi/speech_recognition?tab=readme-ov-file#readme
# https://cloud.google.com/speech-to-text/docs/before-you-begin?hl=fr
# https://cloud.google.com/speech-to-text/pricing?hl=fr


def main() -> None:
    r = sr.Recognizer()
    walker = next(WALKERS)

    with sr.AudioFile(str(walker)) as source:
        audio = r.record(source)
        text = r.recognize_google_cloud(audio, language="fr-FR")
        print(text)


if __name__ == "__main__":
    main()
