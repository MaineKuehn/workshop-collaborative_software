import random

def pad(literal):
    if not literal:
        return "  \n  "
    lines = ['', *literal.splitlines(), '']
    width = max(len(line) for line in lines)
    return '\n'.join(' ' + line.ljust(width) + ' ' for line in lines)


BLOCK = pad("""\
##
##
""")

BLINKER = pad("""\

###

""")

BLINKER3 = pad("""\
     #
###  # ###
     #
""")

PULSAR = pad("""\
  ###

#    #
#    #
#    #
  ###
""")

PENTADECATHLON = pad("""\
  #  #    # #
###  ###### ###
  #  #    # #
""")

PINWHEEL = pad("""\
 ####
#  # #
##   #
# #  #
#    #
 ####
""")

GLIDER = pad("""\
 #
  #
###
""")

DIEHARD = pad("""\
      #
##
 #   ###
""")

GLIDER_GUN = pad("""\
                        #
                      # #
            ##      ##            ##
           #   #    ##            ##
##        #     #   ##
##        #   # ##    # #
          #     #       #
           #   #
            ##
""")

PENTOMINO = pad("""\
 ##
##
 #
""")

BASELINE = pad("""\
######## #####   ###      ####### #####
""")

RANDOM = pad('\n'.join([''.join([random.choice(['#', ' ']) for i in range(100)]) for j in range(100)]))

PATTERNS = [
    'BLOCK', 'BLINKER', 'BLINKER3', 'PULSAR', 'PENTADECATHLON', 'PINWHEEL', 'GLIDER', 'DIEHARD', 'GLIDER_GUN',
    'PENTOMINO', 'RANDOM'
]

__all__ = PATTERNS[:]
