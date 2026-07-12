import streamlit as st
import snowflake.connector
import pandas as pd

# Page config
st.set_page_config(
    page_title="World Cup 2026 Dashboard",
    page_icon="⚽",
    layout="wide"
)

# Snowflake connection
@st.cache_resource
def get_connection():
    return snowflake.connector.connect(
        account=st.secrets["snowflake"]["account"],
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database=st.secrets["snowflake"]["database"],
        schema=st.secrets["snowflake"]["schema"],
        role=st.secrets["snowflake"]["role"]
    )

@st.cache_data
def run_query(query):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query)
    df = pd.DataFrame(cur.fetchall(), columns=[desc[0] for desc in cur.description])
    return df

# Sidebar navigation
st.sidebar.title("⚽ WC 2026")
page = st.sidebar.radio(
    "Navigate",
    ["Match Results", "Group Standings", "Team Performance", "Top Scorers"]
)

# ── Match Results page ────────────────────────────────────────────
if page == "Match Results":
    st.title("🏆 Match Results")
    df = run_query("""
    SELECT DISTINCT * FROM MART_MATCH_RESULTS 
    ORDER BY MATCH_ID """)
    st.dataframe(df, use_container_width=True)
    
# ── Group Standings ───────────────────────────────────────────────
elif page == "Group Standings":
    st.title("📊 Group Standings")
    df = run_query("""
        SELECT * FROM MART_GROUP_STANDINGS 
        ORDER BY GROUP_NAME, POINTS DESC, GOAL_DIFFERENCE DESC
    """)
    for group in df['GROUP_NAME'].unique():
        st.subheader(f"Group {group.replace('GROUP_', '')}")
        st.dataframe(
            df[df['GROUP_NAME'] == group].drop(columns=['GROUP_NAME']),
            use_container_width=True
        )

# ── Team Performance ──────────────────────────────────────────────
elif page == "Team Performance":
    st.title("⚽ Team Performance")
    df = run_query("""
        SELECT * FROM MART_TEAM_PERFORMANCE 
        ORDER BY TOTAL_GOALS_SCORED DESC
    """)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index('TEAM')['TOTAL_GOALS_SCORED'])

# ── Top Scorers ───────────────────────────────────────────────────
elif page == "Top Scorers":
    st.title("🥇 Top Scorers")
    df = run_query("""
        SELECT * FROM MART_TOP_SCORERS 
        ORDER BY GOAL_RANK
    """)
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index('PLAYER_NAME')['GOALS'])