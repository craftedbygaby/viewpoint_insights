import streamlit as st
import pandas as pd

st.markdown("""
<style>
.stApp {
    background-color: #f0f7f0;
}

section[data-testid="stSidebar"] {
    background-color: #e8f4e8;
}

.stButton > button {
    background-color: #009c3b;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER 
# ---------------------------------------------------

col1, col2, col3 = st.columns([0.5, 2, 0.5])
with col2:
    st.image(r"C:\Users\gabri\Documents\Data Analysis\Github\Viewpoint_Insights_final_project_IronHack\src\viewpoint_insights_logo.svg", width=550)

# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------

st.title('Brazil Travel Recommendation App')
st.markdown("<p style='color: #c8902a; font-size: 14px; margin-top: -15px;'>Find your perfect Brazilian destination</p>", unsafe_allow_html=True)

st.markdown('This App allows you to choose your travel preferences and get a recommendation based on them')
st.markdown("""
Use the filters on the left to tell us about your ideal trip:
- **When** you want to travel
- **What type of experience** you are looking for
- **How you feel about crowds**
- **Your weather preference**

We will recommend a Brazilian destination that matches your preferences — including the best time to visit, what makes it special, and what to expect in terms of weather and crowds.
""")

st.divider()

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data #it will be saved inside the internal memory and won't run everytime we run the code
def load_data():

    df = pd.read_csv(r"C:\Users\gabri\Documents\Data Analysis\Github\Viewpoint_Insights_final_project_IronHack\01. Data\02. Processed Data\intelligence_ready_w_images.csv")
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
# SAVING THE FILTERS AND RUNNING THE RECOMMENDATION BASED ON FILTERS (AND SAVING IT TO SHOW LATER)
# ---------------------------------------------------
if st.sidebar.button('Find my destination!'):
    st.session_state['search_clicked'] = True
    st.session_state['month'] = selected_month

    filtered_df = df.copy()

    best_mask = filtered_df['best_months'].str.lower().str.contains(selected_month.lower(), na=False)
    good_mask = filtered_df['good_months'].str.lower().str.contains(selected_month.lower(), na=False)
    filtered_df = filtered_df[best_mask | good_mask]

    if selected_experience != 'All':
        filtered_df = filtered_df[filtered_df['category'] == selected_experience]

    crowd_dict = {'Love the buzz': ['high', 'very high'], 'Prefer quiet': ['moderate', 'low']}
    filtered_df = filtered_df[filtered_df['crowd_level'].isin(crowd_dict[selected_crowd])]

    filtered_df = filtered_df[filtered_df['weather'] == selected_weather.lower()]

    if filtered_df.empty:
        st.session_state['rec'] = df.sample(n=1).iloc[0]
        st.session_state['no_match'] = True
    else:
        st.session_state['rec'] = filtered_df.sample(n=1).iloc[0]
        st.session_state['no_match'] = False

# ---------------------------------------------------
# SHOWING RECOMMENDATIONS
# ---------------------------------------------------

if st.session_state.get('search_clicked'):

    if st.session_state['no_match']:
        st.warning("You unlocked the ‘impossibly specific traveler’ achievement 🏆 Here’s a destination to inspire you!")
                    ### Options
                    ### No exact match found — but great adventures often start unexpectedly ✈️ Here’s a destination to inspire you!
                    ### Your preferences are as unique as you are! While we couldn't find an exact match, here's a destination that might just surprise you 🌟
                    ### We searched harder than someone looking for cheap flights at 2am… but no exact match 😭 Here’s a fun alternative!

    rec = st.session_state['rec']

    st.markdown(f"<h2 style='text-align: center;'>{rec['destination']}</h2>", unsafe_allow_html=True)

    if pd.notna(rec['image_url']) and rec['image_url'] != '':
        st.image(rec['image_url'], use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**State:** {rec['state']}")
        st.markdown(f"**Best months:** {rec['best_months']}")
        if pd.notna(rec['good_months']) and rec['good_months'] != '':
            st.markdown(f"**Good months:** {rec['good_months']}")
        st.markdown(f"**Weather:** {rec['weather'].capitalize()}")
        st.markdown(f"**Crowd level:** {rec['crowd_level'].capitalize()}")

    with col2:
        if st.session_state['no_match']:
            st.markdown(f"**Best months to visit:**")
            st.write(rec['best_months'])
        else:
            st.markdown(f"**Why visit in {st.session_state['month']}:**")
            st.write(rec['why_best'])
        st.markdown(f"**About:**")
        st.write(rec['description'])

else:
    st.info("Set your travel preferences on the left and click **Find my destination!** to get a recommendation.")

st.markdown("""
---
**Want to explore more?** Visit the official Brazil tourism website for deeper inspiration and travel planning:  
[visitbrasil.com](https://visitbrasil.com/en/)
""")

st.divider()

# ---------------------------------------------------
# FINAL MESSAGE
# ---------------------------------------------------

st.markdown("""
<div style="display:flex; justify-content:center; align-items:center; gap:15px;">

<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg" width="50">

<span style="color:#009c3b; font-size:30px; font-weight:bold;">
WE WISH YOU A GREAT TRIP!
</span>

<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg" width="50">

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()
st.markdown("""
<p style='text-align: center; color: grey; font-size: 12px;'>
© 2026 Viewpoint Insights. All rights reserved. | Turning data into direction.
</p>
""", unsafe_allow_html=True)