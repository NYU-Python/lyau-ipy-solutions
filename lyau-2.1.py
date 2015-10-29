import os
import sys

sendmail_prog = '/usr/sbin/sendmail'
required_args = set(['to', 'from'])
valid_args = set(['to', 'from', 'subject', 'body'])

args = sys.argv[1:]

#setting up dict by looping through args and setting the keys and values
argdict = {}
for arg in args:
    field, value = arg.split('=')
    argdict[field] = value

#compare the new dictionary with the required and valid sets by using difference
missing_req=required_args.difference(set(argdict))
extra_val=set(argdict).difference(valid_args)

#using if statements to see if the difference sets are null or not, prints out the errors if the differences are not null
if missing_req:
    print 'Missing these fields: {0}'.format(list(missing_req))
if extra_val:
    print 'Invalid fields: {0}'.format(list(extra_val))

if (not missing_req) and (not extra_val):
#email header template
    template = """From: {0}
To: {1}
Subject: {2}"""

header = template.format(str(argdict['from']), str(argdict['to']),str(argdict['subject']))
print header
