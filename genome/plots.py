import matplotlib.pyplot as plt

names = ['USDA chr', 'USDA pls', 'MJO3', 'PUBIS chr', 'PUBIS pls']
values = [28.5, 35.2, 28.5, 24.2, 19.5]
colors = ['blue', 'blue', 'red', 'green', 'green']

plt.figure(figsize=(9, 5))

plt.ylim([0, 100])
plt.xlabel('Genomes')
plt.ylabel('Percentage of GC')
plt.title('% GC Content in Genomes', fontsize=14)
plt.bar(names, values, color=colors)
plt.grid(True)
plt.savefig('GC_Content.png')
plt.show()

