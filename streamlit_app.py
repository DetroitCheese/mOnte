'''
Converted to streamlit
'''
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to run the Monte Carlo simulation
def run_simulation(trials):
    tosses = np.random.choice(['Heads', 'Tails'], size=trials)
    heads_count = np.sum(tosses == 'Heads')
    tails_count = np.sum(tosses == 'Tails')
    return tosses, heads_count, tails_count

# Function to plot the results
def plot_results(tosses):
    fig, ax = plt.subplots()
    ax.hist(tosses, bins=2)
    return fig

# Streamlit app
st.title('Monte Carlo Simulation of Coin Tosses')

# Input for number of trials
trials = st.number_input('Enter the number of trials', min_value=1, max_value=1000000, value=1000)
if st.button('Run Simulation'):
    tosses, heads_count, tails_count = run_simulation(trials)
    st.write(f'Heads: {heads_count}')
    st.write(f'Tails: {tails_count}')
    st.pyplot(plot_results(tosses))
