# Example Content

This directory contains example content for exporting animations from Maya to Unreal.  
You should be familiar with the basics of NXT as explained by [our tutorials](https://nxt-dev.github.io/tutorials/).  
To download a zip of this repo [click here](https://github.com/nxt-dev/examples/archive/master.zip)  

_The structure and content of these examples may change at any time without notice. It is best to copy these files out of the repository and put them somewhere sensible on your computer._

# Maya FBX Export
To get the example scene and export graph open simply do the following:
1. Open `assets/man/anim/data/base/walk/man_base_walk_anim.ma` in Maya
   - Fix the rig reference, the rig is located at `maya_ue_fbx_demo/assets/man/rig/data/base/man_base_rig.ma`
2. Open the NXT editor in Maya
3. In NXT open the graph `export_fbx.nxt`

You can now export the animation by executing the graph. Click around to the various nodes to read their comments and code to get a taste for how the graph works.

# Multi-context (Maya > NXT > Unreal)

With the right setup, this examples provides a 1 click export from maya that opens unreal headlessly and imports the animation that was just exported.

### Setup
1. Edit `unreal_context/unreal_context.py` and correct the unreal path and project path to your downloaded location.
2. Take the contents `unreal_context` folder and place them in your nxt plugins directory. https://nxt-dev.github.io/extensions/#in-depth-explanations
3. Install the nxt plugin into the provided unreal project. `nxt_unreal_demo.uproject`

### Demo
1. Open the maya file `assets\man\anim\data\base\walk\man_base_walk_anim.ma`
2. Open the NXT editor within Maya, and open `maya_to_unreal.nxt`
3. Edit the animation in any way you like, there is an animation layer called `GiantHand` for quick testing.
4. Run the `maya_to_unreal` graph from the start point `/start_export`(should be default option in build window).
5. Open unreal to see the results!

In order to launch directly into a window of the game(skipping the editor), open a command prompt run the following with paths updated for your machine.
`"C:/Program Files/Epic Games/UE_4.26/Engine/Binaries/Win64/UE4Editor-Cmd.exe" Z:/Projects/nxt/examples/maya_ue_fbx_demo/game/nxt_unreal_demo.uproject -game`

