import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------------------------
# Page configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Nassau Candy Factory Optimization",
    page_icon="🍬",
    layout="wide"
)


# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("🍬 Nassau Candy Factory Reallocation & Shipping Optimization")

st.markdown(
    """
    ### Decision-Intelligence Dashboard

    This application demonstrates the results of a machine-learning-based
    factory reallocation analysis for Nassau Candy Distributor.

    The dashboard evaluates potential factory movements using modeled
    lead-time improvement, profitability, factory distance, and evidence level.
    """
)


# -------------------------------------------------
# Load final recommendation data
# -------------------------------------------------

@st.cache_data
def load_data():

    file_path = "outputs/Nassau_Candy_Final_Recommendations.csv"

    df = pd.read_csv(file_path)

    return df


df = load_data()


# -------------------------------------------------
# KPI calculations
# -------------------------------------------------

move_df = df[df["Recommendation"] == "MOVE CANDIDATE"].copy()

validate_df = df[df["Recommendation"] == "VALIDATE FIRST"].copy()

no_change_df = df[df["Recommendation"] == "NO CHANGE"].copy()


products_analyzed = len(df)

move_products = len(move_df)

validate_products = len(validate_df)

no_change_products = len(no_change_df)

orders_covered = move_df["Orders"].sum()

potential_days = move_df["Potential Total Order Days Reduced"].sum()

sales = move_df["Sales"].sum()

profit = move_df["Profit"].sum()


# -------------------------------------------------
# KPI section
# -------------------------------------------------

st.subheader("Executive KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Products Analyzed",
    products_analyzed
)

col2.metric(
    "Move Candidates",
    move_products
)

col3.metric(
    "Orders Covered",
    f"{orders_covered:,.0f}"
)

col4.metric(
    "Potential Modeled Order-Days Reduced",
    f"{potential_days:,.2f}"
)


col5, col6, col7 = st.columns(3)

col5.metric(
    "Validate First",
    validate_products
)

col6.metric(
    "No Change",
    no_change_products
)

col7.metric(
    "Associated Profit",
    f"{profit:,.2f}"
)


# -------------------------------------------------
# Recommendation distribution
# -------------------------------------------------

st.subheader("Recommendation Distribution")

recommendation_counts = df["Recommendation"].value_counts()

fig, ax = plt.subplots()

recommendation_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Recommendation")
ax.set_ylabel("Number of Products")
ax.set_title("Product Recommendation Distribution")

plt.xticks(rotation=0)

st.pyplot(fig)


# -------------------------------------------------
# Factory movement table
# -------------------------------------------------

st.subheader("Recommended Factory Movements")

movement_columns = [
    "Product",
    "Current Factory",
    "Recommended Factory",
    "Orders",
    "Avg Lead-Time Reduction (Days)",
    "Lead-Time Improvement (%)",
    "Recommendation"
]

available_columns = [
    column for column in movement_columns
    if column in df.columns
]

st.dataframe(
    move_df[available_columns],
    use_container_width=True
)


# -------------------------------------------------
# Product impact
# -------------------------------------------------

st.subheader("Potential Modeled Impact by Product")

impact_columns = [
    "Product",
    "Potential Total Order Days Reduced",
    "Sales",
    "Profit"
]

available_impact_columns = [
    column for column in impact_columns
    if column in move_df.columns
]

if "Potential Total Order Days Reduced" in move_df.columns:

    impact_plot = move_df.sort_values(
        "Potential Total Order Days Reduced",
        ascending=False
    )

    fig2, ax2 = plt.subplots()

    ax2.bar(
        impact_plot["Product"],
        impact_plot["Potential Total Order Days Reduced"]
    )

    ax2.set_xlabel("Product")
    ax2.set_ylabel("Potential Modeled Order-Days Reduced")

    ax2.set_title(
        "Potential Modeled Impact by Product"
    )

    plt.xticks(
        rotation=75,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig2)


# -------------------------------------------------
# Full recommendation table
# -------------------------------------------------

st.subheader("Complete Recommendation Table")

st.dataframe(
    df,
    use_container_width=True
)


# -------------------------------------------------
# Important interpretation
# -------------------------------------------------

st.subheader("⚠️ Important Interpretation")

st.info(
    """
    These recommendations are analytical decision-support outputs rather
    than guaranteed operational outcomes.

    The selected Gradient Boosting model achieved an R² of approximately
    0.042, meaning that the model explains only a small portion of observed
    lead-time variation.

    Therefore, factory movements should be validated using operational
    constraints, factory capacity, transportation costs, inventory,
    production requirements, and pilot testing before implementation.
    """
)


# -------------------------------------------------
# Project methodology
# -------------------------------------------------

with st.expander("View Project Methodology"):

    st.markdown(
        """
        **Dataset**

        - 10,194 records
        - 18 original variables
        - 15 products
        - 5 factories

        **Machine Learning**

        Three regression models were evaluated:

        - Linear Regression
        - Random Forest
        - Gradient Boosting

        Gradient Boosting was selected for scenario simulation.

        **Scenario Simulation**

        40,776 factory-assignment scenarios were evaluated.

        **Recommendation Framework**

        The project considers:

        - 50% Lead-Time Improvement
        - 30% Profitability
        - 20% Factory Distance

        **Evidence Safeguard**

        - 100+ orders → Higher Evidence
        - 30–99 orders → Medium Evidence
        - <30 orders → Validate First
        """
    )


st.caption(
    "Nassau Candy Factory Reallocation & Shipping Optimization | "
    "Machine Learning & Decision Intelligence Project"
)
