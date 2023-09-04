import mido
import json
import sys

mid = mido.MidiFile(sys.argv[1])
curr_time = 0
beatmap = []
for msg in mid:
    curr_time += msg.time
    if msg.type == "note_on":
        beatmap += [{
            "type": msg.note,
            "time": curr_time,
            "position": msg.velocity,
        }]

print(json.dumps({
    "name": "Brain Power",
    "notes": beatmap,
}))