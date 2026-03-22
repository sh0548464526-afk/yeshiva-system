from openpyxl import Workbook

def export_excel(rows):
    wb=Workbook(); ws=wb.active
    ws.append(["תז","יום","ס1","ס2","ס3","סהכ"])

    for r in rows:
        ws.append([
            r["tz"],r["day"],r["s1"],r["s2"],r["s3"],r["total"]
        ])

    return wb