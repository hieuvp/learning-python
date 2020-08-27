import sys
from pprint import pprint

# Add "/foo" directory
# to the list of paths to look for modules
sys.path.append("/foo")

pprint(sys.path)
