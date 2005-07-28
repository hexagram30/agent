from imagination.deployment import deploy

import sys
sys.path.append('.')
sys.path.append('/Users/oubiwann/Adytum/Projects/RookSaga/games/CursesTheRookses/lib/games/rookcurses/TRDemo')
print sys.path

import trmap
actorTemplate = trmap.ActorTemplate

d = {}
execfile("config", {}, d)

print d
application = deploy(**d)
