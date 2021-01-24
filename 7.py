import urllib.request

url = 'https://api.opap.gr/games/v1.0/1100/statistics?drawRange=1801'
url_contents = str(urllib.request.urlopen(url).read())
url_contents = url_contents.replace('{', '')
url_contents = url_contents.replace('}', '')
url_contents = url_contents.replace('[', '')
url_contents = url_contents.replace(']', '')
url_contents = url_contents.replace('"', '')

url_contents = url_contents.split(',')

occurrences = []

for item in url_contents:
    item = item.split(':') 

    if item[0] == "occurrences":
        occurrences.append(int(item[1]))
    
    if item[0] == "numbers":
        occurrences.append(int(item[-1]))

max_number = 0
max_thesi = 0
i = 1
for number in occurrences:
    if number > max_number:
        max_number = number
        max_thesi = i
    
    i += 1

print("The number that occurs the most times is " + str(max_thesi) + ", with " + str(max_number) + " times")