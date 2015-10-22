import os
import sys

args = sys.argv[1:]
number, info, by = args.split(',')

###For this problem, I need to build a dictionary of dictionaries where:
###{a: {b:c, b2:c2}, a2:{b3:c3, b4:c4}}  'a' is the outer key (the 'by' field in the args),
###'b' is the inner key which is the 'info' arg and 'c' is the number of occurences of 'b'.
###The final result would limit the 'b's shown depending on the 'number' arg the user requested (ie. the top 5)

###create a dictionary to refer to for which elements of the lines to read depending on what the user 
###wants to see. Every key is associated with an index of where that data is found in the bit.ly file

outerkeydict={'timestamp':0,'platform':1,'referring_url':2,'short_url_cname':3,'long_url':4,
    'geo_city_name':5, 'country_code':6, 'geo_region':7,'accept_language':8, 'timezone':9}

def validate(number, info, by):
    if not number.isdigit():
        sys.exit("First argument should be a number.")
    if info not in outerkeydict:
        sys.exit("Second argument should be from this list: {0}".format(outerkeydict.keys()))
    if by not in outerkeydict:
        sys.exit("Third argument should be from the following list: {0}".format(outerkeydict.keys()))

### A list of all possible platforms so we can loop through to see if any part of the long strings of 
### the 'user_agent' match with each of these. If so, this function will return the platform 
def get_platform(useragent):
    platforms = ['Android',
                 'BlackBerry',
                 'Windows NT',
                 'iPad',
                 'iPhone',
                 'iPod',
                 'Linux',
                 'Macintosh',
                 'PLAYSTATION 3']
    platform = False
    for x in platforms:
        if x.lower() in useragent.lower():  ###checks to see if the platform string is found in the 
                                        ###string of useragent. comparing lowercase versions of both
                platform = x
    if not platform:
        platform = 'Other' ###if no match is found amongst platform list, then platform will be other.  This function is only called if 'platform' is an arg, so this is OK.
    return platform
    
###starting to build outer dictionary
def get_data(number, info, by):
    outerkeydict={'timestamp':0,'platform':1,'referring_url':2,'short_url_cname':3,'long_url':4,
    'geo_city_name':5, 'country_code':6, 'geo_region':7,'accept_language':8, 'timezone':9}
    outer_dict={}
    for line in open('bitly_2.tsv').readlines()[1:]:
        els = line.split('\t')
        if info == 'platform':   ###checks to see if the second arg was platform, if so calls the get_platform function
            new = get_platform(els[outerkeydict[info]])
        else:     ###if not, then get the elements from the corresponding index by refering to the outerkeydict
            new = els[outerkeydict[info]]
        outer_list = []   #initializing a list to contain all the elements we're interested in from the file (the 'b's or the inner keys)
        outer_list.append(new)  #adding each element as we read through every line int he bit.ly file
        if by == 'platform':   #again, checking to see if the 3rd arg is platform and calling get_platform function again if it is
            outerkey = get_platform(els[outerkeydict[by]])
        else:
            outerkey = els[outerkeydict[by]]  ###otherwise, the outer keys of the dict is just the elements from the corresponding index (from the 'info' arg)
        if outerkey in outer_dict:
            outer_dict[outerkey].append(outer_list) ###as we go through every line in the file, we are checking if 
            ###outer key has been added to the dict yet.  If it has been already, then we append the new innerkey to the list of values (second arg).
        else:
            outer_dict[outerkey]=outer_list #if the outerkey does not exist yet, then we add it to the dict
    return outer_dict   ###the resulting dictionary looks like this {a:[[b],[b2],[b2],[b3],[b]], a2:[[b4],[b5],[b5]]...}
    
from collections import Iterable    
def flatten(a_list):  ###I needed a way to flatten the intermediate dictionary I just created because every value was its own list.  
    #So this func takes all the single-element lists and 'flattens' it into one list
     for item in a_list:
         if isinstance(item, Iterable) and not isinstance(item, basestring):
             for x in flatten(item):
                 yield x
         else:        
             yield item

    
###sorts all values of the innerdict and gets the top 'b' values for each outerkey in outerdict
def sort_innerval(a_dict):
    to_sort=a_dict.items() ###converts a nested dictionary into multiple tuples (a,b) where a is the outer key, and b is the inner dict whose values are number of occurences of the inner key.  Cannot sort dicts, so tuples are needed. 
    x= range(len(to_sort)) ###need to specify a range for how many tuples to loop through
    for i in x:
        sortedtups=zip(to_sort[i][1].keys(), sorted(to_sort[i][1].values(), reverse=True)) 
                   ###two things happening here: 
                   ###1)sorting the tuples within each outerkey so that the innerkey that occurs the most will be on top 
                   ###2)this sorting takes the values of the second element of the tuple and sorts on that, it creates two lists, one list of inner keys ('b'), 
                   ###and one of corresponding (sorted) # of occurences ('c').  I zip these two lists up to create sorted tuples.
        print "{0}: {1}".format(to_sort[i][0], sortedtups[:int(number)])  ###this prints out a dictionary of tuples, it's the correct info
            ###but not the exact format as the sample in the assignment.

def main():
    validate(number, info, by)
    outer_dict = get_data(number, info, by)
    valueset = {}             
    for key, value in outer_dict.items(): 
        for i in key:
            value = list(flatten(value)) ###flattens the dictionary of list of lists created previously
            valueset[key] = value  ###converting the dict with flattened list of 'b's (innerkeys) into a new dict
    combined_dict = {}
    for k, v in valueset.iteritems():
        combined_dict[k] = dict((i, v.count(i)) for i in v)  ###we finally take the dict of innerkeys and count the occurence of each ({a:{[b,b2,b2,b3]}--->{a:{b:1},{b2:2},{b3:1}} and set that as the value for the innerkeys.      
    sort_innerval(combined_dict)

main()
    
