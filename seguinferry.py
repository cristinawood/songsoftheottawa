from miditime.miditime import MIDITime
from datetime import datetime
import random

# coding: utf-8

mymidi = MIDITime(120, 'seguinferry.mid', 240, 4, 1)
my_data = [
{'event_date': datetime	(1912,1,1), 'trips':	0	},
{'event_date': datetime	(1912,1,2), 'trips':	0	},
{'event_date': datetime	(1912,1,3), 'trips':	0	},
{'event_date': datetime	(1912,1,4), 'trips':	0	},
{'event_date': datetime	(1912,1,5)	, 'trips':	0	},
{'event_date': datetime	(1912,1,6)	, 'trips':	0	},
{'event_date': datetime	(1912,1,7)	, 'trips':	2	},
{'event_date': datetime	(1912,1,8)	, 'trips':	2	},
{'event_date': datetime	(1912,1,9)	, 'trips':	2	},
{'event_date': datetime	(1912,1,10)	, 'trips':	2	},
{'event_date': datetime	(1912,1,11)	, 'trips':	2	},
{'event_date': datetime	(1912,1,12)	, 'trips':	1	},
{'event_date': datetime	(1912,1,13)	, 'trips':	1	},
{'event_date': datetime	(1912,1,14)	, 'trips':	2	},
{'event_date': datetime	(1912,1,15)	, 'trips':	2	},
{'event_date': datetime	(1912,1,16)	, 'trips':	2	},
{'event_date': datetime	(1912,1,17)	, 'trips':	2	},
{'event_date': datetime	(1912,1,18)	, 'trips':	2	},
{'event_date': datetime	(1912,1,19)	, 'trips':	2	},
{'event_date': datetime	(1912,1,20)	, 'trips':	2	},
{'event_date': datetime	(1912,1,21)	, 'trips':	2	},
{'event_date': datetime	(1912,1,22)	, 'trips':	2	},
{'event_date': datetime	(1912,1,23)	, 'trips':	2	},
{'event_date': datetime	(1912,1,24)	, 'trips':	0	},
{'event_date': datetime (1912,2,1), 'trips':    0  },
{'event_date': datetime (1912,2,2), 'trips':    0  },
{'event_date': datetime (1912,2,3), 'trips':    0  },
{'event_date': datetime (1912,2,4), 'trips':    0  },
{'event_date': datetime (1912,2,5)  , 'trips':  0  },
{'event_date': datetime (1912,2,6)  , 'trips':  0  },
{'event_date': datetime (1912,2,7)  , 'trips':  2  },
{'event_date': datetime (1912,2,8)  , 'trips':  2  },
{'event_date': datetime (1912,2,9)  , 'trips':  2  },
{'event_date': datetime (1912,2,10) , 'trips':  2  },
{'event_date': datetime (1912,2,11) , 'trips':  2  },
{'event_date': datetime (1912,2,12) , 'trips':  1  },
{'event_date': datetime (1912,2,13) , 'trips':  1  },
{'event_date': datetime (1912,2,14) , 'trips':  2  },
{'event_date': datetime (1912,2,15) , 'trips':  2  },
{'event_date': datetime (1912,2,16) , 'trips':  2  },
{'event_date': datetime (1912,2,17) , 'trips':  2  },
{'event_date': datetime (1912,2,18) , 'trips':  2  },
{'event_date': datetime (1912,2,19) , 'trips':  2  },
{'event_date': datetime (1912,2,20) , 'trips':  2 },
{'event_date': datetime (1912,2,21) , 'trips':  2  },
{'event_date': datetime (1912,2,22) , 'trips':  2  },
{'event_date': datetime (1912,2,23) , 'trips':  2  },
{'event_date': datetime (1912,2,24) , 'trips':  0  },
{'event_date': datetime (1912,3,1), 'trips':    0  },
{'event_date': datetime (1912,3,2), 'trips':    0  },
{'event_date': datetime (1912,3,3), 'trips':    0  },
{'event_date': datetime (1912,3,4), 'trips':    0  },
{'event_date': datetime (1912,3,5)  , 'trips':  0  },
{'event_date': datetime (1912,3,6)  , 'trips':  0  },
{'event_date': datetime (1912,3,7)  , 'trips':  2  },
{'event_date': datetime (1912,3,8)  , 'trips':  2  },
{'event_date': datetime (1912,3,9)  , 'trips':  2  },
{'event_date': datetime (1912,3,10) , 'trips':  2  },
{'event_date': datetime (1912,3,11) , 'trips':  2  },
{'event_date': datetime (1912,3,12) , 'trips':  1  },
{'event_date': datetime (1912,3,13) , 'trips':  1  },
{'event_date': datetime (1912,3,14) , 'trips':  2  },
{'event_date': datetime (1912,3,15) , 'trips':  2  },
{'event_date': datetime (1912,3,16) , 'trips':  2  },
{'event_date': datetime (1912,3,17) , 'trips':  2  },
{'event_date': datetime (1912,3,18) , 'trips':  2  },
{'event_date': datetime (1912,3,19) , 'trips':  2  },
{'event_date': datetime (1912,3,20) , 'trips':  2  },
{'event_date': datetime (1912,3,21) , 'trips':  2  },
{'event_date': datetime (1912,3,22) , 'trips':  2  },
{'event_date': datetime (1912,3,23) , 'trips':  2  },
{'event_date': datetime (1912,3,24) , 'trips':  0  },
{'event_date': datetime (1912,4,1), 'trips':    0  },
{'event_date': datetime (1912,4,2), 'trips':    0  },
{'event_date': datetime (1912,4,3), 'trips':    0  },
{'event_date': datetime (1912,4,4), 'trips':    0  },
{'event_date': datetime (1912,4,5)  , 'trips':  0  },
{'event_date': datetime (1912,4,6)  , 'trips':  0  },
{'event_date': datetime (1912,4,7)  , 'trips':  2  },
{'event_date': datetime (1912,4,8)  , 'trips':  2  },
{'event_date': datetime (1912,4,9)  , 'trips':  2  },
{'event_date': datetime (1912,4,10) , 'trips':  2  },
{'event_date': datetime (1912,4,11) , 'trips':  2  },
{'event_date': datetime (1912,4,12) , 'trips':  1  },
{'event_date': datetime (1912,4,13) , 'trips':  1  },
{'event_date': datetime (1912,4,14) , 'trips':  2  },
{'event_date': datetime (1912,4,15) , 'trips':  2  },
{'event_date': datetime (1912,4,16) , 'trips':  2  },
{'event_date': datetime (1912,4,17) , 'trips':  2  },
{'event_date': datetime (1912,4,18) , 'trips':  2  },
{'event_date': datetime (1912,4,19) , 'trips':  2  },
{'event_date': datetime (1912,4,20) , 'trips':  2  },
{'event_date': datetime (1912,4,21) , 'trips':  2  },
{'event_date': datetime (1912,4,22) , 'trips':  2  },
{'event_date': datetime (1912,4,23) , 'trips':  2  },
{'event_date': datetime (1912,4,24) , 'trips':  0  },
{'event_date': datetime (1912,5,1), 'trips':    0  },
{'event_date': datetime (1912,5,2), 'trips':    0  },
{'event_date': datetime (1912,5,3), 'trips':    0  },
{'event_date': datetime (1912,5,4), 'trips':    0  },
{'event_date': datetime (1912,5,5)  , 'trips':  0  },
{'event_date': datetime (1912,5,6)  , 'trips':  0  },
{'event_date': datetime (1912,5,7)  , 'trips':  2  },
{'event_date': datetime (1912,5,8)  , 'trips':  2  },
{'event_date': datetime (1912,5,9)  , 'trips':  2  },
{'event_date': datetime (1912,5,10) , 'trips':  2  },
{'event_date': datetime (1912,5,11) , 'trips':  2  },
{'event_date': datetime (1912,5,12) , 'trips':  1  },
{'event_date': datetime (1912,5,13) , 'trips':  1  },
{'event_date': datetime (1912,5,14) , 'trips':  2   },
{'event_date': datetime (1912,5,15) , 'trips':  2  },
{'event_date': datetime (1912,5,16) , 'trips':  2  },
{'event_date': datetime (1912,5,17) , 'trips':  2  },
{'event_date': datetime (1912,5,18) , 'trips':  2  },
{'event_date': datetime (1912,5,19) , 'trips':  2  },
{'event_date': datetime (1912,5,20) , 'trips':  2  },
{'event_date': datetime (1912,5,21) , 'trips':  2  },
{'event_date': datetime (1912,5,22) , 'trips':  2  },
{'event_date': datetime (1912,5,23) , 'trips':  2  },
{'event_date': datetime (1912,5,24) , 'trips':  0  },
{'event_date': datetime (1912,6,1), 'trips':    0  },
{'event_date': datetime (1912,6,2), 'trips':    0  },
{'event_date': datetime (1912,6,3), 'trips':    0  },
{'event_date': datetime (1912,6,4), 'trips':    0  },
{'event_date': datetime (1912,6,5)  , 'trips':  0  },
{'event_date': datetime (1912,6,6)  , 'trips':  0  },
{'event_date': datetime (1912,6,7)  , 'trips':  2  },
{'event_date': datetime (1912,6,8)  , 'trips':  2  },
{'event_date': datetime (1912,6,9)  , 'trips':  2  },
{'event_date': datetime (1912,6,10) , 'trips':  2  },
{'event_date': datetime (1912,6,11) , 'trips':  2  },
{'event_date': datetime (1912,6,12) , 'trips':  1  },
{'event_date': datetime (1912,6,13) , 'trips':  1  },
{'event_date': datetime (1912,6,14) , 'trips':  2  },
{'event_date': datetime (1912,6,15) , 'trips':  2  },
{'event_date': datetime (1912,6,16) , 'trips':  2  },
{'event_date': datetime (1912,6,17) , 'trips':  2  },
{'event_date': datetime (1912,6,18) , 'trips':  2  },
{'event_date': datetime (1912,6,19) , 'trips':  2  },
{'event_date': datetime (1912,6,20) , 'trips':  2  },
{'event_date': datetime (1912,6,21) , 'trips':  2  },
{'event_date': datetime (1912,6,22) , 'trips':  2  },
{'event_date': datetime (1912,6,23) , 'trips':  2  },
{'event_date': datetime (1912,6,24) , 'trips':  0  },
{'event_date': datetime (1912,7,1), 'trips':    0  },
{'event_date': datetime (1912,7,2), 'trips':    0  },
{'event_date': datetime (1912,7,3), 'trips':    0  },
{'event_date': datetime (1912,7,4), 'trips':    0  },
{'event_date': datetime (1912,7,5)  , 'trips':  0  },
{'event_date': datetime (1912,7,6)  , 'trips':  0  },
{'event_date': datetime (1912,7,7)  , 'trips':  2  },
{'event_date': datetime (1912,7,8)  , 'trips':  2  },
{'event_date': datetime (1912,7,9)  , 'trips':  2  },
{'event_date': datetime (1912,7,10) , 'trips':  2  },
{'event_date': datetime (1912,7,11) , 'trips':  2  },
{'event_date': datetime (1912,7,12) , 'trips':  1  },
{'event_date': datetime (1912,7,13) , 'trips':  1  },
{'event_date': datetime (1912,7,14) , 'trips':  2  },
{'event_date': datetime (1912,7,15) , 'trips':  2  },
{'event_date': datetime (1912,7,16) , 'trips':  2  },
{'event_date': datetime (1912,7,17) , 'trips':  2  },
{'event_date': datetime (1912,7,18) , 'trips':  1  },
{'event_date': datetime (1912,7,19) , 'trips':  1  },
{'event_date': datetime (1912,7,20) , 'trips':  0  },
{'event_date': datetime (1912,7,21) , 'trips':  0  },
{'event_date': datetime (1912,7,22) , 'trips':  0  },
{'event_date': datetime (1912,7,23) , 'trips':  0  },
{'event_date': datetime (1912,7,24) , 'trips':  0  }
]

my_data_epoched = [{'days_since_epoch': mymidi.days_since_epoch(d['event_date']), 'trips': d['trips']} for d in my_data]

my_data_timed = [{'beat': mymidi.beat(d['days_since_epoch']), 'trips': d['trips']} for d in my_data_epoched]

start_time = my_data_timed[0]['beat']

def mag_to_pitch_tuned(trips):
    scale_pct = mymidi.linear_scale_pct(0, 2, trips)
    # Pick a range of notes. This allows you to play in a key.
    c_major = ['C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'B#']

    #Find the note that matches your data point
    note = mymidi.scale_to_note(scale_pct, c_major)

    #Translate that note to a MIDI pitch
    midi_pitch = mymidi.note_to_midi_pitch(note)

    return midi_pitch

note_list = []

for d in my_data_timed:
    note_list.append([
        d['beat'] - start_time,
        mag_to_pitch_tuned(d['trips']),
        random.randint(0,200),  # attack
        random.randint(1,4)  # duration, in beats
    ])

# Add a track with those notes
mymidi.add_track(note_list)

# Output the .mid file
mymidi.save_midi()