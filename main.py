import json

import cohere
import guardrails as gd

from model import PatientInfo, JobDescription

COHERE_KEY = "Bd9g92JtxnixtQM5JHilOmlXkwmWccrfKG7zzWKH"


# Example1
doctor_prescription = """49 y/o Male with chronic macular rash to face & hair, worse in beard, eyebrows & nares.
Itchy, flaky, slightly scaly. Moderate response to OTC steroid cream"""
guard = gd.Guard.from_pydantic(PatientInfo, prompt=doctor_prescription)

# Example2
# prompt = "Python developer, 4 years of experience, Pune"
# guard = gd.Guard.from_pydantic(JobDescription, prompt=prompt)

co = cohere.Client(api_key=COHERE_KEY)
res = guard(
    co.generate,
    prompt_params={"doctor_prescription": doctor_prescription},
    model='command',
    max_tokens=1024,
    temperature=0.6
)

print(json.dumps(res.validated_output, indent=2))

# output1
# {
#   "gender": "null",
#   "age": 30,
#   "symptoms": [
#     {
#       "symptom": "red, itchy, and flaky rash on face",
#       "affected_area": "head"
#     }
#   ],
#   "current_meds": [
#     {
#       "medication": "steroid creams",
#       "response": "provides some relief"
#     }
#   ]
# }


# output2
# {
#   "title": "Python Developer",
#   "company": "Cohere",
#   "location": "Pune, India",
#   "responsibilities": [
#     "Write efficient, scalable, and maintainable code to meet project requirements",
#     "Collaborate with developers, designers, and project managers to ensure the right balance between business, user needs, and technical constraints",
#     "Participate in code reviews and provide constructive feedback to peers"
#   ],
#   "qualifications": [
#     "Strong understanding of object-oriented programming and Python syntax",
#     "Familiarity with testing frameworks like unittest",
#     "Web development experience with Flask or Django"
#   ],
#   "preferred_qualifications": [
#     "Experience with SQL or NoSQL databases",
#     "Knowledge of data structures and algorithms",
#     "Prior experience with AI, machine learning, or natural language processing"
#   ],
#   "additional_info": "This position offers a flexible work environment and opportunities for skill enhancement.",
#   "contact_info": "cohere.com/jobs"
# }
