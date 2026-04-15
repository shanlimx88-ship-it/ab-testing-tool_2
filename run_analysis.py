import pandas as pd, yaml, os
from src.experiment_analyzer import ExperimentAnalyzer
from src.multiple_comparison import correct
from src.visualization import plot
from src.report_generator import generate

cfg=yaml.safe_load(open("config.yaml"))
df=pd.read_csv("data/sample.csv")

metric_config={}
for m in cfg["analysis"]["metric_types"]["proportion_metrics"]:
    metric_config[m]="proportion"
for m in cfg["analysis"]["metric_types"]["continuous_metrics"]:
    metric_config[m]="continuous"

an=ExperimentAnalyzer(df)
results=[an.analyze(m,t) for m,t in metric_config.items() if m in df.columns]

results=correct(results)

for r in results:
    print(r)

os.makedirs("output/figures",exist_ok=True)
os.makedirs("output/reports",exist_ok=True)

plot(results)
generate(results)
