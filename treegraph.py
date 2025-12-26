import pandas as pd
import plotly.express as px

# --- Load CSV ---
df = pd.read_csv("nss2025.csv")

import plotly.express as px

import pandas as pd
import plotly.express as px

def topTree():
    # Load the data
    df = pd.read_csv("onlyUni.csv")

    val =4

    # 1. Clean the data FIRST by removing rows with NaN values in important columns
    clean_df = df.dropna(subset=['cah2_subject', 'cah3_subject'])

    # 2. Drop duplicates based on 'cah3_subject' and 'provider'
    clean_df = clean_df.drop_duplicates(subset=['cah3_subject', 'provider'])

    # 3. Find the Total Population for each 'cah2_subject'
    cah2_totals = clean_df.groupby('cah2_subject')['population'].sum()

    # 4. Get the Top 10 CAH2 Subjects by Total Population
    top_10_names = cah2_totals.sort_values(ascending=False).iloc[20:].index

    print("Top 10 Subjects selected:")
    print(top_10_names)

    # 5. Filter the ORIGINAL cleaned dataframe to only include these top 10 subjects
    df_top10 = clean_df[clean_df['cah2_subject'].isin(top_10_names)]

    # 6. Calculate the total population of these top 10 subjects
    total_pop = df_top10['population'].sum()

    # 7. Create the Treemap Chart
    fig = px.treemap(
        df_top10, 
        path=[px.Constant(f"Top {val} FEHE Subjects ({total_pop:,})"), 'cah2_subject', 'cah3_subject'], 
        values='population',                   
        color='cah2_subject',
        
        # Color options for the subjects
        color_discrete_sequence=px.colors.qualitative.Bold,
        hover_data={'population': ':,'}
    )

    # Styling: Thin borders, tight margins, readable text
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

    # Show the chart
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


    clean_df = clean_df.drop_duplicates(subset=['cah3_subject', 'provider'])

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



def totalTree():
    df = pd.read_csv("FEHE.csv")

    # Collapse the 27 questions FIRST
    base_df = (
        df
        .groupby(
            ['provider', 'cah1_subject', 'cah2_subject', 'cah3_subject'],
            as_index=False
        )
        .agg(population=('population', 'first'))
    )

    total_pop = base_df['population'].sum()

    fig = px.treemap(
        base_df,
        path=[
            px.Constant(f"All Subjects Student Populations ({total_pop:,})"),
            'cah2_subject',
            'cah3_subject',
       
        ],
        values='population',
        color='cah1_subject',
        color_discrete_sequence=px.colors.qualitative.Bold,
        hover_data={'population': ':,'}
    )

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





def topHalf():



    clean_df = df.dropna(subset=['cah2_subject', 'cah3_subject'])


    clean_df = clean_df.drop_duplicates(subset=['cah3_subject', 'provider'])

    total_pop = df['population'].sum()


    halfPop = total_pop/2

    fig = px.treemap(
        clean_df, 
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



def onluUni():
    df = pd.read_csv("nss2025.csv")

    # 1. Clean the data
    clean_df = df.dropna(subset=['cah2_subject', 'cah3_subject', 'provider'])

    # 2. REMOVE DUPLICATES to calculate accurate Total Population
    #    We create a temporary dataframe 'unique_courses' 
    #    We assume a unique course is a specific Subject at a specific Provider
    unique_courses = clean_df.drop_duplicates(subset=['cah3_subject', 'provider'])

    # 3. Calculate total of just the unique courses
    total_pop = unique_courses['population'].sum()
    
    print(f"Total Unique Population: {total_pop:,}")

    # 4. Create the Chart
    #    Note: Depending on your data, you might want to use 'unique_courses' 
    #    in the treemap too if the duplicates were causing visual errors.
    #    If you want the chart to use the deduped data, change 'clean_df' to 'unique_courses' below:
    fig = px.treemap(
        unique_courses, 
        path=[px.Constant(f"All Subjects ({total_pop:,})"), 'cah2_subject', 'cah3_subject', 'provider'], 
        values='population',                   
        color='cah2_subject',
        
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

# Run the function


#

topTree()



#totalTree()




