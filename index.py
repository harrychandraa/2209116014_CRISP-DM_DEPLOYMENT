import streamlit as st
import pandas as Pd
import numpy as np
import matplotlib.pie as plt
import seaborn  as  sns
import plotly.express as px

st.write("""
# praktikum PDBA A1 - 22         
""")

st.title('ini adalah judul')

st.header('ini adalah tajuk Utama')

st.subheader('Tajuk 1')

st.caption('ini captionnya')

kode_python = """"
def fungsi (parameter):
print ('ini adalah kode python')
"""

st.code(kode_python, languege ='python')

st.text('ini text')

st.latex('')

df = pd.DataFrame({
    'nim':['220191999','2242424424'],
    'nama' : ['harry','harry']
})

st.dataframe(data=df, width=500 , height=50)

st,table(data=df)

st.metric(label='suhu',value='100 F',
          Delta='-1.2 F')

x = np.random.normal(13,3,200)

fig,ax = plt.subplots()
ax.histplot(x=x)
st.pyplot(fig)