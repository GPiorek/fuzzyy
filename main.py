
import simpful as sf
import tkinter as tk

import random
import time

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

stones = [{"x": 1, "y": 2, "size": 3}]
for _ in range(4):
    prev = stones[-1]
    stones.append({
        "x": prev["x"] + prev["size"] + random.randint(1, 3),
        "y": max(1, min(5, prev["y"] + random.randint(-2, 2))),
        "size": random.randint(1, 3),
    })

CELL = 40
H = 9 * CELL

root = tk.Tk()
canvas = tk.Canvas(root, width=30 * CELL, height=H)
canvas.pack()

for s in stones:
    for k in range(s["size"]):
        x = (s["x"] + k) * CELL
        y = H - s["y"] * CELL
        canvas.create_rectangle(x, y, x + CELL, y + CELL, fill="gray")

hero_x = stones[0]["x"]
hero_y = stones[0]["y"]
hero = canvas.create_rectangle(0, 0, CELL, CELL, fill="red")


def put_hero(x, y):
    left = x * CELL
    top = H - (y + 1) * CELL
    canvas.coords(hero, left, top, left + CELL, top + CELL)


put_hero(hero_x, hero_y)
canvas.update()
time.sleep(1)

for i in range(len(stones) - 1):
    nxt = stones[i + 1]

    dx = nxt["x"] - hero_x
    dy = nxt["y"] - hero_y
    reach = round(jump_force(dx, dy, nxt["size"]) * 10)
    new_x = hero_x + reach - dy
    new_y = nxt["y"]

    for step in range(21):
        t = step / 20
        x = hero_x + (new_x - hero_x) * t
        y = hero_y + (new_y - hero_y) * t + 8 * t * (1 - t)
        put_hero(x, y)
        canvas.update()
        time.sleep(0.03)

    hero_x = new_x
    hero_y = new_y
    time.sleep(0.5)

root.mainloop()