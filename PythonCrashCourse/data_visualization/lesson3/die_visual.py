from die import Die
import pygal

die_1 = Die()
# die_2 = Die()

res = []

for roll_num in range(1000):
    re = die_1.roll()
    res.append(re)

frequencies = []
for value in range(1, die_1.num_sides+1):
    frequency = res.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."

hist.x_labels = [str(x) for x in range(1,die_1.num_sides+1)]

hist.x_title = "result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)

hist.render_to_file('./die_visual.svg')

