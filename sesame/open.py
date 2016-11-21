#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import get_external_ip, get_sg_id_from_name
import boto3

def open_sg(sg_id):
      ec2 = boto3.resource('ec2')
      current_ip = get_external_ip()
      current_cidr = current_ip + "/32"
      security_group = ec2.SecurityGroup(sg_id)
      security_group.authorize_ingress(
                  IpProtocol='tcp',
                  FromPort=22,
                  ToPort=22,
                  CidrIp=current_cidr
                  )


if __name__ == '__main__':
      import sys
      sg_name = sys.argv[1]
      sg_id = get_sg_id_from_name(sg_name)
      open_sg(sg_id)
