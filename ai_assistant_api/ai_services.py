import google.generativeai as genai
from django.conf import settings


genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")

def suggest_learning_path(user_skills):
    prompt = f"Given the user skills: {user_skills}, generate a learning path for Web or AI development"
    response = model.generate_content(prompt)
    return response.text

def suggest_project_ideas(topic):
    prompt = f"Given the topic: {topic}, suggest a good project idea"
    response = model.generate_content(prompt)
    return response.text


def summarize_blog(blog_content):
    prompt = f"Given the content {blog_content}, summarize the blog content highlighting important details"
    response = model.generate_content(prompt)
    return response.text

def resume_feedback(resume):
    prompt = f"Given the resume: {resume}, give feedback"
    response = model.generate_content(prompt)
    return response.text

