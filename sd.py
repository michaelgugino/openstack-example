import argparse
import stevedore

exts = stevedore.ExtensionManager(namespace='greeting_apps')

funs = exts.names()

parser = argparse.ArgumentParser()

parser.add_argument('command', metavar='C')
args = parser.parse_args()
try:
    exts[args.command].plugin()
except:
    print("Command %s not found, valid commands are: %s" % (args.command, funs))
