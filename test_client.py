from client import TranscriptionClient

client = TranscriptionClient(
    "localhost",
    9090,
    is_multilingual=True,
    lang="hy",
    # translate=False,
    model="lukarape/whisper-small-erebuni-7-chp400-ct2"
)

client()





