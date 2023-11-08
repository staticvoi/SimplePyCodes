# modules in same directory

# import mymodule
# mymodule.cal_cube(3)
import mymodule as mod
mod.cal_cube(2)
mod.cal_square(2)


# modules in another sub folder
# import foldername.mymodule as mod
# mod.cal_cube(2)

# modules in totally diff path in system

import sys
sys.path.append("C:\Code") # append this path to system path as my module is there
import mymodule as mod
mod.cal_cube(2)
mod.cal_square(2)
