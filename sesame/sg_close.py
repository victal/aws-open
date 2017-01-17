#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import get_external_ip, get_sg_id_from_name, get_all_sgs
import boto3

def sg_close(sg_name=None, all_sgs=False):
      if all_sgs:
            sgs = get_all_sgs()
      else:
            ec2 = boto3.resource('ec2')
            sg_id = get_sg_id_from_name(sg_name)
            sgs = [ec2.SecurityGroup(sg_id)]
      
      current_ip = get_external_ip()
      current_cidr = current_ip + "/32"
      for security_group in sgs:
            print('Closing SSH to this IP on Security Group %s' % security_group.group_name)
            security_group.revoke_ingress(
                        IpProtocol='tcp',
                        FromPort=22,
                        ToPort=22,
                        CidrIp=current_cidr
                        )
