def generate(results):
    html="<h1>Experiment Report</h1><table border=1>"
    for r in results:
        html+=f"<tr><td>{r['metric']}</td><td>{r['lift']:.2%}</td><td>{r['p_adj']:.4f}</td></tr>"
    html+="</table>"
    open("output/reports/report.html","w").write(html)
