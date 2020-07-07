import pandas as pd
import numpy as np

def main():
    # data = pd.DataFrame(np.random.rand(10, 4), columns=['A','B','C','D'])
    # data.head()
    # data.plot.bar();
    
    # df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})
    # ax = df.plot.bar(x='lab', y='val', rot=0)

    data = pd.DataFrame(np.random.rand(100, 1), columns=['value']).reset_index()
    data['value'].plot()
    data['value'].rolling(10).mean().plot()


if __name__ =="__main__":
    main()