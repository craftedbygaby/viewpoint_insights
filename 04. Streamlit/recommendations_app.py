import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------
st.title('Brazil Travel Recommendation App')
st.write('''This App allows you to choose your travel preferences and get recommendations based on them''')

"""instructions on what the user should do to get the recommendations, and what kind of output they can expect (destination name, why this month is great for this place, brief description and highlights, international draw rating, weather and crowd level indicators)'''"""

st.divider()

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data #it will be saved inside the internal memory and won't run everytime we run the code
def load_data():

    df = pd.read_pickle(r"C:\Users\gabri\Documents\Data Analysis\Github\Viewpoint_Insights_final_project_IronHack\01. Data\02. Processed Data\intelligence_ready.pkl")
    return df

df = load_data()

# ---------------------------------------------------
# SIDEBAR TRAVEL PREFERENCES
# ---------------------------------------------------

st.sidebar.header('Travel Preferences')

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

selected_month = st.sidebar.selectbox('When do you want to travel?', 
                              options=months)

selected_experience = st.sidebar.selectbox('What type of experience are you looking for?', 
                                    options = ['All'] + list(df['category'].str.title().unique()))

crowd_level = ['Love the buzz', 'Prefer quiet']

selected_crowd = st.sidebar.radio('How do you feel about crowds?',
                                    options=crowd_level)

selected_weather = st.sidebar.radio('What is your weather preference?',
                                    options=list(df['weather'].str.title().unique()))

# ---------------------------------------------------
# FILTER DATAFRAME FOR RECOMMENDATIONS
# ---------------------------------------------------

filtered_df = df.copy()

#Month
best_mask = filtered_df['best_months'].str.lower().str.contains(
    selected_month.lower(),
    na=False
)

good_mask = filtered_df['good_months'].str.lower().str.contains(
    selected_month.lower(),
    na=False
)

filtered_df = filtered_df[best_mask | good_mask]

#Experience
if selected_experience != 'All':
    filtered_df = filtered_df[filtered_df['Category'] == selected_experience]

#Crowd level
crowd_dict = {
    'Love the buzz': ['high', 'very high'],
    'Prefer quiet': ['moderate', 'low']
}
filtered_df = filtered_df[filtered_df['crowd_level'].isin(crowd_dict[selected_crowd])]

#Weather preference
filtered_df = filtered_df[filtered_df['weather'] == selected_weather]

# ---------------------------------------------------
# SHOWING RECCOMENDATIONS
# ---------------------------------------------------

'''If tie: do random.sample(n=1)
If no destination, make a funny joke text and randomly select a destination to show as a "surprise recommendation"'''

col1, col2 = st.columns(2) 

with col1: 
    st.metric('Total Sales:', f'${total_sales:,.2f}')

''' Destination name and state
•	International draw rating
•	Weather and crowd level indicators'''

with col2:
    st.metric('Average Rating:', avg_rating)
'''•	Why this month is great for this place
•	Brief description and highlights'''

"""
Output for each destination:
•	Destination name and state
•	Why this month is great for this place
•	Brief description and highlights
•	International draw rating
•	Weather and crowd level indicators
"""

st.divider()

# ---------------------------------------------------
# FINAL MESSAGE
# ---------------------------------------------------

st.markdown('''
<h2 style='color:#4CAF50;'>
WE WISH YOU A GREAT TRIP!
</h2>
''', unsafe_allow_html=True)