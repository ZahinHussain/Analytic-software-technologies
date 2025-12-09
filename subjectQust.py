
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- YOUR CODE (UNCHANGED) ---
questionToPlot = [] 
df = pd.read_csv("nss2025.csv")
# Get the list of subjects
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. DATA PREPARATION ---
questionToPlot = [] 

# Get the list of subjects
totalCha1 = df["cah1_subject"].unique().tolist()

# <--- FIX: We must loop through subjects here to define 'subject_df'
for subject in totalCha1:
    
    # Filter for the current subject
    subject_df = df[df["cah1_subject"] == subject]

    # Calculate Top 10
    top_10 = (subject_df.groupby('question', as_index=False)
                .agg(mean_agree_pct=('agree_pct', 'mean'))
                .sort_values('mean_agree_pct', ascending=True)
                .head(10))

    # Append to list
    for index, row in top_10.iterrows():
        questionToPlot.append([
            subject,                       # <--- FIX: We need this for the colors!
            row['question'],               # The question
            float(row['mean_agree_pct'])   # The score
        ])

# Check the first item
if len(questionToPlot) > 0:
    print(questionToPlot[0]) 

# --- 2. PLOTTING CODE ---

plt.figure(figsize=(15, 10))

# Create distinct colors for every subject
colors = plt.cm.rainbow(np.linspace(0, 1, len(totalCha1)))

# Loop through the subjects to plot them with their specific color
for j in range(len(totalCha1)):
    
    current_subject = totalCha1[j]
    current_color = colors[j]
    
    # Temporary lists for this specific subject
    x_questions = []
    y_scores = []
    
    # Extract data for this subject from our main list
    for row in questionToPlot:
        # row is [Subject, Question, Score]
        if row[0] == current_subject:
            x_questions.append(row[1]) 
            y_scores.append(row[2])    

    # Plot the scatter dots
    plt.scatter( y_scores, x_questions,color=current_color, label=current_subject, s=100, alpha=0.7)

# --- 3. FORMATTING ---
plt.xticks(rotation=90, fontsize=8) # Rotate text so it fits
plt.ylabel("Score (%)")
plt.xlabel("Questions")
plt.title("Scores by Question (Colored by Subject)")

# Move legend outside because 30 subjects takes up too much space
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Subjects")
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

plt.show()