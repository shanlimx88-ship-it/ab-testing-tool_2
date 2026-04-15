import pandas as pd, numpy as np, os
np.random.seed(42)

def generate_sample_data(n_users=5000, effect_size=0.02, output_path="data/sample.csv"):
    users = [f"user_{i}" for i in range(n_users)]
    variants = np.random.choice(['control','treatment'], size=n_users)
    data=[]
    for u,v in zip(users,variants):
        base=0.5
        lift=base+effect_size if v=='treatment' else base
        data.append({
            "user_id":u,
            "variant":v,
            "retention_7d":np.random.binomial(1,lift),
            "activation":np.random.binomial(1,0.35 if v=='control' else 0.38),
            "sessions":np.random.poisson(5 if v=='control' else 5.2),
            "error_rate":np.random.beta(1,20 if v=='control' else 22),
            "latency_ms":int(np.random.gamma(2,500 if v=='control' else 480))
        })
    df=pd.DataFrame(data)
    os.makedirs(os.path.dirname(output_path),exist_ok=True)
    df.to_csv(output_path,index=False)
    print("saved:",output_path)

if __name__=="__main__":
    generate_sample_data()
