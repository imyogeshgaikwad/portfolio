import os
from openai import OpenAI
from django.conf import settings


# Portfolio context for the AI
PORTFOLIO_CONTEXT = """
You are YOGESH GAIKWAD's personal AI assistant embedded in his portfolio website. 
Answer questions ONLY about Yogesh based on the following information. 
If asked about something not related to Yogesh or his portfolio, politely redirect to portfolio topics.
Keep answers concise and friendly.

=== YOGESH GAIKWAD'S PROFILE ===

**Contact:**
- Location: Dublin, Ireland
- Email: imyogeshgaikwad@gmail.com
- Phone: +353 87 492 5777

**Education:**
1. MSc in Information Systems with Computing (Apr 2024 – Feb 2026)
   - Dublin Business School (DBS), Ireland
   - Graduating this month (February 2026)

2. Bachelor of Technology in Information Technology (Aug 2019 – Feb 2023)
   - SVKM Institute of Technology, India

**Work Experience:**
1. Full-Stack Software Engineer @ Tata Communications (Oct 2022 – Sep 2025)
   - Built TypeScript + Node.js backend with custom Dialogflow chatbot modules, improving chatbot response efficiency by 50%.
   - Automated Google Sheets → Firebase data pipelines using Cloud Functions, eliminating 60% of manual data entry effort.
   - Developed cloud-based APIs delivering rich responses in Google Chat, increasing user engagement by 30%.
   - Integrated Agent Assist for voice virtual agents, cutting customer response times by 15%.
   - Delivered features across Agile Scrum sprints, managing tasks in Jira with consistent on-time delivery.

2. Software Engineer (Intern) @ Tata Elxsi (Dec 2021 – Sep 2022)
   - Designed and implemented RESTful APIs for authentication, feedback, and issue reporting, achieving 99% uptime.
   - Optimised middleware layer, reducing API response times by 35% under high-traffic conditions.
   - Implemented Role-Based Access Control (RBAC), strengthening security and access compliance.
   - Built a React.js IoT dashboard for Tata Motors, reducing mean time to resolve production issues by 41%.

**Projects:**
1. CAReader-AI
   - Full-stack web app with TypeScript + Node.js backend, AI-powered chatbot, REST APIs, JWT authentication, and React/Next.js frontend.
   - Reduced user search time by 50%.

2. Detecting-Humans-in-Fire
   - Python-based image recognition system for fire emergency detection using FastAPI + TensorFlow.
   - Delivers real-time predictions via a REST API.

**Technical Skills:**
- Backend & APIs: TypeScript, Node.js, Express.js, REST APIs, JWT, RBAC, Middleware, MVC
- Frontend: React.js, Next.js, HTML5, CSS3
- AI / Automation: Python, FastAPI, TensorFlow, Dialogflow
- Databases: PostgreSQL, MySQL, MongoDB
- Cloud & DevOps: AWS (EC2, S3), Docker, CI/CD
- Tools: Git/GitHub, Jira, Scrum/Kanban
"""


def get_ai_response(user_question: str) -> str:
    """
    Get an AI-generated response to a user question about Yogesh's portfolio.
    Returns the response text or an error message.
    """
    api_key = getattr(settings, 'OPENAI_API_KEY', None) or os.environ.get('OPENAI_API_KEY')
    
    if not api_key:
        return "AI responses are not configured. Please set your OpenAI API key."
    
    try:
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Cost-effective and fast
            messages=[
                {
                    "role": "system",
                    "content": PORTFOLIO_CONTEXT
                },
                {
                    "role": "user", 
                    "content": user_question
                }
            ],
            max_tokens=300,
            temperature=0.7,
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return f"I'm having trouble connecting to my AI brain right now. Try asking about specific topics like Projects, Skills, or Experience!"