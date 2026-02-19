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
1. MSc Information Systems with Computing (Apr 2024 – Feb 2026)
   - Dublin Business School (DBS)
   - Focus: AI Ethics, Language Models, Interactive Dashboards, Quantitative Data Analysis

2. Bachelor of Technology in Information Technology (Aug 2019 – Feb 2023)
   - SVKM Institute of Technology, India
   - Focus: Data Structures, OOP (Java/Python), Software Engineering

**Work Experience:**
1. Full-Stack Software Engineer  @ Tata Communication (Oct 2022 – Sep 2025)
   -  Built TypeScript + Node.js backend with custom Dialogflow chatbot modules, improving chatbot response efficiency 
by 50%. 
   - Automated Google Sheets → Firebase data pipelines using Cloud Functions, eliminating 60% of manual data entry 
effort. 
   - Integrated Agent Assist for voice virtual agents, cutting customer response times by 15%. 

2. Software Engineer (Intern) @  Tata Elxsi  (Dec 2021 – Sep 2022)
   - Designed and implemented RESTful APIs for authentication, feedback, and issue reporting, achieving 99% uptime. 
   - Optimised middleware layer, reducing API response times by 35% under high-traffic conditions. 

3. Business Development Associate @ EduGorilla Community (Sep 2023 – May 2024)
   - Exceeded 2x monthly sales targets three times
   - Used CRM pipeline tracking

**Projects:**
1. Climate Migration Detection (Research Project)
   - Under Prof. Elisa D'Amico
   - Validating signals of climate-induced migration
   - Tech: Python, Geospatial Data (Meta/Google Mobility), NLP (GDELT/ReliefWeb), GeoPandas

2. Hindi Chatbot with Sentiment Analysis (NLP)
   - Emotion detection in Hindi text
   - Tech: Python, Django, RAG, OpenAI API, Discourse Relations algorithms

3. Intelligent Context Compression Engine for LLMs
   - Reduced LLM API costs by 60% while maintaining 92% answer quality
   - Tech: Random Forest Classifier, Semantic Compression, Scikit-learn

**Publications:**
- "Enhancing Well-Being Through Computational Emotion Analysis in Hindi Language Texts" (Springer)

**Technical Skills:**
- Languages: Python, SQL, Java
- AI/ML: NLP, RAG, Scikit-learn, Random Forest, Sentiment Analysis
- Data: Pandas, GeoPandas, Matplotlib, Seaborn
- Web: Django, REST APIs, Git
"""


def get_ai_response(user_question: str) -> str:
    """
    Get an AI-generated response to a user question about Ravi's portfolio.
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
