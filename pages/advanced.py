import numpy as np
import pandas as pd
import streamlit as st


# Kolonnas

col1, col2, col3 = st.columns(3)

with col1:
    st.header("beginning")
    st.image(r"img\people_1.jpg", width=200)

with col2:
    st.header("process")
    st.image(r"img\student_2.jpg", width=200)

with col3:
    st.header("result")
    st.image(r"img\mobile_3.jpg", width=300)




# st.title("Tabulu rindu atlase")
# df = pd.DataFrame(
#     np.random.randn(4, 3),
#     columns=('Column 1', 'Column 2', 'Column 3')
# )
# st.subheader('Original dataframe')
# st.write(df)
# df = df[df['Column 1'] > 0]
# st.subheader('Mutated dataframe')
# st.write(df)

# st.title("Tabulu kolonnu atlase")
# df = pd.DataFrame(
#     np.random.randn(4, 3),
#     columns=('Column 1', 'Column 2', 'Column 3')
# )
# st.subheader('Original dataframe')
# st.write(df)
# df = df[['Column 1', 'Column 2']]
# st.subheader('Mutated dataframe')
# st.write(df)

# st.title("Rindu kartības maiņa")
# df = pd.DataFrame(
#     np.random.randn(4, 3),
#     columns=('Column 1', 'Column 2', 'Column 3')
# )
# st.subheader('Original dataframe')
# st.write(df)
# df = df.sort_values(by='Column 1', ascending=True)
# st.subheader('Mutated dataframe')
# st.write(df)


# st.title("Grupēšana")
# df = pd.DataFrame(
#     np.random.randn(12, 3),
#     columns=('Score 1', 'Score 2', 'Score 3')
# )
# df['Name'] = pd.DataFrame(['John', 'Alex', 'Jessica', 'John', 'Alex',
#                            'John', 'Jessica', 'John', 'Alex', 'Alex', 'Jessica', 'Jessica'])
# df['Category'] = pd.DataFrame(['B', 'A', 'D', 'C', 'C', 'A',
#                                'B', 'C', 'B', 'A', 'A', 'D'])
# st.subheader('Original dataframe')
# st.write(df)
# df = df.groupby(['Name', 'Category']).first()
# st.subheader('Mutated dataframe')
# st.write(df)


# st.title("Tabulu apvienošana")

# df1 = pd.DataFrame(
#     np.random.randn(50, 20),
#     columns=('col %d' % i for i in range(20)))

# my_table = st.table(df1)

# df2 = pd.DataFrame(
#     np.random.randn(50, 20),
#     columns=('col %d' % i for i in range(20)))

# my_table.add_rows(df2)
