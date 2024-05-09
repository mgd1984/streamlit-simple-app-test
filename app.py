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
    st.title('LLM Context Window Length vs. Cost-per-Token')

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

def page2():
    st.title('Page 2')
    st.write('This is page 2')

def page3():
    st.title('Page 3')
    st.write('This is page 3')

if __name__ == '__main__':
    st.sidebar.title('Navigation')
    pages = ['Main', 'Page 2', 'Page 3']
    page = st.selectbox('Go to', pages)

    if page == 'Main':
        main()
    elif page == 'Page 2':
        page2()
    elif page == 'Page 3':
        page3()

