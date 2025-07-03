from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.analysis.analysis import Analysis
# Import Graphviz
from graphviz import Digraph

# Build a customer app with https://www.andromo.com/

# Load the APK
# a = APK("/Users/s.eromonsei/Downloads/app_3419487_2366305.apk")
apk_path = APK("/Users/s.eromonsei/Downloads/cat.game.liftapp_29_apps.evozi.com.apk")

# Get information about the app
print("Package Name:", apk_path.get_package())
print("Permissions:", apk_path.get_permissions())

# Load the DEX file
d = DalvikVMFormat(apk_path.get_dex())


# Analyze the DEX code
dx = Analysis(d)


# Visualize AST with Graphviz
ast_graph = Digraph('AST')
for method in d.get_methods():
    ast_graph.node(method.get_name())
    dalvik_code = method.get_code()
    if dalvik_code:
            basic_blocks = BasicBlocks(dalvik_code)
            for block in basic_blocks.get():
                ast_graph.node(str(block))
                ast_graph.edge(method.get_name(), str(block))

ast_graph.render('ast_graph', format='png', cleanup=True)



# Visualize CFG with Graphviz
cfg_graph = Digraph('CFG')
for method in d.get_methods():
    cfg_graph.node(method.get_name())
    dalvik_code = method.get_code()
    if dalvik_code:
        for block in dalvik_code.basic_blocks.get():
            cfg_graph.node(str(block))
            cfg_graph.edge(method.get_name(), str(block))
            for child in block.childs:
                cfg_graph.node(str(child))
                cfg_graph.edge(str(block), str(child))

cfg_graph.render('cfg_graph', format='png', cleanup=True)


# Analyze the DEX code / intermediate representation
#Yes, that's correct. DEX (Dalvik Executable) code is an 
# intermediate representation used by the Dalvik Virtual Machine,
#  which is the runtime environment used in Android for executing applications

for method in d.get_methods():
    print("Method:", method.get_name())
    print("Instructions:")
    for ins in method.get_instructions():
        print(ins)

# Extract all the Class Methods
with open('classMethods.txt', "w") as f:
  for class_data in d.get_classes():
        class_name = class_data.get_name()
        for method in class_data.get_methods():
            # Concatenate the class name and method name for clarity
            full_method_name = f"{class_name}.{method.get_name()}"
            #all_methods.append(full_method_name)
            f.write(full_method_name + "\n")


# Perform static analysis

dx = Analysis(d)

# Get the call graph

call_graph = dx.get_call_graph()
print("Call graph:", call_graph)

#Print the call graph

for node in call_graph.nodes:
    print(f"Method: {node}")
    for neighbor in call_graph.neighbors(node):
        print(f"  Calls: {neighbor}")

        graph.edge(node, neighbor)


# Save the Graphviz output to a file (e.g., in PNG format)
graph.render("call_graph", format="png", cleanup=True)

# Optionally, you can also view the generated graph
graph.view()