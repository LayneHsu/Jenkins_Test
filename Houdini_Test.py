import hou

# Get scene root node
sceneRoot = hou.node('/obj/')

# Create empty geometry node in scene root
geometry = sceneRoot.createNode('geo', run_init_scripts=False)

# Set geometry node name
geometry.setName('MY_GEO')

geometry.createNode('box',"my_box")

hou.hipFile.save("C:\Users\LayneHsu\Desktop\My_box.hip", save_to_recent_files=True)
