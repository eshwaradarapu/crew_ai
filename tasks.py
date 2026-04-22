from crewai import Task

from agents import researcher, reviewer, writer
from models import ReviewerOutput


research_task = Task(
    description=(
        "Research the topic: '{topic}'. Collect key facts, recent developments, "
        "important context, and reliable references. Focus on accuracy and relevance."
    ),
    expected_output=(
        "A structured research brief with: overview, key points, supporting evidence, "
        "and a short source list."
    ),
    agent=researcher,
)

write_task = Task(
    description=(
        "Using the research brief, write a well-structured report/article on '{topic}'. "
        "Use clear sections and coherent flow."
    ),
    expected_output=(
        "A polished report/article with title, introduction, body sections, and conclusion."
    ),
    agent=writer,
    context=[research_task],
)

review_task = Task(
    description=(
        "Review the drafted report for quality, factual consistency, completeness, and clarity. "
        "Evaluate strengths and weaknesses and provide a final verdict."
    ),
    expected_output=(
        "Return your review in this exact format:\n"
        "score: <1-10 integer>\n"
        "strengths: <list of strengths>\n"
        "weaknesses: <list of weaknesses>\n"
        "final_verdict: <Approved | Needs Revision>"
    ),
    agent=reviewer,
    context=[write_task],
    output_pydantic=ReviewerOutput,
)
