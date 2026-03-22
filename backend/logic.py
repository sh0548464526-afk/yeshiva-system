from datetime import datetime

def parse(t):
    if not t: return None
    return datetime.strptime(t,"%H:%M")

def calc(time,start,amount,late):
    t=parse(time); s=parse(start)
    if not t: return 0
    if t<=s: return amount
    m=int((t-s).total_seconds()/60)
    return max(0, amount - (m//10)*late)

def calc_day(row, sedarim):
    return sum([
        calc(row["s1"],sedarim[0].start,sedarim[0].amount,sedarim[0].late),
        calc(row["s2"],sedarim[1].start,sedarim[1].amount,sedarim[1].late),
        calc(row["s3"],sedarim[2].start,sedarim[2].amount,sedarim[2].late),
    ])