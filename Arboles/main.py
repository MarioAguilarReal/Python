# arbol={
#     "value" : 4,
#     "left":{
#         "value":11,
#         "left": None,
#         "right" : None
#     },
#     "right":{
#         "value":23,
#         "left": None,
#         "right":None
#     }

# }

from Clases.Arbol import Arbol

a = Arbol()

a.insert(10)
a.insert(12)
a.insert(14)
a.insert(13)
a.print()

