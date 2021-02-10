import os
from nxt.remote.contexts import RemoteContext, register_context

exe_path = 'C:/Program Files/Epic Games/UE_4.26/Engine/Binaries/Win64/UE4Editor-Cmd.exe'
graph_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'unreal_context.nxt'))
graph_path = graph_path.replace(os.path.sep, '/')
command = exe_path + ''' "Z:/Projects/nxt/examples/maya_ue_fbx_demo/game/nxt_unreal_demo.uproject" -run=pythonscript -script="{cli_path} {cli_args}"'''
unreal_context = RemoteContext('unreal', command, graph_path)
register_context(unreal_context)