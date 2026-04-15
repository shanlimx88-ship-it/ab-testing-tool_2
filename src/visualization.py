import matplotlib.pyplot as plt

def plot(results):
    names=[r["metric"] for r in results]
    lifts=[r["lift"]*100 for r in results]
    plt.figure()
    plt.bar(names,lifts)
    plt.xticks(rotation=30)
    plt.ylabel("Lift %")
    plt.tight_layout()
    plt.savefig("output/figures/lift.png")
