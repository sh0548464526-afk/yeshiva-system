
from datetime import datetime

def t(x):
    if not x: return None
    return datetime.strptime(x,"%H:%M")

def calc(x,start,amount,late):
    if not x: return 0
    x=t(x); s=t(start)
    if x<=s: return amount
    diff=int((x-s).total_seconds()/60)
    return max(0, amount - (diff//10)*late)

def calc_day(r,s):
    return sum([
        calc(r["s1"],s[0].start,s[0].amount,s[0].late),
        calc(r["s2"],s[1].start,s[1].amount,s[1].late),
        calc(r["s3"],s[2].start,s[2].amount,s[2].late)
    ])
