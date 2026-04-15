from statsmodels.stats.multitest import multipletests

def correct(results):
    p=[r["p"] for r in results]
    reject,adj,_,_=multipletests(p,method="fdr_bh")
    for i,r in enumerate(results):
        r["p_adj"]=adj[i]
        r["sig"]=bool(reject[i])
    return results
