import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt  
import seaborn as sns
import random  

@st.cache_data  
def load_data():
    df = pd.read_csv('BlackFriday.csv', nrows=1000) 
    return df


try:
    df = load_data() 
except FileNotFoundError:
    st.error("Error: File not found.")
except pd.errors.ParserError:
    st.error("Error: Invalid data format.")
else:
    # Gender pourcentage
    st.markdown("<h4> 1. we will start our Black Friday analyse with customer gender Informations </h4>", unsafe_allow_html=True)
    st.markdown("<ul><li> Customer Gender pourcentage</li></ul>", unsafe_allow_html=True)
    explode = (0.1, 0)  
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.pie(
        df['Gender'].value_counts(),
        labels = ['Male','Female'],
        explode=explode,
        shadow=True,
        startangle=90,
        autopct='%1.1f%%'
    )
    ax.axis('equal')  
    plt.tight_layout()  
    plt.legend()  
    st.pyplot(fig)

    # Gender vs Purchase
    st.markdown("<ul><li> Analyzing Purchase Amount by Gender</li></ul>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(9, 4))
    df.groupby('Gender')['Purchase'].sum().sort_values().plot(kind='bar', ax=ax, color=['skyblue', 'coral'])
    plt.xticks(range(len(df['Gender'].unique())), ['Female', 'Man'])
    plt.title('Bar chart for Purchase by Gender Type ')
    st.pyplot(fig)
    st.markdown("<p style='text-align: center;'> Men's purchasing power is greater than women's purchasing power, even in normal circumstances. This is likely to affect the owner of the money, but there has been a high turnout of men in the store. About 75% of the customers have made sales of men of all ages, we have probably made sales worth more than 6 billion in men and more than 2.6 billion in ladies </p>", unsafe_allow_html=True)


    # Marital Status pourcentage
    st.markdown("<h4> 2. we will continue our Black Friday analyse with customer Marital Status Informations</h4>", unsafe_allow_html=True)
    st.markdown("<ul><li> Customer Marital Status pourcentage</li></ul>", unsafe_allow_html=True)
    explode = (0.1, 0)  
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.pie(
        df['Marital_Status'].value_counts(),
        labels = ['Yes','No'],
        explode=explode,
        shadow=True,
        startangle=90,
        autopct='%1.1f%%'
    )
    ax.axis('equal')  
    plt.tight_layout()  
    plt.legend()  
    st.pyplot(fig)

    # Marital Status vs Purchase
    st.markdown("<ul><li> Analyzing Purchase Amount by Marital status </li></ul>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(9, 4))

    df.groupby('Marital_Status')['Purchase'].sum().sort_values().plot(kind='bar', ax=ax, color=['skyblue', 'coral'])
    plt.xticks(range(len(df['Gender'].unique())), ['Yes', 'No'])
    plt.title('Bar chart for Purchase by Marital Status Type ')
    st.pyplot(fig) 

    # customer Age 
    st.markdown("<h4> 3. we will continue our Black Friday analyse with customer Age Informations</h4>", unsafe_allow_html=True)
    st.markdown("<ul><li> Analyzing Purchase Amount by Customer Age </li></ul>", unsafe_allow_html=True)
    df.groupby('Age')['Purchase'].sum().sort_values().plot(
        kind='bar',
        color=[random.choice(['skyblue', 'coral', 'lightgreen', 'gold', 'violet']) for _ in range(len(df['Age'].unique()))],
        figsize=(9, 4) 
    )
    plt.title('Bar chart for Purchase by Age')
    st.pyplot(plt) 

    # customer Age vs gender
    st.markdown("<ul><li> Analyzing Gender by Customer Age </li></ul>", unsafe_allow_html=True)
    plt.figure(figsize=(12, 7))  
    sns.countplot(x='Age', hue='Gender', data=df)
    plt.title('Countplot of Age by Gender')
    st.pyplot(plt) 

    st.markdown("<ul><li> The 0-17 age group has the highest number of purchases, followed by the 55+ age group :  </li><p>This could be explained by younger people being more prone to impulse purchases, while older people might have more purchasing power.</p> </ul>", unsafe_allow_html=True)
    st.markdown("<ul><li> The 18-25 and 36-45 age groups have the lowest number of purchases :  </li><p>This could be because these age groups are more likely to invest in durable goods rather than impulse purchases.</p> </ul>", unsafe_allow_html=True)


    # customer city 
    st.markdown("<h4> 4. we will continue our Black Friday analyse with customer City Informations</h4>", unsafe_allow_html=True)
    st.markdown("<ul><li> Analyzing Customer city pourcentage </li></ul>", unsafe_allow_html=True)
    explode = (0.1, 0, 0)  
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.pie(
        df['City_Category'].value_counts(),
        labels=df['City_Category'].unique(),
        explode=explode,
        shadow=True,
        startangle=90,
        autopct='%1.1f%%'
    )
    ax.axis('equal')  
    plt.tight_layout()  
    plt.legend()  
    st.pyplot(fig)


    st.markdown("<ul><li> Distribution of Customer Age Groups across City Categories </li></ul>", unsafe_allow_html=True)
    fig2, ax2 = plt.subplots(figsize=(12, 7))
    city_age_purchase = df.groupby(['City_Category', 'Age'])['Purchase'].sum().reset_index()
    sns.barplot(x='City_Category', y='Purchase', hue='Age', data=city_age_purchase, ax=ax2)
    plt.title('Purchase Amount by City Category and Age')
    plt.xticks(rotation=45)
    st.pyplot(plt)
    st.markdown("<p style='text-align: center;'>The chart shows that City Category B is the most lucrative market with the highest purchase amounts across all age groups. The 26-35 age group is the most active across all cities, while the 55+ group shows the lowest purchasing power. City Category A has lower purchasing power overall, but the 18-25 age group spends more there. City Category C sees the 36-45 age group as a significant contributor to purchases.  </p>", unsafe_allow_html=True)


    # Total Purchase Amount by Years Spent in Current City
    st.markdown("<h4> 4. we will continue our Black Friday analyse with customer stability Informations</h4>", unsafe_allow_html=True)
    st.markdown("<ul><li> Analyzing Total Purchase Amount by Years Spent in Current City </li></ul>", unsafe_allow_html=True)
    # Pie Chart
    labels = ['First Year', 'Second Year', 'Third Year', 'More Than Four Years', 'Guest']
    explode = (0.1, 0.1, 0, 0, 0)
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.pie(
        df.groupby('Stay_In_Current_City_Years')['Purchase'].sum(),
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90
    )
    ax.axis('equal')
    plt.tight_layout()
    plt.legend()
    plt.title("Total Purchase Amount by Years Spent in Current City")
    st.pyplot(fig)
    st.markdown("<p style='text-align: center;'>The pie chart shows that customers who have lived in their current city for their second year contribute the most to total purchase amount (30.2%). New residents (first year) contribute the least (10.1%), while temporary visitors and long-term residents contribute significantly as well.  </p>", unsafe_allow_html=True)



    # Product_Category_1
    st.markdown("<h4> 5. In this section we will see Purchase amount for each product category and the relation between Product Category and Age and between Gender and also product cartegory for each City </h4>", unsafe_allow_html=True)
    st.markdown("<ul><li> Product Category 1 </li></ul>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 7.45))
    df.groupby('Product_Category_1')['Purchase'].sum().sort_values().plot(kind='bar', ax=ax, color=['skyblue', 'green'])
    plt.title('Product category 1 by Purchase')
    plt.tight_layout()
    plt.legend()

    fig1, ax1 = plt.subplots(figsize=(12, 7))
    sns.countplot(x='Product_Category_1', hue='Age', data=df, ax=ax1)
    plt.title('Product Category 1 vs Age')

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig)
    with col2:
        st.pyplot(fig1)

    fig1, ax1 = plt.subplots(figsize=(12, 7))
    sns.countplot(x='Product_Category_1', hue='Gender', data=df, ax=ax1)
    plt.title('Product Category 1 vs Gender')
    st.pyplot(fig1)
    st.markdown("<p style='text-align: center;'>The charts indicate a strong correlation between product category and purchase amount, implying a tiered pricing or value proposition model for products. Younger age groups, particularly the 26-35 age group, dominate most product categories, suggesting a large customer base in this demographic. While gender distribution varies across different categories, male customers appear to be the dominant buyers overall. Understanding these relationships can help businesses tailor their marketing strategies and product offerings to target specific customer segments effectively</p>", unsafe_allow_html=True)


    # Product category 2
    st.markdown("<ul><li> Product Category 2 </li></ul>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 7.45))
    df.groupby('Product_Category_2')['Purchase'].sum().sort_values().plot(kind='bar', ax=ax, color=['skyblue', 'green'])
    plt.title('Product category 2 by Purchase')
    plt.tight_layout()
    plt.legend()

    fig1, ax1 = plt.subplots(figsize=(12, 7))
    sns.countplot(x='Product_Category_2', hue='Age', data=df, ax=ax1)
    plt.title('Product Category 2 vs Age')

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig)
    with col2:
        st.pyplot(fig1)

    fig1, ax1 = plt.subplots(figsize=(12, 7))
    sns.countplot(x='Product_Category_2', hue='Gender', data=df, ax=ax1)
    plt.title('Product Category 2 vs Gender')
    st.pyplot(fig1)
    st.markdown("<p style='text-align: center;'>The charts reveal a clear correlation between product category and purchase amount, suggesting a pricing or value hierarchy for the products. Age distribution across product categories varies, indicating that different categories might target specific age groups. While gender distribution shows a slight bias towards male customers in some categories, the overall distribution seems more balanced than observed for Product Category 1. This analysis provides insights into the customer profiles and purchase patterns associated with different product categories, helping businesses optimize their marketing and product development strategies.</p>", unsafe_allow_html=True)


    # Product category 3
    st.markdown("<ul><li> Product Category 2 </li></ul>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 7.45))
    df.groupby('Product_Category_3')['Purchase'].sum().sort_values().plot(kind='bar', ax=ax, color=['skyblue', 'green'])
    plt.title('Product category 3 by Purchase')
    plt.tight_layout()
    plt.legend()

    fig1, ax1 = plt.subplots(figsize=(12, 7))
    sns.countplot(x='Product_Category_3', hue='Age', data=df, ax=ax1)
    plt.title('Product Category 3 vs Age')

    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig)
    with col2:
        st.pyplot(fig1)

    fig1, ax1 = plt.subplots(figsize=(12, 7))
    sns.countplot(x='Product_Category_3', hue='Gender', data=df, ax=ax1)
    plt.title('Product Category 3 vs Gender')
    st.pyplot(fig1)
    st.markdown("<p style='text-align: center;'>The charts reveal a clear correlation between product category and purchase amount, suggesting a pricing or value hierarchy for the products. Age distribution across product categories varies, indicating that different categories might target specific age groups. While gender distribution shows a slight bias towards male customers in some categories, the overall distribution seems more balanced compared to the previous analysis of Product Category 1 and 2. This analysis provides insights into the customer profiles and purchase patterns associated with different product categories, helping businesses optimize their marketing and product development strategies.</p>", unsafe_allow_html=True)

    

