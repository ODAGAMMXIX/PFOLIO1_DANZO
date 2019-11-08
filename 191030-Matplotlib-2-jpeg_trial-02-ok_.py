import io
import sqlite3
import numpy as np
import pandas as pd
import image
import matplotlib.pyplot as plt
#import matplotlib.pyplot.savefig(fname=olhaissomano, dpi=None, facecolor='w', edgecolor='w',orientation='portrait', papertype=None, format=None,transparent=False, bbox_inches=None, pad_inches=0.1,frameon=None, metadata=None)

#plt.plot(range(10))
#plt.savefig('testplot.png')
#image.open('testplot.png').save('C:\\DANZO\\repository\\testplot.jpg','JPEG')

plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])
plt.xlabel('Months')
plt.ylabel('Books Read')
plt.show()
plt.savefig('books_read.png')

