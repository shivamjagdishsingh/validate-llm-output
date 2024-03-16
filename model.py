from guardrails.validators import ValidRange, ValidChoices
from pydantic import BaseModel, Field
from typing import List


class Symptoms(BaseModel):
    symptom: str = Field(..., description="Symptom that a patient is experiencing")
    affected_area: str = Field(
        ...,
        description="What part of the body the symptom is affecting",
        validators=[ValidChoices(["head", "neck", "chest"], on_fail="reask")],
    )


class CurrentMeds(BaseModel):
    medication: str = Field(
        ..., description="Name of the medication the patient is taking"
    )
    response: str = Field(
        ..., description="How the patient is responding to the medication"
    )


class PatientInfo(BaseModel):
    gender: str = Field(..., description="Patient's gender")
    age: int = Field(..., description="Patient's age", validators=[ValidRange(0, 100)])
    symptoms: List[Symptoms] = Field(
        ..., description="Symptoms that the patient is experiencing"
    )
    current_meds: List[CurrentMeds] = Field(
        ..., description="Medications that the patient is currently taking"
    )


class JobDescription(BaseModel):
    title: str = Field(..., description="Title of the job position")
    company: str = Field(..., description="Name of the company offering the job")
    location: str = Field(..., description="Location of the job (city, state, country)")
    responsibilities: List[str] = Field(
        ..., description="List of responsibilities for the job"
    )
    qualifications: List[str] = Field(
        ..., description="List of qualifications required for the job"
    )
    preferred_qualifications: List[str] = Field(
        ..., description="List of preferred qualifications for the job"
    )
    additional_info: str = Field(
        ..., description="Any additional information about the job"
    )
    contact_info: str = Field(
        ..., description="Contact information for inquiries or applications"
    )
