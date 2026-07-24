import streamlit as st

from tools.weather_tool import weather_information


st.set_page_config(
    page_title="Weather Information MCP",
    page_icon="🌤"
)


st.title("🌤 Weather Information MCP")

st.write(
    "Search any city and get current weather information"
)


city = st.text_input(
    "Enter City Name"
)


if st.button("Get Weather"):

    if city:

        result = weather_information(city)


        if "error" in result:

            st.error(result["error"])


        else:

            st.success(
                "Weather Found"
            )


            st.subheader(
                f'{result["Location"]}, {result["Country"]}'
            )


            col1, col2 = st.columns(2)


            with col1:

                st.metric(
                    "Temperature",
                    result["Temperature"]
                )


            with col2:

                st.metric(
                    "Humidity",
                    result["Humidity"]
                )


            st.write(
                "☁ Condition:",
                result["Weather"]
            )
