#!/usr/bin/env python
#
#    Copyright (c) 2009-2015 Tom Keffer <tkeffer@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#
"""Entry point to the weewx weather system."""
import sys
from optparse import OptionParser

# First import any user extensions:
import user.extensions       #@UnusedImport
# Now the engine
import weewx.engine

usagestr = """
  %prog config_path [--daemon] [--pidfile=PIDFILE] [--exit] [--loop-on-init]
                     [--version] [--help]

  Entry point to the weewx weather program. Can be run directly, or as a daemon
  by specifying the '--daemon' option.

Arguments:
    config_path: Path to the weewx configuration file to be used.
"""

#===============================================================================
#                       function parseArgs()
#===============================================================================

def parseArgs():
    """Parse any command line options."""

    parser = OptionParser(usage=usagestr)
    parser.add_option("-d", "--daemon",  action="store_true", dest="daemon",  help="Run as a daemon")
    parser.add_option("-p", "--pidfile", type="string",       dest="pidfile", help="Path to process ID file", default="/var/run/weewx.pid")     
    parser.add_option("-v", "--version", action="store_true", dest="version", help="Display version number then exit")
    parser.add_option("-x", "--exit",    action="store_true", dest="exit"   , help="Exit on I/O and database errors instead of restarting")
    parser.add_option("-r", "--loop-on-init", action="store_true", dest="loop_on_init"  , help="Loop if device is not ready on startup")
    (options, args) = parser.parse_args()
    
    if options.version:
        print weewx.__version__
        sys.exit()
        
    if len(args) < 1:
        sys.stderr.write("Missing argument(s).\n")
        sys.stderr.write(parser.parse_args(["--help"]))
        sys.exit(weewx.CMD_ERROR)
    
    return options, args

#===============================================================================
#                       Main entry point
#===============================================================================

# Get the command line options and arguments:
(options, args) = parseArgs()

# Fire up the engine.
weewx.engine.main(options, args)
