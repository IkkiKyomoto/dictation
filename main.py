import openai
import shutil
import datetime
from edit_audio import edit

path = "audio_place/audio.m4a"
audio_file= open(path, "rb")
num = edit(audio_file)
print("audio file edited")
text = ""
for i in range(1, num + 1):
    audio_file = open(f"audio_place/edited{i}.mp3", "rb")
    response = openai.Audio.transcribe("whisper-1", audio_file)
    text += response["text"]
    dt_now = datetime.datetime.now()
    print(f"audio file {i} / {num} completed")
f = open(f'result/dictation.txt', 'w')
f.write(text + '\n')
f.close()
shutil.move("audio_place/audio.m4a", f"archive/audio{dt_now.isoformat()}.m4a")
shutil.rmtree("audio_place/")
print("all completed!!")
# for i, edited_file in enumerate(edited_files):
#     transcript = openai.Audio.transcribe("whisper-1", edited_files[i])
#     f = open(f'result/dictation{i}.txt', 'w')

#     f.write(transcript["text"] + '\n')

#     f.close()
#     dt_now = datetime.datetime.now()
#     shutil.move("audio_place/audio.wav", f"archive/audio{dt_now.isoformat()}.m4a")