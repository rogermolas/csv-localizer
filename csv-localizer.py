import os
import sys
import argparse
 

def main ():

    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
   
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()


    if args.t == 'string':
        print "ios"
    elif args.t == "xml":
        print "android"
    elif args.t == "json":
        print "web"
    else:
        print "Invalid"

    # print args
        # action = sys.argv[1].lower()
        # platform_type = sys.argv[2].lower()
        # invalid_message =  "csv-localizer --help' list available subcommands and some concept guides."
        # input_directory = sys.argv[3]
        # # output_source = sys.argv[4]
        # if action == "--help":
        #     print "log help"

        # # check platform argumnent
        # if action== "--platform":
        #     if platform_type == "ios":
        #         print "iOS"
        #     elif platform_type == "android":
        #         print "android"
        #     else:
        #         print "\nPlatform should be iOS or Android\n"
        #         print invalid_message

        # # check input directory argumnent  
        # if len(input_directory) == 0:
        #     print "Success"
        # else:
        #     print "Invalid souce directory \n"
        #     print invalid_message
        # print("--platform [platform] [CSV path] [Output path]")
        
if __name__ == '__main__':
    main()
