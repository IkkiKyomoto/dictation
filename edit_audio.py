import pydub

def edit(file, file_format):
    song = pydub.AudioSegment.from_file(file, file_format)
    #song = song.speedup(playback_speed=2.0, crossfade=0)
    minutes = 10
    slice_song = []
    end = minutes*60*1000
    i = 1
    while len(song) > minutes*60*1000:
        slice_song.append(song[:end])
        song = song[end:]
        slice_song[i - 1].export(f"workplace/edited{i}.mp3", format="mp3")
        i += 1
        
    slice_song.append(song)
    song.export(f"workplace/edited{i}.mp3", format="mp3")
    return i