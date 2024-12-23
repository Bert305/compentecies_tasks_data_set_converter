import pandas as pd

# Define the data
data = {
    "Competencies": [
        "Communication", "Teamwork", "Problem-Solving", "Oral/Written Communication",
        "Leadership & Responsibility", "Professionalism/Work Ethic", "Career Management",
        "Global/Intercultural Fluency", "Digital Technology", "Critical Thinking/Problem Solving",
        "Analytical Thinking", "Curiosity", "Motivation", "Self-Management"
    ],
    "Tasks": [
        "Guest Speaker events, Job Shadowing, Mentoring, Internships, Workplace Tours",
        "Workplace Challenges/Student Projects, Team-based assignments",
        "Solving real-life industry problems through projects, Participating in work-based challenges",
        "Participation in Guest Speaker Series, Writing assignments (Cover Letters, Resumes)",
        "Leadership roles in projects, Mentoring younger students",
        "Professional Portfolio & Job Preparation, Professional conduct in workplace settings",
        "Career path identification, Development of an Individual Career Plan",
        "Exposure to multicultural environments, Global industry webinars",
        "Using digital tools and platforms (e.g., IBM Open P-TECH), e-learning sessions",
        "Analytical problem-solving in team projects, Critical analysis in project evaluations",
        "Analyzing labor market trends, Industry-specific case studies",
        "Research projects (e.g., Dream job research project), Explorative assignments",
        "Setting and achieving personal academic and career goals",
        "Managing personal project timelines, Self-assessment activities"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("data_into_spreadsheet/competencies_and_tasks.xlsx", index=False)

# Print confirmation
print("The spreadsheet has been saved as 'competencies_and_tasks.xlsx'.")


