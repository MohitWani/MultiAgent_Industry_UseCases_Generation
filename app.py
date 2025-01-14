import streamlit as st
from crewai import Crew
from utils.Agents import agents
from utils.Tasks import tasks



def run(industry_name):
    # Define the Crew with agents and tasks
    crew = Crew(
        agents=agents,
        tasks=tasks,
        max_rpm=29,  # requests per min limit
        verbose=True,
    )

    input_data = {
        'industry_name': industry_name
    }

    # Kick off the task
    crew.kickoff(inputs=input_data)

    try:
        with open("final_report.md", "r") as file:
            markdown_content = file.read()
        return markdown_content
    except FileNotFoundError:
        return "Error: The output file was not generated."

st.title('Market Research Agent')

query = st.text_input("Write a Industry Name")

if st.button("Submit"):
    st.write(run(query))
