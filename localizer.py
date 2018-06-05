import os
import sys
import csv
import json

from ios_localizer import start_localize_ios
from android_localizer import start_localize_android
from json_localizer import start_localize_json
from properties_localizer import start_localize_properties

CURRENT_DIR = os.path.dirname(__file__)

def main():
  print "Localizing...."
  # Load Settings File
  with open(os.path.join(CURRENT_DIR, "config.json")) as setting_file:
    setting = json.load(setting_file)

    PLATFORM = setting["PLATFORM"]
    IN_PATH = setting["IN_PATH"]
    OUT_PATH = setting["OUT_PATH"]
    LANG_KEYS = setting["LANG_KEYS"]
    BASE_STRINGS_PATH = setting["BASE_STRINGS_PATH"]
    
    if BASE_STRINGS_PATH == "currentdir":
      print "Detect currentdir -> \n  " + CURRENT_DIR
      BASE_STRINGS_PATH = CURRENT_DIR

    print "In path: {0}".format(IN_PATH)
    print "Out path: {0}".format(OUT_PATH)
    print "Lang keys: {0}".format(LANG_KEYS)
    print "------------------------------------\nSTART..."

    if PLATFORM == "ios":
      start_localize_ios(CURRENT_DIR, BASE_STRINGS_PATH, IN_PATH, OUT_PATH, LANG_KEYS)
    elif PLATFORM == "android":
      start_localize_android(CURRENT_DIR, BASE_STRINGS_PATH, IN_PATH, OUT_PATH, LANG_KEYS)
    elif PLATFORM == "json":
      start_localize_json(CURRENT_DIR, BASE_STRINGS_PATH, IN_PATH, OUT_PATH, LANG_KEYS)
    elif PLATFORM == "properties":
      start_localize_properties(CURRENT_DIR, BASE_STRINGS_PATH, IN_PATH, OUT_PATH, LANG_KEYS)
    else:
      print 'ERROR LOCALIZING.'
      print 'Unsupported format.'
      print '\n\n'
      pass
    
    print 'DONE LOCALIZING.'
    print '\n\n'

if __name__ == '__main__':
    main()
