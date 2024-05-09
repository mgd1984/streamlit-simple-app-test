import streamlit as st
import pandas as pd

import plotly.express as px

def main():
    data = {
        "Model": ["GPT-3", "GPT-3.5 Turbo", "GPT-4", "GPT-4 Turbo", "GPT-5", "GPT-5-Turbo"],
        "Context Window Length": [4096, 16000, 32000, 128000, 512000, 1024000],
        "Cost per Token (USD)": [100, 80, 40, 30, 20, 15],
        "Parameter Count (Billions)": [175, 80, 1800, 400, 18000, 4000]
    }
    df = pd.DataFrame(data)

    # Streamlit Interface
    st.title('Relationship Between Context Window Length and Cost-per-Token in LLMs')

    # Plotting
    fig = px.scatter(df, x="Context Window Length", y="Cost per Token (USD)", 
                title="Cost per Token vs. Context Window Length",
                labels={"Cost per Token (USD)": "Cost per Token (USD)",
                        "Context Window Length": "Context Window Length (tokens)"},
                hover_data=["Model"],
                size="Parameter Count (Billions)",
                color="Model",
                size_max=30,
                color_continuous_scale="viridis")
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()