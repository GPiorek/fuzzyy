import simpful as sf

FS = sf.FuzzySystem(show_banner=False)

#DX
near = sf.FuzzySet(points=[[0, 1], [4, 0]], term="near")
mid = sf.FuzzySet(points=[[0, 0], [4, 1], [8, 0]], term="mid")
far = sf.FuzzySet(points=[[4, 0], [8, 1], [10, 1]], term="far")
FS.add_linguistic_variable("dx", sf.LinguisticVariable([near, mid, far]))

#DY
down = sf.FuzzySet(points=[[-3, 1], [0, 0]], term="down")
flat = sf.FuzzySet(points=[[-3, 0], [0, 1], [3, 0]], term="flat")
up = sf.FuzzySet(points=[[0, 0], [3, 1]], term="up")
FS.add_linguistic_variable("dy", sf.LinguisticVariable([down, flat, up]))

#WD
small = sf.FuzzySet(points=[[1, 1], [2, 0]], term="small")
med = sf.FuzzySet(points=[[1, 0], [2, 1], [3, 0]], term="med")
big = sf.FuzzySet(points=[[2, 0], [3, 1]], term="big")
FS.add_linguistic_variable("wd", sf.LinguisticVariable([small, med, big]))

dx_words = ["near", "mid", "far"]
dy_words = ["down", "flat", "up"]
wd_words = ["small","med", "big"]

dx_range = {"near": 0, "mid": 4, "far": 8}
dy_range = {"down": -3,"flat": 0,"up": 3}
wd_range = {"small": 0,"med": 0.5,"big": 1}

for a in dx_words:
    for b in dy_words:
        for c in wd_words:
            name = f"F_{a}_{b}_{c}"
            reach = dx_range[a] + dy_range[b] + wd_range[c]
            f = max(0, min(1, reach / 10))
            FS.set_crisp_output_value(name, f)
            rule = f"IF(dx IS {a}) AND (dy IS {b}) AND (wd IS {c}) THEN (F IS {name})"
            FS.add_rules([rule])

def jump_force(dx, dy, wd):
    FS.set_variable("dx", dx)
    FS.set_variable("dy", dy)
    FS.set_variable("wd", wd)
    return FS.Sugeno_inference(["F"])["F"]
