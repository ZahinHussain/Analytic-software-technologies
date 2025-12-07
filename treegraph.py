import pandas as pd
import plotly.express as px

# --- Load CSV ---
df = pd.read_csv("nss2025.csv")

def topTree():

    val =5

    # 1. Clean the data FIRST
    clean_df = df.dropna(subset=['cah2_subject', 'cah3_subject'])

    # 2. Find the Top 10 CAH2 Subjects by Total Population
    #    (We sum them up to find out who is biggest)
    cah2_totals = clean_df.groupby('cah2_subject')['population'].sum()
    
    #    Get the NAMES of the top 10
    top_10_names = cah2_totals.sort_values(ascending=False).head(val).index
    
    print("Top 10 Subjects selected:")
    print(top_10_names)

    # 3. Filter the ORIGINAL dataframe to keep only those 10 subjects
    #    (This keeps the CAH3 data alive)
    df_top10 = clean_df[clean_df['cah2_subject'].isin(top_10_names)]

    # 4. Calculate total of just these 10
    total_pop = df_top10['population'].sum()

    # 5. Create the Chart
    fig = px.treemap(
        df_top10, 
        path=[px.Constant(f"Top {val} Subjects ({total_pop:,})"), 'cah2_subject', 'cah3_subject'], 
        values='population',                   
        color='cah2_subject',
        
        # Keep the "Pop" colors you liked
        color_discrete_sequence=px.colors.qualitative.Bold,
        hover_data={'population': ':,'}
    )

    # Styling: Thin borders, Tight margins, Readable text
    fig.update_traces(
        root_color="lightgrey",
        textinfo="label+value+percent parent",
        textfont=dict(size=15, family="Arial Black"),
        marker=dict(line=dict(color='#FFFFFF', width=0.5))
    )

    fig.update_layout(
        margin=dict(t=30, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode='hide')
    )
    
    fig.show()







def midTree():
    # 1. Clean the data
    clean_df = df.dropna(subset=['cah2_subject', 'cah3_subject'])

    # 2. Rank subjects by size
    cah2_totals = clean_df.groupby('cah2_subject')['population'].sum()
    
    # 3. FIX: Get the NAMES (.index) of the subjects ranked 11th to 20th
    #    iloc[10:20] grabs the "Mid Part"
    mid_names = cah2_totals.sort_values(ascending=False).iloc[5:15].index
    
    print("Subjects selected:")
    print(mid_names)

    # 4. Filter data to match these names
    df_mid = clean_df[clean_df['cah2_subject'].isin(mid_names)]

    # 5. Check if data is empty to prevent errors
    if df_mid.empty:
        print("No data found for this range!")
        return

    # 6. Calculate total
    total_pop = df_mid['population'].sum()

    # 7. Create the Chart
    fig = px.treemap(
        df_mid, 
        path=[px.Constant(f"Mid-Range Subjects ({total_pop:,})"), 'cah2_subject', 'cah3_subject'], 
        values='population',                   
        color='cah2_subject',
        
        # "Bold" colors (Clear Cut)
        color_discrete_sequence=px.colors.qualitative.Bold,
        hover_data={'population': ':,'}
    )

    # Styling
    fig.update_traces(
        root_color="lightgrey",
        textinfo="label+value+percent parent",
        textfont=dict(size=15, family="Arial Black"),
        marker=dict(line=dict(color='#FFFFFF', width=0.5))
    )

    fig.update_layout(
        margin=dict(t=30, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode='hide')
    )
    
    fig.show()



def lastTree():
    # 1. Clean the data FIRST
    clean_df = df.dropna(subset=['cah2_subject', 'cah3_subject'])

    # 2. Find the Top 10 CAH2 Subjects by Total Population
    #    (We sum them up to find out who is biggest)
    cah2_totals = clean_df.groupby('cah2_subject')['population'].sum()
    
    #    Get the NAMES of the top 10
    top_10_names = cah2_totals.sort_values(ascending=False).tail(15)
    
    print("Top 10 Subjects selected:")
    print(top_10_names)

    # 3. Filter the ORIGINAL dataframe to keep only those 10 subjects
    #    (This keeps the CAH3 data alive)
    df_top10 = clean_df[clean_df['cah2_subject'].isin(top_10_names)]

    # 4. Calculate total of just these 10
    total_pop = df_top10['population'].sum()

    # 5. Create the Chart
    fig = px.treemap(
        df_top10, 
        path=[px.Constant(f"Last 25 Subjects ({total_pop:,})"), 'cah2_subject', 'cah3_subject'], 
        values='population',                   
        color='cah2_subject',
        
        # Keep the "Pop" colors you liked
        color_discrete_sequence=px.colors.qualitative.Bold,
        hover_data={'population': ':,'}
    )

    # Styling: Thin borders, Tight margins, Readable text
    fig.update_traces(
        root_color="lightgrey",
        textinfo="label+value+percent parent",
        textfont=dict(size=15, family="Arial Black"),
        marker=dict(line=dict(color='#FFFFFF', width=0.5))
    )

    fig.update_layout(
        margin=dict(t=30, l=0, r=0, b=0),
        uniformtext=dict(minsize=10, mode='hide')
    )
    
    fig.show()

midTree()

