import pandas as pd
import matplotlib.pyplot as plt

def generate_overall_plot():
    data = pd.read_csv('overall_rankings')
    df = pd.DataFrame(data)
    
    x = list(df.iloc[:, 0])
    y = list(df.iloc[:, 1])
    
    # Plot the data using bar() method
    plt.bar(x, y, color='b')
    plt.title("Overall ranking of all modules")
    plt.xlabel("Rank")
    plt.ylabel("Number of modules")

    # Rotate x labels
    plt.xticks(rotation=45)

    for index,data in enumerate(y):
        plt.text(x=index-0.4, y=data+10, s=f"{data}", fontdict=dict(fontsize=10))
    
    # Save the plot
    plt.tight_layout()
    plt.savefig("overall_ranking.png")

def generate_platform_plot():
    data = pd.read_csv('overall_exploits')
    df = pd.DataFrame(data)
    
    x = list(df.iloc[:, 0])
    y = list(df.iloc[:, 1])
    
    # Plot the data using bar() method
    plt.bar(x, y, color='b')
    plt.title("Overall number of modules for different platforms")
    plt.xlabel("Platform")
    plt.ylabel("Number of modules")

    # Rotate x labels
    plt.xticks(rotation=45)

    for index,data in enumerate(y):
        plt.text(x=index-0.5, y=data+2, s=f"{data}", fontdict=dict(fontsize=10))
    
    # Save the plot
    plt.tight_layout()
    plt.savefig("overall_platforms.png")

if __name__ == '__main__':
    generate_overall_plot()
    plt.clf()
    generate_platform_plot()