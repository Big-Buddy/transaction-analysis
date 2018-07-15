from scipy.stats import binom
import seaborn as sb
import matplotlib.pyplot as plt

binom.rvs(n=59721,p=0.248)
data_binom = binom.rvs(n=59721,p=0.248,loc=0,size=1000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='green',
                  hist_kws={"linewidth": 15,'alpha':1})
plt.show()