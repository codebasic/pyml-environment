import sys, platform

import numpy as np
import pandas as pd
import matplotlib
import sklearn

print('OS', platform.system(), platform.release())
print("Python version: {}".format(sys.version))
print("Numpy version: {}".format(np.__version__))
print("Pandas version: {}".format(pd.__version__))
print("Matplotlib version: {}".format(matplotlib.__version__))
print("Scikit-learn version: {}".format(sklearn.__version__))
