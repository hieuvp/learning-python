import re

# Slight optimization
pattern = re.compile(r"\[(on|off)\]")

# Returning a matched object
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))

# Doesn't return anything
print(re.search(pattern, "Nada...:-("))
