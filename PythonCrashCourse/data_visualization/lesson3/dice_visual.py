from die import Die
import pygal

die_1 = Die()
die_2 = Die()

res = []

for roll_num in range(1000):
    re = die_1.roll() + die_2.roll()
    res.append(re)

frequencies = []
for value in range(2, (die_1.num_sides+die_2.num_sides+1)):
    frequency = res.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."

hist.x_labels = [str(x) for x in range(2,(die_1.num_sides+die_2.num_sides+1))]

hist.x_title = "result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)

hist.render_to_file('./dice_visual.svg')

