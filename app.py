import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd
import time
from sklearn.datasets import fetch_california_housing

st.title('🏠House Price prediction using ML')
st.image('https://i.pinimg.com/originals/f1/be/c8/f1bec81e20d80cd36c82379af920a4e9.gif')
