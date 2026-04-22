from crewai import Crew, Process

from agents import researcher, reviewer, writer
from tasks import research_task, review_task, write_task


crew = Crew(
    agents=[researcher, writer, reviewer],
    tasks=[research_task, write_task, review_task],
    process=Process.sequential,
    verbose=True,
)


if __name__ == "__main__":
    topic = input("Enter a topic: ").strip()
    result = crew.kickoff(inputs={"topic": topic})
    print(result)
