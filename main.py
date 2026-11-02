import simpful as sf

FS = sf.FuzzySystem(show_banner=False)

#DX
near = sf.FuzzySet(points=[[0, 1], [4, 0]], term="near")
mid = sf.FuzzySet(points=[[0, 0], [4, 1], [8, 0]], term="mid")
far = sf.FuzzySet(points=[[4, 0], [8, 1], [10, 1]], term="far")
FS.add_linguistic_variable("dx", sf.LinguisticVariable([near, mid, far]))

print(near.get_value(3), mid.get_value(3), far.get_value(3))

FS.set_crisp_output_value("F_NEAR", 0)
FS.set_crisp_output_value("F_MID", 0.4)
FS.set_crisp_output_value("F_FAR", 0.8)

RULE1 = "IF (dx IS near) THEN (F IS F_NEAR)"
RULE2 = "IF (dx IS mid) THEN (F IS F_MID)"
RULE3 = "IF (dx IS far) THEN (F IS F_FAR)"
FS.add_rules([RULE1, RULE2, RULE3])

#test
FS.set_variable("dx", 3)
print(FS.Sugeno_inference(["F"]))

#DY
down = sf.FuzzySet(points=[[-3, 1], [0, 0]], term="down")
flat = sf.FuzzySet(points=[[-3, 0], [0, 1], [3, 0]], term="flat")
up = sf.FuzzySet(points=[[0, 0], [3, 1]], term="up")
FS.add_linguistic_variable("dy", sf.LinguisticVariable([down, flat, up]))

#test
print(down.get_value(-1), flat.get_value(-1), up.get_value(-1))


#WD
small = sf.FuzzySet(points=[[1, 1], [2, 0]], term="small")
med = sf.FuzzySet(points=[[1, 0], [2, 1], [3, 0]], term="med")
big = sf.FuzzySet(points=[[2, 0], [3, 1]], term="big")
FS.add_linguistic_variable("wd", sf.LinguisticVariable([small, med, big]))

#test
print(small.get_value(1.5), med.get_value(1.5), big.get_value(1.5))