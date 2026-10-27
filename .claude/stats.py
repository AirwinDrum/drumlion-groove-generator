import re, math

RAW_161 = [
    [121,131,141,151],[121,131,142,152],[121,131,143,153],[121,132,144,154],
    [121,132,145,155],[121,132,146,155],[121,133,147,156],[121,133,148,157],
    [121,133,149,158],[122,134,150,159],[122,134,151,159],[122,134,151,160],
    [122,135,152,161],[122,135,152,162],[122,135,153,163],[122,136,153,163],
    [122,136,154,164],[122,136,154,165],[123,137,155,166],[123,137,155,167],
    [123,137,156,167],[123,138,156,168],[123,138,157,169],[123,138,157,170],
    [123,139,158,171],[123,139,158,171],[123,139,159,172],[124,140,159,173],
    [124,140,160,174],[124,140,160,175],[124,141,161,176],[124,141,161,177],
    [124,141,162,178],[124,142,162,179],[124,142,163,180],[124,142,163,181],
    [125,143,164,182],[125,143,164,183],[125,143,165,184],[125,144,165,185]
]
RAW_201 = [
    [125,144,166,185],[125,144,166,186],[125,145,167,187],[125,145,167,188],
    [125,145,168,189],[126,146,168,189],[126,146,169,190],[126,146,169,191],
    [126,147,170,192],[126,147,170,193],[126,147,171,193],[126,148,171,194],
    [126,148,172,195],[126,148,172,196],[127,149,173,197],[127,149,173,197],
    [127,149,174,198],[127,150,174,199],[127,150,175,200],[127,150,175,201],
    [127,151,176,201],[127,151,176,202],[127,151,177,203],[128,152,177,204],
    [128,152,178,205],[128,152,178,205],[128,153,179,206],[128,153,179,207],
    [128,153,180,208],[128,154,180,209],[128,154,181,209],[128,154,181,210],
    [129,155,182,211],[129,155,182,212],[129,155,183,213],[129,156,183,213],
    [129,156,184,214],[129,156,184,215],[129,157,185,216],[129,157,185,217],
    [129,157,186,217],[130,158,186,218],[130,158,187,218],[130,158,187,218],
    [130,159,188,219],[130,159,188,219],[130,159,189,219],[130,160,189,220],
    [130,160,190,220],[130,160,190,220]
]

def get_bars(bpm, base_dur):
    return math.ceil(bpm * base_dur / 60 / 4 / 4) * 4

def get_blocks(t):
    if   t <= 50:  bpms=[t];                      durs=[30]
    elif t <= 70:  bpms=[t];                      durs=[40]
    elif t <= 80:  bpms=[t];                      durs=[50]
    elif t <= 90:  bpms=[t-10,t];                 durs=[50,60]
    elif t <= 100: bpms=[t-20,t-10,t];            durs=[40,50,60]
    elif t <= 110: bpms=[t-30,t-20,t-10,t];       durs=[30,40,50,60]
    elif t <= 160: bpms=[t-40,t-30,t-20,t-10,t]; durs=[20,30,40,50,60]
    elif t <= 200:
        r=RAW_161[t-161]; bpms=[r[0],r[1],r[2],r[3],t]; durs=[20,30,40,50,60]
    elif t <= 250:
        r=RAW_201[t-201]; bpms=[r[0],r[1],r[2],r[3],t]; durs=[20,30,40,50,60]
    else:          bpms=[t-120,t-90,t-60,t-30,t]; durs=[20,30,40,50,60]
    return sum(get_bars(b,d)*4*60/b for b,d in zip(bpms,durs))

def get_pauses(t):
    if t <= 80:  return 0
    if t <= 90:  return 15
    if t <= 100: return 25
    if t <= 110: return 35
    if t <= 160: return 45
    if t <= 200: return 55
    if t <= 250: return 70
    return 90

def lesson_secs(minBPM, maxBPM, step):
    total, t = 0, minBPM
    while t <= maxBPM:
        total += get_blocks(t) + get_pauses(t)
        t += step
    return total

with open('/Users/erwineitsen/Desktop/Projekte/Drumlion/groove-generator/index.html', 'r') as f:
    html = f.read()

chunks = re.split(r'\{id:\d+,', html)
by_cat = {}

for chunk in chunks[1:]:
    cat_m   = re.search(r"cat:'(\w+)'", chunk)
    min_m   = re.search(r"minBPM:(\d+)", chunk)
    max_m   = re.search(r"maxBPM:(\d+)", chunk)
    step_m  = re.search(r"\bstep:(\d+)", chunk)
    label_m = re.search(r"catLabel:'([^']+)'", chunk)
    if not (cat_m and min_m and max_m and step_m): continue
    minBPM,maxBPM,step = int(min_m.group(1)),int(max_m.group(1)),int(step_m.group(1))
    label = label_m.group(1) if label_m else cat_m.group(1)
    steps = (maxBPM-minBPM)//step+1
    secs  = lesson_secs(minBPM, maxBPM, step)
    if label not in by_cat:
        by_cat[label] = {'lessons':0,'steps':0,'secs':0,'min':minBPM,'max':maxBPM,'step':step}
    by_cat[label]['lessons'] += 1
    by_cat[label]['steps']   += steps
    by_cat[label]['secs']    += secs

order = ['Basic Grooves 1','Basic Grooves 2','Hi-Hat Openings 1','Hi-Hat Openings 2',
         'Downbeat Accents','Upbeat Accents','Quarter Fills','Eighth Note Fills','Rudiments']

print(f"{'Kategorie':<25} {'BPM':<12} {'Step':>4} {'Schritte':>8} {'Stunden':>8}")
print("-" * 60)
total_steps=0; total_secs=0
for cat in order:
    if cat not in by_cat: continue
    v = by_cat[cat]
    print(f"{cat:<25} {v['min']}-{v['max']:<11} {v['step']:>4} {v['steps']:>8} {v['secs']/3600:>7.1f}h")
    total_steps += v['steps']; total_secs += v['secs']
print("-" * 60)
print(f"{'GESAMT':<42} {total_steps:>8} {total_secs/3600:>7.1f}h")
