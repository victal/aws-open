#!/usr/bin/env python
# -*- coding: utf-8 -*-


from argparse import ArgumentParser
from sg_open import sg_open
from sg_close import sg_close

def create_parser():
      parser = ArgumentParser()
      subparsers = parser.add_subparsers(dest='command')
      p_open = subparsers.add_parser('open', help='Add rules to open SSH to the local IP')
      open_group = p_open.add_mutually_exclusive_group(required=True)
      open_group.add_argument('--name', dest='name', help='Name of a Securiy Group to which to add the SSH rule')
      open_group.add_argument('-a', '--all', action='store_true', help='If set, will add the SSH rule to all existing Security Groups')

      p_close = subparsers.add_parser('close', help='Removs rules allowing SSH access to the local IP')
      close_group = p_close.add_mutually_exclusive_group(required=True)
      close_group.add_argument('--name', dest='name', help='Name of a Securiy Group from which to remove the SSH rules')
      close_group.add_argument('-a', '--all', action='store_true', help='If set, will try to remove all SSH rules from a given SG, or all SSH rules specific to the local IP, otherwise')

      subparsers.add_parser('list-open', help='Lists Security Groups that have SSH rules allowing access from this IP')
      subparsers.add_parser('list-closed', help='Lists Security Groups that do not have SSH rules allowing access from this IP')

      return parser


def main():
      parser = create_parser()
      args = parser.parse_args()
      if args.command == 'close':
            sg_close(sg_name=args.name, all=args.all)
      elif args.command == 'open':
            sg_open(sg_name=args.name, all=args.all)
      else:
            parser.parse_args(['-h'])


if __name__ == "__main__":
      main()
