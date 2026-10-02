# Visualizing Data with Matplotlib -- Code 8.3: Vertical bar chart
# (book source: ch08_matplotlib.tex, line 348)

import matplotlib.pyplot as plt

subjects = ['Maths', 'Physics', 'Chemistry', 'Biology']
scores   = [88, 75, 92, 67]

fig, ax = plt.subplots()
ax.bar(subjects, scores, color='steelblue', edgecolor='white')
ax.set_ylim(0, 100)
ax.set_ylabel('Score (%)')
ax.set_title('Exam Results')
fig.savefig('bar_chart.pdf', bbox_inches='tight')
plt.show()
