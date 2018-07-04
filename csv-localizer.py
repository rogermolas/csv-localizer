import sys, argparse, logging, os

from ios_localizer import start_localize_ios
from android_localizer import start_localize_android

CURRENT_DIR = os.path.dirname(__file__)

# Gather our code in a main() function
def main(args, loglevel):
  logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
  if args.platform == 'ios':
    logging.debug("ios")
  elif args.platform == "android":
    logging.debug("android")
  else:
    logging.warn("Invalid platform, platform should be ios or android only")

  logging.debug("Your Argument: %s" % args.platform)
  logging.debug("Your Argument: %s" % args.input)
  logging.debug("Your Argument: %s" % args.output)
  
  logging.info("Start Localizing .... ")

  PLATFORM = args.platform
  IN_PATH = args.input
  OUT_PATH = args.output
  LANG_KEYS = ["en", "zh", "ja"] #static will change later
  BASE_STRINGS_PATH = "currentdir"
  
  if BASE_STRINGS_PATH == "currentdir":
    BASE_STRINGS_PATH = CURRENT_DIR

  logging.info("------------------------------------\nSTART...")

  if PLATFORM == "ios":
    start_localize_ios(CURRENT_DIR, BASE_STRINGS_PATH, IN_PATH, OUT_PATH, LANG_KEYS)
  elif PLATFORM == "android":
    start_localize_android(CURRENT_DIR, BASE_STRINGS_PATH, IN_PATH, OUT_PATH, LANG_KEYS)
  else:
    logging.error('ERROR LOCALIZING.')
    logging.error('Unsupported format \n\n')
    pass

    print 'DONE LOCALIZING.'
    print '\n'
  
  # Load Settings File
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = "Locatization commands")
  parser.add_argument("-p",help="Specify Platform (iOS, Android)" ,dest="platform", type=str, required=True)
  parser.add_argument("-i",help="Source path for CSV file" ,dest="input", type=str, required=True)
  parser.add_argument("-o",help="Output for localizable files" ,dest="output", type=str, required=True)

  parser.add_argument("-v",
                      "--verbose",
                      help="increase output verbosity",
                      action="store_true")
  args = parser.parse_args()
  
  # Setup logging
  if args.verbose:
    loglevel = logging.DEBUG
  else:
    loglevel = logging.INFO

  main(args, loglevel)
