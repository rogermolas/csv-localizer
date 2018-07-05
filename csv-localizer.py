import sys, argparse, logging, os, csv
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

  # check input path
  if not os.path.exists(IN_PATH):
    logging.error('Source path not found, Invalid path.')
    return
  
  # check output path
  if not os.path.exists(OUT_PATH):
    logging.error('Target path not found, Invalid path.')
    return
  
  # generate output directory
  OUTPUT_DIR = os.path.join(OUT_PATH, "output")
  os.makedirs(OUTPUT_DIR)

  
  if BASE_STRINGS_PATH == "currentdir":
    BASE_STRINGS_PATH = CURRENT_DIR

  logging.info("------------------------------------\nSTART...")

  if PLATFORM == "ios":
    start_localize_ios(CURRENT_DIR, BASE_STRINGS_PATH, IN_PATH, OUTPUT_DIR, LANG_KEYS)
  elif PLATFORM == "android":
    start_localize_android(CURRENT_DIR, BASE_STRINGS_PATH, IN_PATH, OUT_PATH, LANG_KEYS)
  else:
    logging.error('ERROR LOCALIZING.')
    logging.error('Unsupported format \n\n')
    pass

    print 'DONE LOCALIZING.'
    print '\n'


def start_localize_ios(CURRENT_DIR, BASE_PATH, IN_PATH, OUT_PATH, LANG_KEYS):

  base_out_dir = OUT_PATH
  # top most
  if not os.path.exists(base_out_dir):
      os.makedirs(base_out_dir)

  # each languages
  for lang in LANG_KEYS:
    lang_path = os.path.join(base_out_dir, "{0}.lproj/".format(lang))
    if not os.path.exists(lang_path):
      os.makedirs(lang_path)

  full_out_paths = [os.path.join(base_out_dir, "{0}.lproj/".format(langKey) + "Localizable.strings") for langKey in LANG_KEYS]
  allwrites = [open(out_path, 'w') for out_path in full_out_paths]

  for dirname, dirnames, filenames in os.walk(os.path.join(CURRENT_DIR, IN_PATH)):
    for f in filenames:
      filename, ext = os.path.splitext(f)
      if ext != '.csv':
        continue

      fullpath = os.path.join(dirname, f)
      print 'Localizing: ' + filename + ' ...'

      with open(fullpath, 'rb') as csvfile:
        [fwrite.write('\n\n\n/*  {0}  */\n\n'.format(filename)) for fwrite in allwrites]

        reader = csv.reader(csvfile, delimiter=',')

        iterrows = iter(reader);
        next(iterrows) # skip first line (it is header).

        for row in iterrows:
          row_key = row[0].replace(" ", "")
          # comment
          if row_key[:2] == '//':
            continue

          row_values = [row[i+1] for i in range(len(LANG_KEYS))]

          # if any row is empty, skip it!
          if any([value == "" for value in row_values]):
            [fwrite.write('\n') for idx, fwrite in enumerate(allwrites)]
          else:
            [fwrite.write('"{key}" = "{lang}";\n'.format(key=row_key, lang=row_values[idx])) for idx, fwrite in enumerate(allwrites)]
  [fwrite.close() for fwrite in allwrites]
  
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
