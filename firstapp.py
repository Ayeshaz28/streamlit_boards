import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px

df = px.data.gapminder().query("continent=='Asia'")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
              size="pop", color="country", hover_name="country",
                log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
fig.show()
