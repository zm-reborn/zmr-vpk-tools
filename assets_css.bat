:: Please configure this:
SET VPK_EXE=D:\_steam\steamapps\common\Source SDK Base 2013 Multiplayer\bin\vpk.exe
SET CONTENT_DIR=assets_css


python vpk_generator.py --vpk "%VPK_EXE%" --dir "%CONTENT_DIR%" --include @files_css.txt --vpk_params="-M" --name assets_css --responsefile response_css.txt

