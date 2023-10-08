import mido
import json
import sys

mid = mido.MidiFile(sys.argv[1])
curr_time = 1.2
beatmap = []
last_note = dict()
for msg in mid:
    curr_time += msg.time
    if msg.type == "note_on" and msg.velocity > 0:
        new_note = {
            "type": msg.note,
            "time": curr_time,
            "position": (msg.velocity + 64) % 128,
        }
        beatmap += [new_note]
        last_note[msg.note] = new_note
    if msg.type == "note_off":
        if msg.note in last_note:
            if last_note[msg.note]["type"] < 60:
                last_note[msg.note]["duration"] = curr_time - last_note[msg.note]["time"]
            del last_note[msg.note]
        else:
            # print("Warning: note_off without note_on")
            pass

print(json.dumps({
    "name": "Numb to Slaughter",
    "notes": beatmap,
}, indent=4))