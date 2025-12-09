import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

# -----------------------------------------
# LOAD DATA
# -----------------------------------------
def load_data(path="nss2025.csv"):
    return pd.read_csv(path)


# -----------------------------------------
# PROCESSING: group, sort, remove last row
# -----------------------------------------
def process_subject_counts(df):
    subject_counts = (
        df.groupby(['cah2_subject'])
['population']
        .sum()
        .reset_index()
        .sort_values('population', ascending=False)
    )
    return subject_counts


# -----------------------------------------
# CHECK IF CURRENT TOTAL <= TARGET 
# -----------------------------------------
def reached_target(subject_counts, target):
    current_sum = subject_counts['population'].sum()
    return current_sum <= target


# -----------------------------------------
# REMOVE ROWS UNTIL TARGET REACHED
# -----------------------------------------
def trim_until_target(subject_counts, target):
    # Keep removing last row until <= target
    while True:
        if reached_target(subject_counts, target):
            break
        subject_counts = subject_counts.iloc[:-1]

    return subject_counts


# -----------------------------------------
# MAIN
# -----------------------------------------


'''
df = load_data()

subject_counts = process_subject_counts(df)

total_pop_target = df['population'].sum() *0.5

print("Initial rows:", len(subject_counts))



# Now trim until <= target
subject_counts = trim_until_target(subject_counts, total_pop_target)

print("Final rows:", len(subject_counts))
print(subject_counts)

fig = px.treemap(
        subject_counts, 
        path=[px.Constant(f"Last 25 Subjects ({total_pop_target:,})"), 'cah1_subject','cah2_subject'], 
        values='population',                   
        color='cah1_subject',
        
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



'''



df = load_data()

subject_counts = process_subject_counts(df)

total_pop_target = df['population'].sum() *0.5

print("Initial rows:", len(subject_counts))



# Now trim until <= target
subject_counts = trim_until_target(subject_counts, total_pop_target)

print("Final rows:", len(subject_counts))
print(subject_counts)

fig = px.treemap(
        subject_counts, 
        path=[px.Constant(f"Last 25 Subjects ({total_pop_target:,})"), 'cah2_subject'], 
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
