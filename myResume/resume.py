import streamlit as st

my_image="https://media.licdn.com/dms/image/v2/D4D03AQFUu3YvmhAqag/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1728707266204?e=1750896000&v=beta&t=p4UOY4tmDy2zybxhOq-q51Bb90eXofmElZWGjbSSojg"


st.sidebar.image(my_image,width=150)
st.sidebar.header('Contact')
st.sidebar.markdown(""" 
    +91 95504884754
    kishandata23@gmail.com

""")
st.sidebar.header("Skills")
skills_list=[]
st.sidebar.markdown(""" 
- Programming Language: Python, SQL  
- Framework & Libraries: NumPy, Pandas, Matplotlib, Beautiful Soup, Snowflake, Airflow 
- Visualization & Analysis tools: Basic of Power BI, Splunk and Excel 
- Cloud Deployment and Containers: AWS EC2, S3, IAM, Vercel, Git and GitHub

""")    

# st.sidebar._multiselect('Skills',['Python','SQL','Basic of Power BI'],default=['Python','SQL','Basic of Power BI'])

# st.header("Sutariya Kishankumar")
st.markdown("<h3 style='text-align: center;'>Sutariya Kishankumar</h3>", unsafe_allow_html=True)

st.subheader('Objective')
st.write('''
With 3+ years of hands-on experience in Python development, SQL, Airflow, and Splunk. A key contributor 
to the Core DataOps team, with a strong focus on building scalable data pipelines and monitoring systems. 
Actively seeking a long-term opportunity with a growth-oriented organization where I can take on added 
responsibilities and contribute to impactful projects. 
''')
 
st.subheader('WORK EXPERIENCE')
st.write('Mphasis Ltd (Dec 2021 – Present):  Software Engineer ')
st.markdown("""
- Developed and maintained scalable ETL pipelines using Airflow for seamless data migration. 
- Designed and implemented Python scripts for efficient data ingestion and validation, enhancing the 
performance of the Snowflake Data Warehouse. 
- Performed advanced data analytics and leveraged SQL to query and analyze data from Snowflake, Aqua 
Data Studio, and other databases. 
- Created a comprehensive Splunk dashboard to monitor server logs, leveraging KPIs and key insights to 
support production escalations and generate real-time alerts. 


""")


st.subheader('Projects')
# st.('')
st.markdown('''
- Project Name: ETL   
    - Technologies/Tools: Python, RDBMS (Postgres SQL, SQL Server), Pyspark. 
    - Description: Extracted data from various sources including web scraping, APIs, and CSV files; transformed 
and modeled the data using Python libraries, and loaded it into a SQL database for further analysis. 

- Project Name: Black Friday 
    - Technologies/Tools: Exploratory Data Analysis & Feature Engineering 
    - Description: Processed raw customer purchase data through cleaning and transformation, and built an ML 
model to analyze and predict customer behavior. 

- Project Name: Web Scrapping 
    - Technologies/Tools/Library: Python, Beautiful Soup 
    - Description: Scraped e-commerce websites like Amazon and Flipkart to extract product details and display 
the data in a structured tabular format.
''')




st.subheader('EDUCATION')
st.write('''VIGNAN UNIVERSITY | Bachelor of Technology in Electronics and Communication Engineering with 
CGPA: 8.64, Guntur, AP, 522213''')



