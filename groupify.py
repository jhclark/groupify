#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import sys
import random

WHO_FILE = "who.txt"

def usage():
  print("Usage: groupify <max_per_group>")
  print()
  print("First, place the members of your group who will be attending in who.txt")

def load_who():
  with open(WHO_FILE) as f:
    who = f.readlines()
    who = [ x.strip() for x in who ]
    return who

def groupify(who, num_groups):
  random.seed()
  random.shuffle(who)
  groups = [ [] for _ in range(num_groups) ]
  for i in range(len(who)):
    groups[i%num_groups].append(who[i])
  return groups

def main(*args):
  if len(args) != 1:
    usage()
    sys.exit(1)

  who = load_who()
  max_per_group = int(args[0])
  num_groups = 1
  while len(who) / num_groups > max_per_group:
    num_groups += 1
  groups = groupify(who, num_groups)
  for i in range(len(groups)):
    print("Group {}: {}".format(i+1, ", ".join(groups[i])))

if __name__ == "__main__":
  main(*sys.argv[1:])
