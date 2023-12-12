import re
import pandas as pd

fp = 'masadir/x1.json'
#urlP = r'https://(?:twitter\.com|x\.com)/[\w/=?&\.-]+' 
urlP = r'https://twitter\.com/[\w]+' 

try:
    with open(fp, 'r') as file:
        cnt = file.read()
        urls = re.findall(urlP, cnt)
        print("ناضي")
except IOError as e:
    print(f"هناك مشكلة: {e}")
    urls = []

urls_df = pd.DataFrame(set(urls), columns=['Motasahyen'])
csv = 'natija/x1.csv'

urls_df.to_csv(csv, index=False)