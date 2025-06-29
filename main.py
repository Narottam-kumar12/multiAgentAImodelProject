from user_input import UserInputNode
from memory import DebateMemory
from judge import DebateJudge
from agents import Agent
from logger import setup_logger
from feedback import FeedbackSystem
import random


def run_debate(topic):
    # Initialize systems
    logger = setup_logger()
    feedback = FeedbackSystem()
    memory_node = DebateMemory()
    judge_node = DebateJudge(feedback)

    # Create agents with feedback system
    agent_a = Agent("AgentA", "Scientist", feedback)
    agent_b = Agent("AgentB", "Philosopher", feedback)

    # Start debate
    logger.info(f"Starting debate on topic: {topic}")
    print(f"Starting debate on topic: {topic}")

    for round_num in range(1, 9):
        if round_num % 2 != 0:  # Agent A's turn
            argument = agent_a.generate_argument(topic, memory_node.transcript, round_num)
        else:  # Agent B's turn
            argument = agent_b.generate_argument(topic, memory_node.transcript, round_num)

        memory_node.update_memory(argument)
        logger.info(f"[Round {round_num}] {argument}")
        print(f"[Round {round_num}] {argument}")

    # Judge the debate
    winner, justification = judge_node.evaluate(memory_node.transcript)
    logger.info(f"[Judge] Winner: {winner} Reason: {justification}")
    print(f"[Judge] Winner: {winner} Reason: {justification}")


if __name__ == "__main__":
    topic = input("Enter topic for debate: ")
    run_debate(topic)
