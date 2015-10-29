#Part a)

#creating a list of cities from looping through lines of file
city_list=[]
for line in open('bitly.tsv').readlines()[1:]:
    els = line.split('\t')
    city_list.append(els[3])

#sorting list by passing the lower function to all city names and
#converting list into a set since sets are unique and will eliminate duplicates
sorted_city_set = set(sorted(city_list, key=str.lower))

#prints the number of unique cities in case it's not practical to print whole list on screen
print 'Number of unique cities in this file: {0}'.format(len(sorted_city_set))


#Part b)

#create dict for unique countries and their respective count of occurences in file by looping through and adding 1 each time it appears
country={}
for line in open('bitly.tsv').readlines()[1:]:
    els = line.split('\t')
    if els[4] in country:
        country[els[4]] += 1
    else:
        country[els[4]] = 1

#sorts dictionary by value (from largest to smallest number of occurences), then prints out the top ten
top_country= list(sorted(country, key=country.get, reverse=True))
if '' in top_country:
    top_country.remove('')
top_country=top_country[:10]
print 'The top ten countries in the file are: {0}'.format(top_country)

#Part c)

#creates a list of all the long urls in file
long_url=[]
for line in open('bitly.tsv').readlines()[1:]:
    els = line.split('\t')
    long_url.append(els[2])

#splitting out the machine by using '/' as a delimiter in the long url
machines=[]
for slice in long_url:
    machines.append(slice.split('/')[2])

#creating a dict to loop through in order to tally up how many times the machines occur in the file
tally_machines={}
for machine in machines:
    if machine in tally_machines:
        tally_machines[machine] += 1
    else:
        tally_machines[machine] = 1

#sorting dict by value, then converting it into a list in order to return the top ten
top_machines= list(sorted(tally_machines, key=tally_machines.get, reverse=True))[:10]
print 'The top ten machines in the file are: {0}'.format(top_machines)

print_city = raw_input('Would you like a list of unique cities in this file? (y or n): ')
if print_city == 'y':
    print sorted_city_set
