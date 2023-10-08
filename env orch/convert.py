import mido
import json
import sys

colors = ["#0FC0FC", "#7B1DAF", "#FF2FB9", "#D4FF47"]

mid = mido.MidiFile(sys.argv[1])
curr_time = 1.2
beatmap = []
for msg in mid:
    curr_time += msg.time
    if msg.type == "note_on" and msg.velocity > 0:
        new_note = {
            "type": "recolor-background",
            "time": curr_time,
            "color": colors[len(beatmap) % len(colors)]
        }
        beatmap += [new_note]

print(json.dumps({
    "events": beatmap,
}, indent=4))