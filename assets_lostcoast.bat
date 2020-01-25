:: Please configure this:
SET VPK_EXE=D:\_steam\steamapps\common\Source SDK Base 2013 Multiplayer\bin\vpk.exe
SET CONTENT_DIR=assets_lostcoast


python vpk_generator.py --vpk "%VPK_EXE%" --dir "%CONTENT_DIR%" --include @files_lostcoast.txt --vpk_params="-M" --name assets_lostcoast --responsefile response_lostcoast.txt

