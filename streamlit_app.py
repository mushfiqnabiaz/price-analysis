import streamlit as st
import pandas as pd
import numpy as np
st.title("Bangladesh Product Price Analysis")

#datafreame
st.write("This is Dataframe Demo")
df = pd.DataFrame(
    np.random.randn(50,20),
    columns=('col %d' % i for i in range (20))
)

st.dataframe(df)
