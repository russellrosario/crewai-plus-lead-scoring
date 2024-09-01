from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

from typing import List
from pydantic import BaseModel, Field

class LeadScore(BaseModel):
	lead_score: float = Field(..., description="The score of the lead between 0 - 10")
	use_case_summary: str = Field(..., description="The summary of the use case of the lead")
	talking_points: List[str] = Field(..., description="The talking points and ideas for an email and  call with the lead")

@CrewBase
class CrewaiPlusLeadScoringCrew():
	"""CrewaiPlusLeadScoring crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def lead_analysis_agent(self) -> Agent:
			return Agent(
					config=self.agents_config['lead_analysis_agent'],
					tools=[SerperDevTool(), ScrapeWebsiteTool()],
					allow_delegation=False,
					verbose=True
			)

	@agent
	def research_agent(self) -> Agent:
			return Agent(
					config=self.agents_config['research_agent'],
					tools=[SerperDevTool(), ScrapeWebsiteTool()],
					allow_delegation=False,
					verbose=True
			)

	@agent
	def scoring_and_planning_agent(self) -> Agent:
			return Agent(
					config=self.agents_config['scoring_and_planning_agent'],
					tools=[SerperDevTool(), ScrapeWebsiteTool()],
					verbose=True
			)

	@task
	def lead_analysis_task(self) -> Task:
			return Task(
					config=self.tasks_config['lead_analysis_task'],
					agent=self.lead_analysis_agent()
			)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.research_agent()
		)

	@task
	def scoring_and_planning_task(self) -> Task:
		return Task(
			config=self.tasks_config['scoring_and_planning_task'],
			agent=self.scoring_and_planning_agent(),
			output_json=LeadScore
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the LeadQualification and Research Crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=2
		)
