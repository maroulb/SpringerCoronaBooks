"""Some docstring here."""

import pandas as pd
import requests
import sys

helptext = '\nusage: python spricobo.py [list]\n\n[list] is a comma separated list (without whitespaces!)\nconsisting of abbreviations of disciplines to download:\n\nall : all books of all disciplines\nbsc : Behavioral Science\nbsp : Behavioral Science and Psychology\nbls : Biomedical and Life Sciences\nbne : Business and Economics\nbnm : Business and Management\ncms : Chemistry and Materials Science\ncsc : Computer Science\nees : Earth and Environmental Science\nenf : Economics and Finance\nedu : Education\neny : Energy\neng : Engineering\nhsl : Humanities, Social Sciences and Law\nitr : Intelligent Technologies and Robotics\nlnc : Law and Criminology\nlcm : Literature, Cultural and Media Studies\nmns : Mathematics and Statistics\nmed : Medicine\npna : Physics and Astronomy\nrnp : Religion and Philosophy\nssc : Social Sciences\n'


if len(sys.argv) != 2:
    print(helptext)
    sys.exit()

wishes = sys.argv[1]

wishlist = []

if 'all' in wishes:
    wishlist = ['Behavioral Science', 'Behavioral Science and Psychology', 'Biomedical and Life Sciences', 'Business and Economics', 'Business and Management', 'Chemistry and Materials Science', 'Computer Science', 'Earth and Environmental Science', 'Economics and Finance', 'Education', 'Energy', 'Engineering', 'Humanities, Social Sciences and Law', 'Intelligent Technologies and Robotics', 'Law and Criminology', 'Literature, Cultural and Media Studies', 'Mathematics and Statistics', 'Medicine', 'Physics and Astronomy', 'Religion and Philosophy', 'Social Sciences']

if 'bsc' in wishes:
    wishlist.append('Behavioral Sciences')
if 'bsp' in wishes:
    wishlist.append('Behavioral Science and Psychology')
if 'bls' in wishes:
    wishlist.append('Biomedical and Life Sciences')
if 'bne' in wishes:
    wishlist.append('Business and Economics')
if 'bnm' in wishes:
    wishlist.append('Business and Management')
if 'cms' in wishes:
    wishlist.append('Chemistry and Materials Sciences')
if 'csc' in wishes:
    wishlist.append('Computer Sciences')
if 'ees' in wishes:
    wishlist.append('Earth and Environmental Sciences')
if 'enf' in wishes:
    wishlist.append('Economics and Finance')
if 'edu' in wishes:
    wishlist.append('Education')
if 'eny' in wishes:
    wishlist.append('Energy')
if 'eng' in wishes:
    wishlist.append('Engineering')
if 'hsl' in wishes:
    wishlist.append('Humanities, Social Sciences and Law')
if 'itr' in wishes:
    wishlist.append('Intelligent Technologies and Robotics')
if 'lnc' in wishes:
    wishlist.append('Law and Criminology')
if 'lcm' in wishes:
    wishlist.append('Literature, Cultural and Media Studies')
if 'mns' in wishes:
    wishlist.append('Mathematics and Statistics')
if 'med' in wishes:
    wishlist.append('Medicine')
if 'pna' in wishes:
    wishlist.append('Physics and Astronomy')
if 'rnp' in wishes:
    wishlist.append('Religion and Philosophy')
if 'ssc' in wishes:
    wishlist.append('Social Sciences')


data = pd.read_excel('Free+English+textbooks.xlsx')

from tqdm import tqdm

for i in tqdm(data.itertuples()):
    if i[12] in wishlist:  # == "Computer Science":
        #  urls.append(i[19].encode('utf-8'))
        url = i[19].encode('utf-8')
        base, isbn = url.split('&')
        isbn_key, isbn = isbn.split('=')
        base_url = 'https://link.springer.com/content/pdf/10.1007%2F'
        dl_url = base_url + isbn + '.pdf'
        r = requests.get(dl_url, allow_redirects=True)
        if r.headers.get('content-type') == 'application/pdf':
            title = i[1].encode('utf-8')
            if '/' in title:
                title, waste = title.split('/')
            open(title + '.pdf', 'wb').write(r.content)
