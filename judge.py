import random
class DebateJudge:
    def __init__(self, feedback_system):
        self.feedback = feedback_system

    def evaluate(self, memory):
        # Evaluate each argument
        for i, argument in enumerate(memory):
            key = f"Agent{'A' if i % 2 == 0 else 'B'}_round_{i + 1}"
            if key in self.feedback.argument_history:
                feedback = {
                    'relevance': random.randint(5, 10),  # In real use, analyze content
                    'uniqueness': 10 - memory[:i].count(argument),
                    'impact': len(argument.split()) // 10  # Simple proxy for depth
                }
                self.feedback.evaluate_argument(key, feedback)

        # Determine winner based on average scores
        scores = {'AgentA': 0, 'AgentB': 0}
        counts = {'AgentA': 0, 'AgentB': 0}

        for key in self.feedback.argument_history:
            if 'AgentA' in key:
                scores['AgentA'] += self.feedback.argument_history[key]['score']
                counts['AgentA'] += 1
            elif 'AgentB' in key:
                scores['AgentB'] += self.feedback.argument_history[key]['score']
                counts['AgentB'] += 1

        avg_a = scores['AgentA'] / counts['AgentA'] if counts['AgentA'] else 0
        avg_b = scores['AgentB'] / counts['AgentB'] if counts['AgentB'] else 0

        winner = 'AgentA' if avg_a > avg_b else 'AgentB'
        justification = ("Presented more compelling arguments" if winner == 'AgentA'
                         else "Had stronger counterpoints overall")

        return winner, justification
