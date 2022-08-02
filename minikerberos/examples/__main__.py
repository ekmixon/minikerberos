#!/usr/bin/env python3
#
# Author:
#  Tamas Jos (@skelsec)
#
import os
import logging
import ntpath

from minikerberos.ccache import CCACHE, Credential
from minikerberos.common import print_table
from minikerberos import logger

def main():
	import argparse

	parser = argparse.ArgumentParser(description='Prints CCACHE file info')
	parser.add_argument('ccachefile', help='input CCACHE file')
	parser.add_argument('-v', '--verbose', action='count', default=0)
	args = parser.parse_args()

	###### VERBOSITY
	if args.verbose == 0:
		logging.basicConfig(level=logging.INFO)
	else:
		logging.basicConfig(level=logging.DEBUG)


	logging.basicConfig(level=logging.INFO)
	logging.debug(f'Opening file {args.ccachefile}')
	cc = CCACHE.from_file(args.ccachefile)

	table = [['id'] + Credential.summary_header()]
	table.extend(
		[str(i)] + cred.summary() for i, cred in enumerate(cc.credentials)
	)

	print()	#this line intentionally left blank
	print_table(table)
	

if __name__ == '__main__':
	main()