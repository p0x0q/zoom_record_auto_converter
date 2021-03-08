# zoom_record_auto_converter

.zoomファイルが存在するフォルダーと，Zoomインストール時に同梱されるzTscoder.exeを指定して，全ての.zoomファイルを動画ファイルに変換するPythonスクリプトです．

optional arguments:

  -h, --help            show this help message and exit
  
  --record-path RECORD_PATH  
  
                        Example: C:\Users\p0x0q\Documents\Zoom(Location folder of the .zoom file) (default: None)
                        
  --check-process-time CHECK_PROCESS_TIME
  
                        checking for process time(sec) (default: 10)
                        
  --convert-path CONVERT_PATH
  
                        Example: C:\Users\p0x0q\AppData\Roaming\Zoom\bin\zTscoder.exe (Location of the zTscoder.exefile) (default: None)
                        
                        
and:

the following arguments are required: --record-path, --convert-path
