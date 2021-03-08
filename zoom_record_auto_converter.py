import subprocess
import glob
import argparse
import time
import os

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

parser.add_argument(
    "--record-path",
    required=True,
    help="Example: C:\\Users\\p0x0q\\Documents\\Zoom(Location folder of the .zoom file)"
)
parser.add_argument(
    "--check-process-time",
    required=False,
    default=10,
    help="checking for process time(sec)"
)
parser.add_argument(
    "--convert-path",
    required=True,
    help="Example: C:\\Users\\p0x0q\\AppData\\Roaming\\Zoom\\bin\\zTscoder.exe (Location file of the zTscoder.exe file)"
)

args = parser.parse_args()

def is_waiting():
    cmd = 'tasklist'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if "zTscoder" in str(line):
            return True
    return False
def waiting():
    if is_waiting() == False:
        return
    else:
        time.sleep(args.check_process_time)
        waiting()

for filepath in glob.glob(args.record_path + r"\**\*"):
    if ".zoom" in filepath:
        print("Waiting for zTscoder to finish..")
        waiting()
        if os.path.exists(filepath):
            print("converting: " + filepath)
            cmd = args.convert_path+ ' ' + filepath
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)