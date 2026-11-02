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


