#
# Ok, quick task for you agent - we've received a strange file from
# the first alien communication.
# It's at /tmp/alien-signal.txt, we need you to open and read the file.
#
#
with open("/tmp/alien-signal.txt") as file:
  for x in file:
    print(x)
