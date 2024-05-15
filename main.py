import openai
import shutil
import datetime
import glob
import os
from edit_audio import edit

audio_files = glob.glob("audio_place/*")
for i, audio_file in enumerate(audio_files):
    file_format = audio_file.split(".")[-1]
    audio_file = open(audio_file, "rb")
    num = edit(audio_file, file_format)
    print("audio file edited")
    text = ""
    for j in range(1, num + 1):
        edited_audio_file = open(f"workplace/edited{j}.mp3", "rb")
        response = openai.Audio.transcribe("whisper-1", edited_audio_file)
        text += response["text"]
        dt_now = datetime.datetime.now()
        print(f"{i + 1} / {len(audio_files)} audio file: {j} / {num} completed")
    f = open(f'result/dictation{dt_now.isoformat()}.txt', 'w')
    f.write(text + '\n')
    f.close()
    shutil.move(audio_file.name, f"archive/audio{dt_now.isoformat()}.{file_format}")
    workplace_files = glob.glob("workplace/*")
    for workplace_file in workplace_files:
        os.remove(workplace_file)
    print(f"{i} / {len(audio_files)} completed!!")
print("all completed!!")
# path = "audio_place/audio.m4a"
# audio_file= open(path, "rb")
# file_format
# num = edit(audio_file, file_format)
# print("audio file edited")
# text = ""
# for i in range(1, num + 1):
#     audio_file = open(f"audio_place/edited{i}.mp3", "rb")
#     response = openai.Audio.transcribe("whisper-1", audio_file)
#     text += response["text"]
#     dt_now = datetime.datetime.now()
#     print(f"audio file {i} / {num} completed")
# f = open(f'result/dictation{dt_now.isoformat()}.txt', 'w')
# f.write(text + '\n')
# f.close()
# shutil.move("audio_place/audio.m4a", f"archive/audio{dt_now.isoformat()}.m4a")

# shutil.rmtree("audio_place/")
# print("all completed!!")
# for i, edited_file in enumerate(edited_files):
#     transcript = openai.Audio.transcribe("whisper-1", edited_files[i])
#     f = open(f'result/dictation{i}.txt', 'w')

#     f.write(transcript["text"] + '\n')

#     f.close()
#     dt_now = datetime.datetime.now()
#     shutil.move("audio_place/audio.wav", f"archive/audio{dt_now.isoformat()}.m4a")