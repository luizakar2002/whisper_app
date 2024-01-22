from server import TranscriptionServer

server = TranscriptionServer()
server.run(host="0.0.0.0", port=9090, custom_model_path="lukarape/whisper-small-erebuni-7-chp400-ct2")
# server.run("0.0.0.0", 9090)