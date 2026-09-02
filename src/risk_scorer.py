# src/risk_scorer.py
import pandas as pd
def score(row):
    risks=[]
    if row.get("Alternate1") in ["","-"]: risks.append("single-source")
    if row.get("LCSC")=="C347122": risks.append("NRND")
    if int(row.get("Qty",1))>10: risks.append("lead-time")
    return ";".join(risks) if risks else "low"
if __name__=="__main__":
    df=pd.read_csv("../data/bom_input.csv")
    df["risk"]=df.apply(score,axis=1)
    print(df["risk"].value_counts())
