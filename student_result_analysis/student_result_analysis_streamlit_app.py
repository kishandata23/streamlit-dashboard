import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st

# reading data
data = './dataset.csv'
df = pd.read_csv(data)

# drop column Unnamed: 0 
df=df.drop('Unnamed: 0',axis=1)

# Display figures in Streamlit
st.title("Analysis")



 
# Create figures
fig1, ax1 = plt.subplots()
gender_dist = sns.countplot(df, x='Gender', ax=ax1)
gender_dist.bar_label(gender_dist.containers[0])
ax1.set_title('Gender Distribution')
 
st.pyplot(fig1)


fig2, ax2 = plt.subplots()
group_by_ParentEduc = df.groupby('ParentEduc').agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
group_by_ParentEduc = sns.heatmap(group_by_ParentEduc,annot=True)
ax2.set_title("Parent Education effect on Student's Subject score")
st.pyplot(fig2)



fig3, ax3 = plt.subplots()
group_by_ParentMaritalStatus = df.groupby('ParentMaritalStatus').agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
ParentMaritalStatus = sns.heatmap(group_by_ParentMaritalStatus,annot=True)
ax3.set_title("ParentMaritalStatus effect on Student's Subject score")
st.pyplot(fig3)



# # Use columns to display graphs in a row
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.pyplot(fig1)

# with col2:
#     st.pyplot(fig2)

# with col3:
#     st.pyplot(fig3)