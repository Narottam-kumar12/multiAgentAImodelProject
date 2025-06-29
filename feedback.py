import random
class FeedbackSystem:
    def __init__(self):
        self.argument_history = {}
        self.performance_scores = {}

    def record_argument(self, agent_name, argument, round_num):
        key = f"{agent_name}_round_{round_num}"
        self.argument_history[key] = {
            'argument': argument,
            'score': 0,
            'used': False
        }

    def evaluate_argument(self, argument_key, judge_feedback):
        # Score based on judge's feedback (1-10 scale)
        relevance = judge_feedback.get('relevance', 5)
        uniqueness = judge_feedback.get('uniqueness', 5)
        impact = judge_feedback.get('impact', 5)

        score = (relevance * 0.4) + (uniqueness * 0.3) + (impact * 0.3)
        self.argument_history[argument_key]['score'] = score
        self.argument_history[argument_key]['used'] = True

        # Update performance scores for argument types
        argument_type = self._classify_argument(argument_key)
        if argument_type not in self.performance_scores:
            self.performance_scores[argument_type] = []
        self.performance_scores[argument_type].append(score)

    def _classify_argument(self, argument_key):
        argument = self.argument_history[argument_key]['argument']
        if "ethical" in argument.lower():
            return "ethical"
        elif "economic" in argument.lower():
            return "economic"
        elif "social" in argument.lower():
            return "social"
        elif "technological" in argument.lower():
            return "technological"
        return "other"

    def get_best_argument_types(self, agent_name, n=2):
        agent_args = {k: v for k, v in self.performance_scores.items()
                      if any(k in key for key in self.argument_history.keys()
                             if agent_name in key)}

        if not agent_args:
            return random.sample(["ethical", "economic", "social", "technological"], n)

        avg_scores = {k: sum(v) / len(v) for k, v in agent_args.items()}
        return sorted(avg_scores.keys(), key=lambda x: avg_scores[x], reverse=True)[:n]
