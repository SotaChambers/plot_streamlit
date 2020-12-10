import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import streamlit as st

dat = np.random.rand(20,4)
df = pd.DataFrame(dat, columns=['baseball','soccer','basketball','golf',])
df_1 = df.set_index('baseball')
df.index.name = 'Time'
df.head()

plt.style.use('seaborn-dark-palette')
font = {'family': 'meiryo'}
matplotlib.rc('font', **font)

fig = plt.figure(figsize=(12,9))
ax = plt.subplot()
plt.plot(df.index, df.soccer, label='soccer', marker='D', markersize=10, markerfacecolor='lightblue')
plt.scatter(df.index, df.basketball, color='red', label='basketball')
plt.xlabel('baseball',fontsize=18)
plt.tick_params(labelsize=18)
plt.tight_layout()
plt.legend()

fig = plt.figure(figsize=(12,5))

ax1 = plt.subplot(121)
plt.plot(df.index, df.baseball, label='baseball')
plt.scatter(df.index, df.golf, color='red', label='golf')
ax1.set_title('test')
ax1.set_xlim(0,22)
ax1.set_xlabel('time', fontsize=20)
ax1.set_ylabel('arb units', fontsize=24)
plt.tick_params(labelsize=18)

ax2 =plt.subplot(122)
plt.scatter(df.index, df.basketball, color='red')
ax2.set_title('test_2')
ax2.set_xlim(0,22)
ax2.set_xlabel('time', fontsize=20)
ax2.set_ylabel('basketball', fontsize=24)
plt.tick_params(labelsize=18)

plt.tight_layout()

fig, axes = plt.subplots(2, 3, figsize=(9, 6))
df.plot(ax=axes[0, 0],y='basketball')
df.plot(ax=axes[1, 2],x='golf',y='soccer', kind='scatter', legend=False)
plt.tight_layout()

st.title('グラフテスト')
st.line_chart(df.baseball）


