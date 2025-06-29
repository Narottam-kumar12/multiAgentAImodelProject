# agents.py
import random
from feedback import FeedbackSystem


class Agent:
    def __init__(self, name, persona, feedback_system):
        self.name = name
        self.persona = persona
        self.feedback = feedback_system
        self.used_arguments = set()  # Track used arguments

        # Expanded argument templates specific to data security
        self.argument_templates = {
            "ethical": [
                "The ethical implications of data security include concerns about {privacy} and {breaches}.",
                "Organizations must ensure {responsibilities} in handling user data to maintain trust.",
                "We must consider the moral responsibilities of companies in protecting {data} from unauthorized access."
            ],
            "economic": [
                "Data security breaches can lead to significant {losses} for businesses, affecting their bottom line.",
                "Investing in robust data security measures can result in {benefits} for organizations and their customers.",
                "The economic impact of data breaches can include {reputation} damage and loss of customer trust."
            ],
            "social": [
                "Socially, data security is crucial for maintaining {trust} between users and organizations.",
                "The impact of data breaches on individuals raises questions about {identity} theft and privacy violations.",
                "Data security measures can help address social issues, such as {discrimination} in data handling."
            ],
            "technological": [
                "Technologically, advancements in encryption can enhance data security against {threats}.",
                "The integration of AI in data security raises concerns about {misuse} and ethical dilemmas.",
                "Current data security technologies must evolve to prevent {attacks} and protect user information."
            ],
            "regulatory": [
                "Regulatory frameworks are essential for enforcing data security standards and protecting consumers.",
                "Compliance with data protection laws can enhance {trust} and mitigate risks for organizations.",
                "The role of government in regulating data security practices is crucial for safeguarding public interests."
            ]
        }

        # Fillers for template slots
        self.template_fillers = {
            "privacy": ["user consent", "data protection", "information security"],
            "breaches": ["data leaks", "cyber attacks", "security incidents"],
            "responsibilities": ["transparency", "accountability", "ethical guidelines"],
            "data": ["personal information", "sensitive data", "customer records"],
            "losses": ["financial losses", "legal penalties", "operational disruptions"],
            "benefits": ["cost savings", "improved customer trust", "enhanced reputation"],
            "reputation": ["brand damage", "loss of clients", "negative publicity"],
            "trust": ["confidence", "credibility", "loyalty"],
            "identity": ["identity theft", "personal safety", "data misuse"],
            "discrimination": ["bias", "inequality", "unfair treatment"],
            "threats": ["hacking", "phishing", "malware"],
            "misuse": ["data exploitation", "privacy violations", "unauthorized access"],
            "attacks": ["DDoS attacks", "ransomware", "phishing attempts"]
        }

    def generate_argument(self, topic, memory, round_num):
        # Get best performing argument types based on history
        best_types = self.feedback.get_best_argument_types(self.name)

        # Generate candidate arguments
        candidates = []
        for arg_type in best_types:
            for template in self.argument_templates[arg_type]:
                # Fill template slots
                filled = template
                for slot in self.template_fillers:
                    if f"{{{slot}}}" in template:
                        filled = filled.replace(f"{{{slot}}}",
                                                random.choice(self.template_fillers[slot]))

                # Add context from previous arguments
                if memory:
                    last_arg = memory[-1]
                    if "ethical" in last_arg.lower():
                        filled += " This builds on previous ethical concerns."
                    elif "economic" in last_arg.lower():
                        filled += " The economic dimension compounds this issue."

                # Ensure the argument is unique
                if filled not in self.used_arguments:
                    candidates.append(f"{self.persona} argues that {topic} because {filled}")

        # Randomly select a candidate argument if available
        if candidates:
            selected_argument = random.choice(candidates)
            self.used_arguments.add(selected_argument)  # Track used argument
            self.feedback.record_argument(self.name, selected_argument, round_num)
            return selected_argument

        # Fallback if all candidates used
        return f"{self.persona} reiterates the importance of considering {topic} carefully."
