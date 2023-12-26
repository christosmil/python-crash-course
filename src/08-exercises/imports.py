# Import a module.
import shirt

shirt.make_shirt('small', 'Luke, I am your father.')

# Import a specific function of a module.
from shirt import make_shirt

make_shirt('medium', 'I have a bad feeling about this.')

# Import a spefic function from a module with alias.
from shirt import make_shirt as ms

ms('large', 'May the force be with you.')

# Import a module with alias.
import shirt as sh

sh.make_shirt('extra large', 'A long time ago in a galaxy far away.')

# Import all function from a module.
from shirt import *

make_shirt('extra extra large', 'Hello, there!')