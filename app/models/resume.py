from typing import List, Optional, Dict
from pydantic import BaseModel, Field


class Contact(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    github: Optional[str] = None
    telegram: Optional[str] = None
    website: Optional[str] = None


class Job(BaseModel):
    title: str
    company: Optional[str] = None
    period: Optional[str] = None
    location: Optional[str] = None
    company_link: Optional[str] = None
    description: Optional[str] = None
    achievements: List[str] = Field(default_factory=list)


class Project(BaseModel):
    title: str
    period: Optional[str] = None
    description: Optional[str] = None
    achievements: List[str] = Field(default_factory=list)
    technologies: List[str] = Field(default_factory=list)
    github_link: Optional[str] = None
    demo_link: Optional[str] = None
    docs_link: Optional[str] = None


class Education(BaseModel):
    degree: str
    institution: Optional[str] = None
    period: Optional[str] = None
    certificate_link: Optional[str] = None
    description: Optional[str] = None


class Resume(BaseModel):
    name: str
    role: Optional[str] = None
    summary: Optional[str] = None
    avatar: Optional[str] = None
    contacts: Contact = Field(default_factory=Contact)
    experience: List[Job] = Field(default_factory=list)
    projects: List[Project] = Field(default_factory=list)
    education: List[Education] = Field(default_factory=list)
    skills: Dict[str, List[str]] = Field(default_factory=dict)
    achievements: List[str] = Field(default_factory=list)
    languages: List[str] = Field(default_factory=list)

    class Config:
        extra = 'ignore'


__all__ = [
    "Contact",
    "Job",
    "Project",
    "Education",
    "Resume",
]
