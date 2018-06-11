#!/usr/bin/env python3
import sys
import yaml

import byml

if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help']:
    sys.stderr.write("Usage: byml_to_yml.py <BYML>")
    sys.exit(1)

class Dumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(Dumper, self).increase_indent(flow, False)

if sys.argv[1] == '-':
    f = sys.stdin.buffer
else:
    f = open(sys.argv[1], "rb")

with f as file:
    data = file.read()
    root = byml.Byml(data).parse()
    yaml.dump(root, sys.stdout, Dumper=Dumper, allow_unicode=True)
