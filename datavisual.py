import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("nss2025.csv")

tab1, tab2, tab3 = st.tabs(["Population with subject cat", "Charts", "Search"])

with tab1:
    st.header("Overview")
    st.write("Population distributions by subject categories")

    # ========= CAH1 =========
    st.subheader("Population by CAH1")

    cah1_options = sorted(df["cah1_subject"].dropna().unique())
    cah1_filter = st.selectbox("Filter CAH1", ["All"] + cah1_options)

    if cah1_filter != "All":
        df1 = df[df["cah1_subject"] == cah1_filter]
    else:
        df1 = df

    cah1_pop = (
        df1.groupby("cah1_subject")["population"]
        .sum()
        .sort_values()
    )

    fig1, ax1 = plt.subplots(figsize=(10, max(4, len(cah1_pop) * 0.4)))
    ax1.barh(cah1_pop.index, cah1_pop.values)
    ax1.set_xlabel("Population")
    ax1.set_ylabel("CAH1 Subject")
    plt.tight_layout()
    st.pyplot(fig1)

    # ========= CAH2 =========
    st.subheader("Population by CAH2")

    cah2_options = sorted(df["cah2_subject"].dropna().unique())
    cah2_filter = st.selectbox("Filter CAH2", ["All"] + cah2_options)

    if cah2_filter != "All":
        df2 = df[df["cah2_subject"] == cah2_filter]
    else:
        df2 = df

    cah2_pop = (
        df2.groupby("cah2_subject")["population"]
        .sum()
        .sort_values()
    )

    fig2, ax2 = plt.subplots(figsize=(10, max(4, len(cah2_pop) * 0.4)))
    ax2.barh(cah2_pop.index, cah2_pop.values)
    ax2.set_xlabel("Population")
    ax2.set_ylabel("CAH2 Subject")
    plt.tight_layout()
    st.pyplot(fig2)

    # ========= CAH3 =========
    st.subheader("Population by CAH3")

    cah3_options = sorted(df["cah3_subject"].dropna().unique())
    cah3_filter = st.selectbox("Filter CAH3", ["All"] + cah3_options)

    if cah3_filter != "All":
        df3 = df[df["cah3_subject"] == cah3_filter]
    else:
        df3 = df

    cah3_pop = (
        df3.groupby("cah3_subject")["population"]
        .sum()
        .sort_values()
    )

    fig3, ax3 = plt.subplots(figsize=(10, max(4, len(cah3_pop) * 0.4)))
    ax3.barh(cah3_pop.index, cah3_pop.values)
    ax3.set_xlabel("Population")
    ax3.set_ylabel("CAH3 Subject")
    plt.tight_layout()
    st.pyplot(fig3)


    # ========= CAH2 to 3  =========
    st.subheader("Population by CAH2 with CAH3 filter")

        # --- Dropdown for CAH2 ---
    cah2_options = sorted(df["cah2_subject"].dropna().unique())
    cah2_filter = st.selectbox("Filter CAH2", ["All"] + cah2_options, key="cah2_filter")

    # --- Filter dataframe based on CAH2 selection ---
    if cah2_filter != "All":
        df_filtered = df[df["cah2_subject"] == cah2_filter]
    else:
        df_filtered = df.copy()

   



    # --- Group by CAH3 and calculate population sums ---
    cah3_pop = df_filtered.groupby("cah3_subject")["population"].sum().sort_values()

    # --- Plot ---
    fig3, ax3 = plt.subplots(figsize=(10, max(4, len(cah3_pop) * 0.4)))
    ax3.barh(cah3_pop.index, cah3_pop.values, color="blue")
    ax3.set_xlabel("Population")
    ax3.set_ylabel("CAH3 Subject")
    ax3.set_title(f"Population for CAH2: {cah2_filter}")
    plt.tight_layout()
    st.pyplot(fig3)

with tab2:
    import streamlit as st
    import matplotlib.pyplot as plt

    st.subheader("Population by CAH2 with CAH3 filter")

    # --- Dropdown for CAH3 ---
    cah3_options = sorted(df["cah1_subject"].dropna().unique())
    cah3_filter = st.selectbox(
        "Filter CAH1",
        ["All"] + cah3_options,
        key="cah3_filter"
    )

    # --- Filter dataframe ---
    if cah3_filter != "All":
        df_filtered = df[df["cah1_subject"] == cah3_filter]
    else:
        df_filtered = df.copy()

    # --- Aggregate data ---
    top_10 = (
        df_filtered
        .groupby("question", as_index=False)
        .agg(mean_agree_pct=("agree_pct", "mean"))
        .sort_values("mean_agree_pct", ascending=True)
    )

    # --- Prepare plotting lists ---
    questionToPlot = []
    answerValues = []

    for _, row in top_10.iterrows():
        questionToPlot.append(row["question"])
        answerValues.append(row["mean_agree_pct"])

    # --- Plot ---
    fig, ax = plt.subplots(figsize=(12, 10))

    ax.barh(questionToPlot, answerValues)
    ax.set_xlabel("Percentage")
    ax.set_title("Results by Question")
    ax.grid(axis="x", linestyle="--", alpha=0.7)
    ax.invert_yaxis()

    plt.tight_layout()

    # --- Streamlit render ---
    st.pyplot(fig)




    # -----------------------------

    # --- THE PLOTTING CODE (FIXED) ---




    




with tab3:
    st.header("Search")
    st.write("Add search tools here.")
