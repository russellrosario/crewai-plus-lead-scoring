#!/usr/bin/env python
from crewai_plus_lead_scoring.crew import CrewaiPlusLeadScoringCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs',
        'company': 'Salesloft',
        'icp_description': 'AI-Powered Lead Scoring System',
        'product_name': 'AI-Powered Lead Scoring System',
        'form_response': 'I like AI',
        'product_description': 'AI-Powered Lead Scoring System'
    }
    CrewaiPlusLeadScoringCrew().crew().kickoff(inputs=inputs)