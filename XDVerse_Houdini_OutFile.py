import hou

# Get scene root node
sceneRoot = hou.node('/obj/')

# Create empty geometry node in scene root
geometry = sceneRoot.createNode('geo', run_init_scripts=False)

# Set geometry node name
geometry.setName('MY_GEO')

geometry.createNode('box',"my_box")

hou.hipFile.save("E:\Work\XD_Work\Houdini\Projects\PCG_Pipeline\Working_Dir\geo\XDVerse_Houdini_OutFile.hip", save_to_recent_files=True)
