import math

print ('The value of PI is approximately {}.'.format(str(math.pi).ljust(4)[:4]))
print ('The value of PI is approximately {0:.3f}.'.format(math.pi))
print ('The value of PI is approximately %6.3f.' % math.pi)

from pathlib import Path
contents = Path(file_path).read_text()