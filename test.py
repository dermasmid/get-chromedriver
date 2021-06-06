import sys
import os
sys.path.insert(0, '/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1]))

import get_chromedriver

get_chromedriver.download_chromedriver()
