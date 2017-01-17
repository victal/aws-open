#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
from ipaddress import IPv4Network, IPv4Address
from utils import get_external_ip

def list_open_sgs():
      ec2 = boto3.resource('ec2')
      current_ip = IPv4Address(get_external_ip())
      open_sgs = []
      for sg in ec2.security_groups.all():
            if is_open(sg, current_ip):
                  open_sgs.append(sg.group_name)

      print(open_sgs)

def list_closed_sgs():
      ec2 = boto3.resource('ec2')
      current_ip = IPv4Address(get_external_ip())
      closed_sgs = []
      for sg in ec2.security_groups.all():
            if not is_open(sg, current_ip):
                  closed_sgs.append(sg)

      print(closed_sgs)

def is_open(security_group, ip_address):
      for permission in security_group.ip_permissions:
            if permission.get('IpProtocol') == 'tcp' and \
               permission.get('FromPort') <= 22 and \
               permission.get('ToPort') >= 22:
                     for ip_range in permission.get('IpRanges'):
                           network = IPv4Network(ip_range.get('CidrIp'))
                           if ip_address in network:
                                 return True
      return False
