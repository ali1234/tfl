import requests
from collections import defaultdict

s = defaultdict(dict)

def dump_severity():
    url = 'https://api.tfl.gov.uk/line/meta/severity'
    r = requests.get(url)
    j = r.json()
    for line in j:
        s[line['severityLevel']][line['modeName']] = line['description']

    for k, v in s.items():
        print(k)
        for kk, vv in v.items():
            if kk not in ['national-rail', 'road', 'cable-car']:
                print(vv, kk)

if __name__ == '__main__':
    dump_severity()