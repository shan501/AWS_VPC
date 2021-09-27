#! /usr/bin/env python3 
import boto3 
from boto3 import VPCConnection

#create a vpc and specify the cidrblock 
client=boto3.client('ec2')
vpc = client.create_vpc(CidrBlock='10.0.0.0/16')


#name the vpc 
vpc.create_tags(Tags=[{"Key":"Name","Value":"my_vpc"}])

#view the all the vpc we have created 
vpcs=client.describe_vpc()
no_of_vpcs=vpcs("Vpcs")
print(no_of_vpcs)


#creating a subnet and attaching it to our vpc
connection=VPCConnection()
subnet=connection.create_subnet(vpc.id,"10.0.0.0/24")


#create a vpn gateway and attach it to our vpc 
vpn=connection.create_vpn_gateway('gateway')
vpn.attach(vpc.id)

#getting vpn connections
vpns=connection.get_all_vpn_connections()






