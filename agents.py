from crewai import Agent, LLM
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

llm = LLM(model="groq/llama-3.3-70b-versatile")


researcher = Agent(
    role="Researcher Agent",
    goal=(
        "Gather accurate, relevant, and well-organized information about the given topic "
        "from reliable sources."
    ),
    backstory=(
        "You are an expert research analyst known for quickly finding trustworthy "
        "information, identifying key insights, and separating facts from noise."
    ),
    llm=llm,
    tools=[search_tool],
    verbose=True,
    allow_delegation=False,
)

writer = Agent(
    role="Writer Agent",
    goal=(
        "Write a clear, structured, and engaging report/article about the topic "
        "using the Researcher Agent's findings as the primary context."
    ),
    backstory=(
        "You are a professional content writer who transforms raw research into "
        "well-structured reports with strong flow, logical sections, and clear language."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

reviewer = Agent(
    role="Reviewer Agent",
    goal=(
        "Review the written report for quality, factual consistency, completeness, "
        "and clarity. Provide  actionable feedback."
    ),
    backstory=(
        "You are a meticulous editor and quality reviewer. You spot weak arguments, "
        "missing context, and unclear writing, then provide precise suggestions to improve it."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)
