import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def main():
    diamonds = pd.read_csv('diamonds.csv', index_col=0)
    print(diamonds.head(7), end='\n\n')
    print(diamonds.tail(7), end='\n\n')
    print(diamonds.describe(), end='\n\n')

    print(diamonds['cut'].describe(), end='\n\n')
    print(diamonds['color'].describe(), end='\n\n')
    print(diamonds['clarity'].describe(), end='\n\n')

    print(diamonds['cut'].unique(), end='\n\n')
    print(diamonds['color'].unique(), end='\n\n')
    print(diamonds['clarity'].unique(), end='\n\n')

    diamonds.hist()
    plt.savefig('hists.png')
if __name__ == "__main__":
    main()