from pydantic import BaseModel, Field


class ReviewerOutput(BaseModel):
	score: int = Field(..., ge=1, le=10, description="Final review score from 1 to 10")
	strengths: list[str] = Field(..., description="Key strengths of the article/report")
	weaknesses: list[str] = Field(..., description="Main weaknesses or gaps")
	final_verdict: str = Field(
		..., description="Final decision, for example: Approved or Needs Revision"
	)
