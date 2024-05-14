import pydub
def edit(file):
    song = pydub.AudioSegment.from_file(file, "m4a")
    minutes = 10
    slice_song = []
    end = minutes*60*1000
    i = 1
    while len(song) > minutes*60*1000:
        slice_song.append(song[:end])
        song = song[end:]
        slice_song[i - 1].export(f"audio_place/edited{i}.mp3", format="mp3")
        i += 1
        
    slice_song.append(song)
    song.export(f"audio_place/edited{i}.mp3", format="mp3")
    return i