import streamlit as st


def speech_to_text(audio):
    """The function `speech_to_text` takes an audio file as input and uses a specified model to transcribe
    the speech in the file, with options to tag audio events, specify language, and annotate speakers.

    Parameters
    ----------
    audio
        The `audio` parameter in the `speech_to_text` function is the input audio file that you want to
    convert to text. This file contains the speech that you want to transcribe into text.

    Returns
    -------
        The function `speech_to_text` returns the transcription of the audio file provided as input, with
    additional annotations such as tagging audio events like laughter, applause, etc., and diarization
    to annotate who is speaking in the audio.

    """
    transcription = st.session_state[
        "elevenlabs"
    ].speech_to_text.convert(
        file=audio,
        model_id="scribe_v2",  # Model to use
        tag_audio_events=True,  # Tag audio events like laughter, applause, etc.
        language_code="eng",  # Language of the audio file. If set to None, the model will detect the language automatically.
        diarize=True,  # Whether to annotate who is speaking
    )

    return transcription.text
