import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np  


# Problem 01
df01 = pd.read_csv(r"D:\NewFolder\AAE718\data\SOCR-HeightWeight.csv")


def pr01(x):
    # Use matplotlib.pyplot
    plt.figure(figsize = (25,10))
    plt.scatter(x['Height(Inches)'], x['Weight(Pounds)'])
    plt.title("P01 Scatter Plot - matplotlib")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.savefig(r"pr01_mat.pdf")

    # Use Seaborn
    plt.figure(figsize = (25,10))
    sns.scatterplot(data = x, x = 'Height(Inches)', y = 'Weight(Pounds)')
    plt.title("P01 Scatter Plot - Seaborn")
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.savefig(r"pr01_seaborn.pdf")

if __name__ == "__main__":
    pr01(df01)

# Problem 02
def pr02(x):
    # matplotlib
    fig, axs = plt.subplots(1, 2, figsize = (24,10))
    axs[0].hist(x['Height(Inches)'],bins = 24, edgecolor = 'black')
    axs[0].set_xlabel('Height(Inches)',fontsize = 36)
    axs[0].set_ylabel('count',fontsize = 36)
    axs[1].hist(x['Weight(Pounds)'],bins = 24, edgecolor = 'black')
    axs[1].set_xlabel('Weight(Pounds)',fontsize = 36)
    axs[1].set_ylabel('count',fontsize = 36)
    plt.suptitle('Histogram - Matpotlib',fontsize = 36)
    plt.savefig(r"pr02_mat.pdf")

    # seaborn
    fig, axs = plt.subplots(1, 2, figsize = (24,10))
    sns.histplot(x['Height(Inches)'], ax = axs[0], bins = 24)
    axs[0].set_xlabel('Height(Inches)',fontsize = 36)
    axs[0].set_ylabel('count',fontsize = 36)
    sns.histplot(x['Weight(Pounds)'], ax = axs[1], bins = 24)
    axs[1].set_xlabel('Weight(Pounds)',fontsize = 36)
    axs[1].set_ylabel('count',fontsize = 36)
    fig.suptitle('Histogram - Seaborn',fontsize = 36)
    plt.savefig(r"pr02_seaborn.pdf")

if __name__ == "__main__":
    pr02(df01)

std_height = df01['Height(Inches)'].std()
std_weight = df01['Weight(Pounds)'].std()

# Problem 03
def pr03(x):
    # seaborn
    sns.lmplot(x='Height(Inches)', y='Weight(Pounds)', data=x, line_kws={'color': 'blue'}, scatter_kws={'color':'black', 'alpha': 0.5}, height=20, aspect=3, ci=95)
    plt.title('P03-Seaborn', fontsize=64)
    plt.xlabel('Height (Inches)', fontsize=64)
    plt.ylabel('Weight (Pounds)', fontsize=64)
    plt.savefig(r"pr03_seaborn.pdf", bbox_inches='tight')

    # matplotlib
    plt.figure(figsize=(24, 10))
    plt.scatter(x['Height(Inches)'], x['Weight(Pounds)'], color='black', alpha=0.5)
    beta = np.polyfit(x['Height(Inches)'], x['Weight(Pounds)'], 1)
    line = np.polyval(beta,x['Height(Inches)'])
    plt.plot(x['Height(Inches)'], line, color='blue', label='Regression Line')
    plt.title('P03-Matplotlib', fontsize=24)
    plt.xlabel('Height (Inches)', fontsize=24)
    plt.ylabel('Weight (Pounds)', fontsize=24)
    plt.savefig(r"pr03_mat.pdf", bbox_inches='tight')

if __name__ == "__main__":
    pr03(df01)

# Problem 04
df04 = pd.read_csv(r"D:\NewFolder\AAE718\data\company_sales_data.csv")

def pr04(x):
    # how has the total profit changed over months?
    plt.figure(figsize=(12, 10))
    plt.plot(x['month_number'], x['total_profit'], marker='o', linestyle='-')
    plt.title('Total Profit Over Months', fontsize=24)
    plt.xlabel('Month', fontsize=24)
    plt.ylabel('Total Profit', fontsize=24)
    plt.grid(True)
    plt.savefig(r"pr04_1.pdf", bbox_inches='tight')
    plt.show()

    # how have sales of each product changed over time?
    products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap',
       'shampoo', 'moisturizer']
    for i in products:
        plt.plot(x['month_number'],x[i],marker='o', label=i)
    plt.title('Product Sales Over Time',fontsize=24)
    plt.xlabel('Month',fontsize=24)
    plt.ylabel('Sales',fontsize=24)
    plt.grid(True)
    plt.legend()
    plt.savefig(r"pr04_2.pdf", bbox_inches='tight')
    plt.show()

    # Is there a relationship between facecream and facewash?
    plt.figure(figsize=(12, 10))
    plt.scatter(x['facecream'],x['facewash'])
    plt.xlabel('facecream', fontsize = 24)
    plt.ylabel('facewash', fontsize = 24)
    plt.title('Relationship between Facecream & Facewash',fontsize=24)
    plt.savefig(r"pr04_3.pdf", bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    pr04(df04)

# Problem 05
df05 = pd.read_csv(r"D:\NewFolder\AAE718\data\crop_production.csv")
def pr05(x):
    # The wheat production data among each location
    wheat_data = x[x['SUBJECT'] == 'WHEAT']
    plt.figure(figsize=(12, 10))
    sns.barplot(x='Value', y='LOCATION', data=wheat_data)
    plt.xlabel('Value', fontsize = 24)
    plt.ylabel('Location', fontsize = 24)
    plt.title('Wheat Production Data among Location',fontsize=24)
    plt.savefig(r"pr05_1.pdf", bbox_inches='tight')
    plt.show()

    # The wheat production data changed over time in USA
    wheat_usa_data = wheat_data[wheat_data['LOCATION'] == 'USA']
    plt.figure(figsize = (12, 10))
    sns.lineplot(x='TIME', y = 'Value', data = wheat_usa_data, ci = None)
    plt.xlabel('Year', fontsize = 24)
    plt.ylabel('Production', fontsize = 24)
    plt.title('Wheat Production Data Changed Over Time in USA',fontsize=24)
    plt.savefig(r"pr05_2.pdf", bbox_inches='tight')
    plt.show()

    # The crop production data changed over time in USA
    usa_data =  x[x['LOCATION'] == 'USA']
    sns.lineplot(x='TIME', y = 'Value', hue = 'SUBJECT', data = usa_data, ci = None)
    plt.xlabel('Year', fontsize = 24)
    plt.ylabel('Production', fontsize = 24)
    plt.title('Crop Production Data Changed Over Time in USA',fontsize=24)
    plt.savefig(r"pr05_3.pdf", bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    pr05(df05)

# Problem 06
# See in PDF file.