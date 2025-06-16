import asyncio
from pydantic import BaseModel
from agents import Agent, Runner, trace

# Agent 1: Generate a quiz question from user topic
question_agent = Agent(
    name="question_agent",
    instructions="Generate a single quiz question about the topic provided by the user."
)

# Output model for Agent 2
class QuestionCheckOutput(BaseModel):
    is_math: bool
    is_logical: bool

# Agent 2: Check if question is math and logical
check_agent = Agent(
    name="check_agent",
    instructions="Given a question, check if it is a math question, and if it is logically correct.",
    output_type=QuestionCheckOutput,
)

# Agent 3: Answer the math question
answer_agent = Agent(
    name="answer_agent",
    instructions="Given a math question, provide a concise answer.",
    output_type=str,
)

async def main():
    user_topic = input("Which topic should I make a quiz question about? ")

    with trace("Quiz Generation Flow"):
        # 1. Generate a quiz question
        question_result = await Runner.run(question_agent, user_topic)
        print(f"\nQuiz Question: {question_result.final_output}")

        # 2. Check the question
        check_result = await Runner.run(check_agent, question_result.final_output)
        assert isinstance(check_result.final_output, QuestionCheckOutput)

        # 3. Conditional gate
        if not check_result.final_output.is_math:
            print("The question is not a math question, so we stop here.")
            return
        if not check_result.final_output.is_logical:
            print("The question is not logical, so we stop here.")
            return

        print("The question is a logical math question. Proceeding to answer...")

        # 4. Answer the math question
        answer_result = await Runner.run(answer_agent, question_result.final_output)
        print(f"\nAnswer: {answer_result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
