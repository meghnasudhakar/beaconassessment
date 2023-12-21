import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Data Dashboard",
    layout="wide",
)

st.title("Github Repository Data Dashboard")

repository_data = pd.read_csv("/Users/msudhakar/Documents/streamlitproject/github_dataset.csv")
largest_lang = repository_data['language'].value_counts().nlargest(5)

langlist = largest_lang.index.to_list()

largest_lang_df = repository_data[repository_data["language"].isin(langlist)]


dataset, graphs_button = st.tabs(["Dataset", "Exploratory Analysis"])

with dataset:
    st.write("View the dataset below using the project language filter!")
    lang_filter = st.selectbox("Select the Project Language", pd.unique(repository_data["language"]))
    df2 = repository_data[repository_data["language"] == lang_filter]
    st.write(df2)

with graphs_button:
    heatmap_graphs = px.density_heatmap(title = "Heatmap of Top 5 Most Frequently Used Languages", 
                                        data_frame = largest_lang_df, x = "language")
    st.write(heatmap_graphs)
    st.write("This graph displays a heatmap of the top 5 most frequently used languages\
                in the github dataset. We can see that JavaScript is used most frequently\
                among all repositories.")

    histogram1 = px.histogram(title = "Histogram of Dataset Stars", data_frame=repository_data, x="stars_count")
    st.write(histogram1)

    histogram2 = px.histogram(title = "Histogram of Dataset Forks", data_frame=repository_data, x="forks_count")
    st.write(histogram2)

    histogram3 = px.histogram(title ="Histogram of Dataset Pull Requests", data_frame=repository_data, x="pull_requests")
    st.write(histogram3)

    st.write("From the above three histograms, it is clear that a majority of data\
                regarding stars, forks, and pull requests for the github repositories\
                    are heavily right skewed with a majority of the data concentrated\
                        around the lower end of the ranges. All histograms show thin\
                            and sparsely populated tails.")

    heatmap1 = px.scatter(title = "Scatterplot of Forks and Stars", data_frame=repository_data, y="stars_count", x="forks_count")
    st.write(heatmap1)

    heatmap2 = px.scatter(title ="Scatterplot of Pull Requests and Stars", data_frame=repository_data, y="stars_count", x="pull_requests")
    st.write(heatmap2)

    st.write("While the second scatterplot does not provide much information about the\
        association between the number of pull requests and the dataset stars, there is a \
            clearer relationship between the number of forks and stars from the first\
                scatterplot. As the number of forks increase, we see a higher number of\
                    stars as well. While we cannot make a conclusive insight without the\
                        corresponding statistical tests, this pattern would be interesting\
                            to further investigate.")
    


