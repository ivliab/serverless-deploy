#!/usr/bin/env python3
import sys
import subprocess

print(list(sys.argv))

stage = sys.argv[1]
region = sys.argv[2]
workdir = sys.argv[3]

if not stage or not region:
    print("You must supply a stage and a region to deploy to.")
    sys.exit(1)

print ("Deploying {}/{}".format(stage, region))

subprocess.run(
    ['npm', 'ci'],
    cwd=workdir,
)

subprocess.run(
    ['serverless', 'deploy', '--region {}'.format(region), '--stage {}'.format(stage)],
    cwd=workdir,
)
