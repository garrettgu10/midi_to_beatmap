import mido
mid = mido.MidiFile("example beatmap.mid")
curr_time = 0
beatmap = []
for msg in mid:
    curr_time += msg.time
    if msg.type == "note_on":
        beatmap += [(msg.note, curr_time, msg.velocity)]

json = open("beatmap.json", "w")
json.write(str(beatmap))