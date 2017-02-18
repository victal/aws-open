# aws-open
A small script to easily open and close external SSH on AWS Security groups.

This is useful when you got an AWS account that you can't access via a VPN Connection and when you don't want to keep port 22 open for a large IP range (say, when your client machine has gets a dynamic IP from a large range from your ISP, for example).

With this script, you can simply open port 22 on the external-facing Security group in your account for connections from your IP, and then close it when you're done.

## Installation

AWS-open works with python >= 3. It's not on PyPI yet, so for now you will have to clone this repository and run 
```
# python3 setup.py install
```
in order to install it.

## Usage

```
awsesame [-h] {open,close,list-open,list-closed} ...

positional arguments:
  {open,close,list-open,list-closed}
    open                Add rules to open SSH to the local IP
    close               Removes rules allowing SSH access to the local IP
    list-open           Lists Security Groups that have SSH rules allowing
                        access from this IP
    list-closed         Lists Security Groups that do not have SSH rules
                        allowing access from this IP

optional arguments:
  -h, --help            show this help message and exit
```
## TODO:
Not complete by any means

- Upload project to PyPI
- Tests (however possible)
- Work with ports other than 22
- Deal with Security group rules spanning multiple ports
