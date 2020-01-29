:: Please configure these:
SET VPK_EXE=D:\_steam\steamapps\common\Source SDK Base 2013 Multiplayer\bin\vpk.exe
:: The path to where all the unpacked content is.
SET CONTENT_DIR=D:\_assets_build\


python ..\vpk_generator.py --vpk "%VPK_EXE%" --dir "%CONTENT_DIR%" --vpk_params="-M" --name assets_ep2 --responsefile response_ep2.txt

