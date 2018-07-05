import sys, argparse, logging, os, csv
from android_localizer import start_localize_android

# Gather our code in a main() function
def main(args, loglevel):
  # logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
  logging.basicConfig(format="%(message)s", level=loglevel)
  PLATFORM = args.platform
  IN_PATH = args.input
  OUT_PATH = args.output
  LANG_KEYS = None  #static will change later
  print '\n'
  logging.info("Start Localizing .... ")
  print '\n'
  logging.info("------------------------------------")
  
  # check source path
  logging.debug("\n")
  logging.debug("Validating source path ...")
  logging.debug("\n")
  if not os.path.exists(IN_PATH):
    logging.error('Source path not found, Invalid path.')
    logging.debug("\n")
    return
  
  logging.debug("Valid source path, finding csv file ...")
  logging.debug("\n")
  logging.debug("Validating target path ...")
  logging.debug("\n")
  # check output path
  if not os.path.exists(OUT_PATH):
    logging.error('Target path not found, Invalid path.')
    logging.debug("\n")
    return
  logging.debug("Valid target path, generating output directory ...")
  logging.debug("\n")
  
  # generate output directory
  OUTPUT_DIR = os.path.join(OUT_PATH, "output")
  if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
    logging.debug("Output directory generated : %s" % OUTPUT_DIR)
    logging.debug("\n")
  else:
    logging.debug("Using output directory: %s" % OUTPUT_DIR)
    logging.debug("\n")

  if PLATFORM == "ios":
    logging.debug("Platform : %s" % PLATFORM)
    logging.debug("\n")
    logging.info("Generation output : %s" % OUTPUT_DIR)
    start_localize_ios(IN_PATH, OUTPUT_DIR)
  else:
    logging.warn("Invalid platform, platform should be ios or android only")
    logging.debug("\n")
    logging.error('ERROR LOCALIZING.')
  print '\n'
  logging.info("DONE LOCALIZING.")
  print '\n'

def start_localize_ios(SOURCE_PATH, OUTPUT_PATH):
  base_out_dir = OUTPUT_PATH
  # each languages
  # for lang in LANG_KEYS:
  #   lang_path = os.path.join(base_out_dir, "{0}.lproj/".format(lang))
  #   if not os.path.exists(lang_path):
  #     os.makedirs(lang_path)

  # full_out_paths = [os.path.join(base_out_dir, "{0}.lproj/".format(langKey) + "Localizable.strings") for langKey in LANG_KEYS]
  # allwrites = [open(out_path, 'w') for out_path in full_out_paths]

  full_out_paths = None
  allwrites = None

  for dirname, dirnames, filenames in os.walk(SOURCE_PATH):
    for f in filenames:
      filename, ext = os.path.splitext(f)
      if ext != '.csv':
        continue

      fullpath = os.path.join(dirname, f)
      logging.info("Localizing: %s", filename)

      with open(fullpath, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        # create language key
        for i, line in enumerate(reader):
          if i == 0:
            line.remove(line[0])
            LANG_KEYS = line  # assign new value to key
            
            # iterate each language
            for lang in LANG_KEYS:
              lang_path = os.path.join(base_out_dir, "{0}.lproj/".format(lang))
              if not os.path.exists(lang_path):
                os.makedirs(lang_path)

          full_out_paths = [os.path.join(base_out_dir, "{0}.lproj/".format(langKey) + "Localizable.strings") for langKey in LANG_KEYS]
          allwrites = [open(out_path, 'w') for out_path in full_out_paths]

      with open(fullpath, 'rb') as csvfile:
        [fwrite.write('\n\n\n/*  {0}  */\n\n'.format(filename)) for fwrite in allwrites]
        
        reader = csv.reader(csvfile, delimiter=',')
        iterrows = iter(reader)
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
  

# Standard boilerplate to call the main() function to begin
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description = "Locatization commands")
  parser.add_argument("-p",help="Specify Platform (iOS, Android)" ,dest="platform", type=str, required=True)
  parser.add_argument("-i",help="Input source, CSV file path" ,dest="input", type=str, required=True)
  parser.add_argument("-o",help="Generated output path for localizable files" ,dest="output", type=str, required=True)

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