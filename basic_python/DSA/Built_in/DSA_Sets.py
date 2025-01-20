from os import setsid
import numpy as np

engineers = set(["Jtestn", "Jane", 'Jack', "Janice"])

# UNION OPERATIONS IN sets

samson = set(["Jtestn", "Jane"])

samson | engineers = > {'Jack', 'Jane', 'Janice', 'Jtestn'}
np.union1d(samson, engineers) = > {'Jack', 'Jane', 'Janice', 'Jtestn'}
ste3 = samson.union(engineers) = > call ste3 {'Jack', 'Jane', 'Janice', 'Jtestn'}
samson.update(engineers) = > call samson will updated value = > {'Jack', 'Jane', 'Janice', 'Jtestn'}


# INTERSECTION OPERATIONS

samson & engineers = > {'Jane', 'Jtestn'}


# SET DIFFERENCES
engineers.difference(samson) = > {'Jack', 'Janice'}

# ADDING VALUES to SET
samson.add("Kunle") = > {'Jane', 'Jtestn', 'Kunle'}

# Remove or Pop()
samson.pop() = > removes the first set
samson.remove(100) = > removes specific value as specified.

# DIFFERENCE_UPDATE
# This removes what is common an returns the difference from the main set
samson.difference_update(engineers) = >
