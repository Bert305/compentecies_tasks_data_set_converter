import pandas as pd

# Data structure with competencies and tasks, using periods to separate tasks
data = {
    "Competencies": [
        "Career & Self-Development",
        "Communication",
        "Critical Thinking",
        "Equity & Inclusion",
        "Leadership",
        "Professionalism",
        "Teamwork",
        "Technology"
    ],
    "Tasks": [
        "Show an awareness of own strengths and areas for development. Identify areas for continual growth while pursuing and applying feedback. Develop plans and goals for one’s future career. Professionally advocate for oneself and others. Display curiosity; seek out opportunities to learn. Assume duties or positions that will help one progress professionally. Establish, maintain, and/or leverage relationships with people who can help one professionally. Seek and embrace development opportunities. Voluntarily participate in further education, training, or other events to support one’s career.",
        "Understand the importance of and demonstrate verbal, written, and non-verbal/body language abilities. Employ active listening, persuasion, and influencing skills. Communicate in a clear and organized manner so that others can effectively understand. Frame communication with respect to diversity of learning styles, varied individual communication abilities, and cultural differences. Ask appropriate questions for specific information from supervisors, specialists, and others. Promptly inform relevant others when needing guidance with assigned tasks.",
        "Make decisions and solve problems using sound, inclusive reasoning and judgment. Gather and analyze information from a diverse set of sources and individuals to fully understand a problem. Proactively anticipate needs and prioritize action steps. Accurately summarize and interpret data with an awareness of personal biases that may impact outcomes. Effectively communicate actions and rationale, recognizing the diverse perspectives and lived experiences of stakeholders. Multi-task well in a fast-paced environment.",
        "Solicit and use feedback from multiple cultural perspectives to make inclusive and equity-minded decisions. Actively contribute to inclusive and equitable practices that influence individual and systemic change. Advocate for inclusion, equitable practices, justice, and empowerment for historically marginalized communities. Seek global cross-cultural interactions and experiences that enhance one’s understanding of people from different demographic groups and that leads to personal growth. Keep an open mind to diverse ideas and new ways of thinking. Identify resources and eliminate barriers resulting from individual and systemic racism, inequities, and biases. Demonstrate flexibility by adapting to diverse environments. Address systems of privilege that limit opportunities for members of historically marginalized communities.",
        "Inspire, persuade, and motivate self and others under a shared vision. Seek out and leverage diverse resources and feedback from others to inform direction. Use innovative thinking to go beyond traditional methods. Serve as a role model to others by approaching tasks with confidence and a positive attitude. Motivate and inspire others by encouraging them and by building mutual trust. Plan, initiate, manage, complete, and evaluate projects.",
        "Act equitably with integrity and accountability to self, others, and the organization. Maintain a positive personal brand in alignment with organization and personal career values. Be present and prepared. Demonstrate dependability (e.g., report consistently for work or meetings). Prioritize and complete tasks to accomplish organizational goals. Consistently meet or exceed goals and expectations. Have an attention to detail, resulting in few if any errors in their work. Show a high level of dedication toward doing a good job.",
        "Listen carefully to others, taking time to understand and ask appropriate questions without interrupting. Effectively manage conflict, interact with and respect diverse personalities, and meet ambiguity with resilience. Be accountable for individual and team responsibilities and deliverables. Employ personal strengths, knowledge, and talents to complement those of others. Exercise the ability to compromise and be agile. Collaborate with others to achieve common goals. Build strong, positive working relationships with supervisor and team members/coworkers.",
        "Navigate change and be open to learning new technologies. Use technology to improve efficiency and productivity of their work. Identify appropriate technology for completing specific tasks. Manage technology to integrate information to support relevant, effective, and timely decision-making. Quickly adapt to new or unfamiliar technologies. Manipulate information, construct ideas, and use technology to achieve strategic goals."
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to Excel
df.to_excel("NACE_Career_Readiness_Competencies_Revised_Apr_2024.xlsx", index=False)

# Print DataFrame to verify contents
print(df)
