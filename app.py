from flask import Flask, render_template, jsonify, request, redirect, url_for
import difflib

app = Flask(__name__)

CAREERS = {
    "uiux": {
        "id": "uiux",
        "title": "UI/UX Design",
        "icon": "🎨",
        "tagline": "Architect human-centric digital experiences",
        "growth": 28,
        "color": "#ff6b9d",
        "description": "UI/UX Designers shape how users interact with software. Across India's booming startup ecosystem, product-led growth has made UX a critical differentiator, driving massive demand for designers who can balance aesthetics with logic.",
        "salary": "₹8L – ₹24L",
        "yoy_growth": "28%",
        "career_paths": "4+",
        "sub_roles": ["Product Designer", "UX Researcher", "Interaction Designer", "UX Writer"],
        "top_skills": ["Figma", "User Research", "Prototyping", "Design Systems"],
        "job_roles": [
            {
                "title": "Product Designer",
                "desc": "Lead end-to-end design for web and mobile products.",
                "salary": "₹12L - ₹25L",
                "skills": ["Figma", "Design Systems", "Product Strategy"],
                "locations": ["Bengaluru", "Mumbai"],
                "trend": [20, 35, 50, 65, 80, 100],
                "interview_tips": [{"type": "Portfolio", "advice": "Focus on the 'Why' behind design decisions."}]
            },
            {
                "title": "UX Researcher",
                "desc": "Analyze user behavior to inform product strategy.",
                "salary": "₹10L - ₹18L",
                "skills": ["User Interviews", "Usability Testing", "Data Analysis"],
                "locations": ["Hyderabad", "Bengaluru"],
                "trend": [15, 25, 40, 55, 75, 90],
                "interview_tips": [{"type": "Case Study", "advice": "Showcase research impact on a product feature."}]
            },
            {
                "title": "Interaction Designer",
                "desc": "Focus on animations and complex user flows.",
                "salary": "₹9L - ₹16L",
                "skills": ["After Effects", "Principle", "Micro-interactions"],
                "locations": ["Pune", "Gurgaon"],
                "trend": [10, 20, 35, 50, 70, 85],
                "interview_tips": [{"type": "Portfolio", "advice": "Present interactive prototypes, not just static screens."}]
            },
            {
                "title": "UI Developer",
                "desc": "Bridge the gap between design and frontend code.",
                "salary": "₹10L - ₹20L",
                "skills": ["HTML5/CSS3", "JavaScript", "React.js"],
                "locations": ["Chennai", "Bengaluru"],
                "trend": [30, 45, 60, 75, 90, 100],
                "interview_tips": [{"type": "Coding", "advice": "Expect to build a complex UI component from scratch."}]
            },
            {
                "title": "UX Writer",
                "desc": "Craft the copy that guides users through interfaces.",
                "salary": "₹7L - ₹14L",
                "skills": ["Copywriting", "Content Strategy", "Information Architecture"],
                "locations": ["Remote", "Mumbai"],
                "trend": [5, 15, 25, 40, 60, 80],
                "interview_tips": [{"type": "Exercise", "advice": "Rewrite technical error messages into human-readable text."}]
            }
        ],
        "market_data": [38, 45, 55, 65, 78, 92, 100],
        "quote": "Design is a craft where portfolio trumps degree.",
        "academic_paths": [{"title": "BDes / BFA", "duration": "4 years", "recommended": True}],
        "certifications": [{"name": "Google UX Design", "provider": "Google", "level": "BEGINNER"}],
        "platforms": [{"name": "Figma Learn", "desc": "Official tutorials.", "url": "#"}],
        "jobs": [{"company": "Razorpay", "title": "Senior Designer", "salary": "₹18L - ₹24L"}],
        "youtube_query": "UI UX Design Career Roadmap India"
    },
    "servicenow": {
        "id": "servicenow",
        "title": "ServiceNow",
        "icon": "⚙️",
        "tagline": "Automate enterprise workflows at scale",
        "growth": 35,
        "color": "#00d4aa",
        "description": "ServiceNow professionals implement enterprise service management. India is the global delivery hub for this platform.",
        "salary": "₹10L – ₹35L",
        "yoy_growth": "35%",
        "career_paths": "5+",
        "sub_roles": ["Developer", "Admin", "ITSM Consultant"],
        "job_roles": [
            {
                "title": "ServiceNow Developer",
                "desc": "Write scripts and build apps on the Now platform.",
                "salary": "₹10L - ₹22L",
                "skills": ["JavaScript", "GlideRecord", "ITIL"],
                "locations": ["Bengaluru", "Pune"],
                "trend": [40, 55, 70, 85, 95, 100],
                "interview_tips": [{"type": "Technical", "advice": "Master Client Scripts vs Business Rules."}]
            },
            {
                "title": "Platform Architect",
                "desc": "Design large-scale enterprise ServiceNow solutions.",
                "salary": "₹25L - ₹45L",
                "skills": ["Domain Separation", "System Integration", "Performance Tuning"],
                "locations": ["Hyderabad", "Mumbai"],
                "trend": [20, 35, 55, 75, 90, 100],
                "interview_tips": [{"type": "Architecture", "advice": "Explain instance synchronization in a global setup."}]
            },
            {
                "title": "ITSM Consultant",
                "desc": "Optimize IT service management workflows.",
                "salary": "₹15L - ₹28L",
                "skills": ["ITIL", "Process Mapping", "CMDB"],
                "locations": ["Gurgaon", "Chennai"],
                "trend": [30, 40, 50, 65, 80, 95],
                "interview_tips": [{"type": "Process", "advice": "Walk through an incident lifecycle."}]
            },
            {
                "title": "ServiceNow Admin",
                "desc": "Manage instances, users, and daily operations.",
                "salary": "₹6L - ₹12L",
                "skills": ["Instance Config", "Data Management", "Process Automation"],
                "locations": ["Kolkata", "Noida"],
                "trend": [25, 35, 45, 60, 75, 90],
                "interview_tips": [{"type": "System", "advice": "Difference between UI Policies and Data Policies."}]
            },
            {
                "title": "GRC Specialist",
                "desc": "Implement Governance, Risk, and Compliance apps.",
                "salary": "₹18L - ₹30L",
                "skills": ["Risk Frameworks", "Policy Management", "Audit Prep"],
                "locations": ["Bengaluru", "Hyderabad"],
                "trend": [10, 25, 45, 65, 85, 100],
                "interview_tips": [{"type": "Compliance", "advice": "Difference between Control and Risk Statement."}]
            }
        ],
        "market_data": [30, 40, 52, 65, 80, 95, 100],
        "quote": "One solid ServiceNow certification can double your salary.",
        "academic_paths": [{"title": "BTech CSE", "duration": "4 years", "recommended": True}],
        "certifications": [{"name": "Certified System Admin", "provider": "ServiceNow", "level": "BEGINNER"}],
        "platforms": [{"name": "Now Learning", "desc": "Official training.", "url": "#"}],
        "jobs": [{"company": "Infosys", "title": "ServiceNow Dev", "salary": "₹12L - ₹20L"}],
        "youtube_query": "ServiceNow Developer Roadmap India"
    },
    "salesforce": {
        "id": "salesforce",
        "title": "Salesforce",
        "icon": "☁️",
        "tagline": "Drive customer relationship transformations",
        "growth": 25,
        "color": "#00a1e0",
        "description": "Salesforce professionals help businesses manage customer relationships. India has the second-largest Salesforce talent pool globally.",
        "salary": "₹9L – ₹30L",
        "yoy_growth": "25%",
        "career_paths": "6+",
        "sub_roles": ["Admin", "Developer", "Consultant"],
        "job_roles": [
            {
                "title": "Salesforce Developer",
                "desc": "Build custom apps using Apex and LWC.",
                "salary": "₹12L - ₹24L",
                "skills": ["Apex", "LWC", "SOQL"],
                "locations": ["Hyderabad", "Bengaluru"],
                "trend": [30, 45, 60, 75, 90, 100],
                "interview_tips": [{"type": "Coding", "advice": "Practice bulkified Apex triggers."}]
            },
            {
                "title": "Salesforce Admin",
                "desc": "Manage users, profiles, and core platform configuration.",
                "salary": "₹6L - ₹12L",
                "skills": ["Profiles", "Permission Sets", "Flows"],
                "locations": ["Noida", "Pune"],
                "trend": [20, 35, 45, 60, 75, 85],
                "interview_tips": [{"type": "Automation", "advice": "When to use Flow vs. Validation Rule."}]
            },
            {
                "title": "Salesforce Consultant",
                "desc": "Translate business needs into Salesforce solutions.",
                "salary": "₹15L - ₹28L",
                "skills": ["Business Analysis", "Solution Design", "Stakeholder Management"],
                "locations": ["Gurgaon", "Mumbai"],
                "trend": [15, 25, 40, 55, 75, 95],
                "interview_tips": [{"type": "Scenario", "advice": "How to handle conflicting client requirements."}]
            },
            {
                "title": "Marketing Cloud Specialist",
                "desc": "Automate customer journeys and marketing campaigns.",
                "salary": "₹10L - ₹20L",
                "skills": ["Journey Builder", "Email Studio", "AMPscript"],
                "locations": ["Remote", "Bengaluru"],
                "trend": [10, 20, 35, 55, 80, 100],
                "interview_tips": [{"type": "Platform", "advice": "Explain the different Marketing Cloud studios."}]
            },
            {
                "title": "Salesforce Architect",
                "desc": "Design global scale enterprise CRM architectures.",
                "salary": "₹30L - ₹55L",
                "skills": ["System Design", "Integration", "Security"],
                "locations": ["Hyderabad", "Bengaluru"],
                "trend": [10, 25, 45, 65, 85, 100],
                "interview_tips": [{"type": "Architecture", "advice": "Design a multi-org Salesforce strategy."}]
            }
        ],
        "market_data": [35, 45, 55, 62, 75, 88, 100],
        "quote": "Salesforce Architects in India earn global-tier packages.",
        "academic_paths": [{"title": "BTech / MCA", "duration": "3-4 years", "recommended": True}],
        "certifications": [{"name": "Platform Developer I", "provider": "Salesforce", "level": "INTERMEDIATE"}],
        "platforms": [{"name": "Trailhead", "desc": "Best free learning.", "url": "#"}],
        "jobs": [{"company": "Deloitte", "title": "Salesforce Dev", "salary": "₹14L - ₹22L"}],
        "youtube_query": "Salesforce Developer Roadmap India"
    },
    "product": {
        "id": "product",
        "title": "Product Management",
        "icon": "🚀",
        "tagline": "Lead the vision from ideation to launch",
        "growth": 40,
        "color": "#9b59b6",
        "description": "PMs are the CEOs of their products. High demand in Bengaluru and Gurgaon for tech-savvy business leaders.",
        "salary": "₹15L – ₹50L",
        "yoy_growth": "40%",
        "career_paths": "3+",
        "sub_roles": ["APM", "Product Manager", "Growth PM"],
        "job_roles": [
            {
                "title": "Associate Product Manager",
                "desc": "Support product discovery and feature execution.",
                "salary": "₹15L - ₹25L",
                "skills": ["SQL", "Analytics", "Wireframing"],
                "locations": ["Bengaluru", "Gurgaon"],
                "trend": [40, 55, 70, 85, 95, 100],
                "interview_tips": [{"type": "Product Sense", "advice": "Practice RICE prioritization."}]
            },
            {
                "title": "Growth Product Manager",
                "desc": "Focus on acquisition, activation, and retention metrics.",
                "salary": "₹20L - ₹35L",
                "skills": ["A/B Testing", "Funnel Optimization", "User Psychology"],
                "locations": ["Mumbai", "Bengaluru"],
                "trend": [20, 35, 50, 68, 85, 100],
                "interview_tips": [{"type": "Case Study", "advice": "Propose a growth strategy for a given product."}]
            },
            {
                "title": "Technical Product Manager",
                "desc": "Bridge complex engineering infra with business value.",
                "salary": "₹22L - ₹40L",
                "skills": ["System Design", "API Design", "Agile Methodologies"],
                "locations": ["Hyderabad", "Bengaluru"],
                "trend": [25, 38, 55, 72, 88, 100],
                "interview_tips": [{"type": "Technical", "advice": "Explain how an API gateway works."}]
            },
            {
                "title": "Product Analyst",
                "desc": "Dive into user data to find actionable product insights.",
                "salary": "₹10L - ₹18L",
                "skills": ["SQL", "Tableau", "User Behavior Analysis"],
                "locations": ["Pune", "Remote"],
                "trend": [30, 45, 60, 75, 90, 100],
                "interview_tips": [{"type": "Data", "advice": "Analyze a dataset and present key findings."}]
            },
            {
                "title": "UX Product Manager",
                "desc": "Lead initiatives focused purely on user experience quality.",
                "salary": "₹18L - ₹30L",
                "skills": ["User Research", "Prototyping", "Information Architecture"],
                "locations": ["Bengaluru", "Delhi"],
                "trend": [15, 25, 40, 60, 80, 95],
                "interview_tips": [{"type": "Product Sense", "advice": "Critique the UX of a popular app."}]
            }
        ],
        "market_data": [28, 38, 50, 65, 82, 95, 100],
        "quote": "PMs synthesize data and empathy into decisions.",
        "academic_paths": [{"title": "BTech + MBA", "duration": "6 years", "recommended": True}],
        "certifications": [{"name": "Product Mgmt Cert", "provider": "PM School", "level": "BEGINNER"}],
        "platforms": [{"name": "Reforge", "desc": "Advanced PM growth.", "url": "#"}],
        "jobs": [{"company": "Zomato", "title": "Product Manager", "salary": "₹35L - ₹60L"}],
        "youtube_query": "Product Management Roadmap India"
    },
    "devops": {
        "id": "devops",
        "title": "DevOps/Cloud",
        "icon": "⚡",
        "tagline": "Build resilient, scalable infrastructure",
        "growth": 32,
        "color": "#f39c12",
        "description": "DevOps engineers manage the backbone of tech companies. High demand for AWS/Azure/K8s skills.",
        "salary": "₹12L – ₹45L",
        "yoy_growth": "32%",
        "career_paths": "5+",
        "sub_roles": ["DevOps Engineer", "SRE", "Cloud Architect"],
        "job_roles": [
            {
                "title": "DevOps Engineer",
                "desc": "Automate deployments and CI/CD pipelines.",
                "salary": "₹12L - ₹25L",
                "skills": ["Docker", "Kubernetes", "Terraform"],
                "locations": ["Bengaluru", "Pune"],
                "trend": [40, 55, 75, 90, 100, 100],
                "interview_tips": [{"type": "Architecture", "advice": "Draw a full CI/CD pipeline."}]
            },
            {
                "title": "Cloud Architect",
                "desc": "Design scalable cloud infrastructure on AWS/Azure.",
                "salary": "₹30L - ₹55L",
                "skills": ["AWS/Azure", "System Design", "Cost Optimization"],
                "locations": ["Hyderabad", "Gurgaon"],
                "trend": [20, 35, 55, 75, 92, 100],
                "interview_tips": [{"type": "Design", "advice": "Whiteboard a scalable system under high-load."}]
            },
            {
                "title": "Site Reliability Engineer",
                "desc": "Ensure high availability and system performance.",
                "salary": "₹18L - ₹35L",
                "skills": ["Monitoring", "Automation", "Distributed Systems"],
                "locations": ["Bengaluru", "Mumbai"],
                "trend": [25, 40, 60, 80, 95, 100],
                "interview_tips": [{"type": "Scenario", "advice": "Handle a massive spike in 5xx errors."}]
            },
            {
                "title": "Cloud Security Engineer",
                "desc": "Secure cloud environments and data compliance.",
                "salary": "₹15L - ₹30L",
                "skills": ["Zero Trust", "Encryption", "DevSecOps"],
                "locations": ["Chennai", "Pune"],
                "trend": [15, 30, 50, 70, 90, 100],
                "interview_tips": [{"type": "Threats", "advice": "Explain a recent cloud breach and prevention."}]
            },
            {
                "title": "Platform Engineer",
                "desc": "Build internal developer platforms and tooling.",
                "salary": "₹20L - ₹38L",
                "skills": ["IDP Frameworks", "Self-Service", "Developer Experience"],
                "locations": ["Bengaluru", "Remote"],
                "trend": [10, 20, 45, 65, 85, 100],
                "interview_tips": [{"type": "Strategy", "advice": "Platform Engineering vs. traditional DevOps."}]
            }
        ],
        "market_data": [32, 42, 55, 68, 82, 94, 100],
        "quote": "Cloud skills are recession-proof.",
        "academic_paths": [{"title": "BTech CSE", "duration": "4 years", "recommended": True}],
        "certifications": [{"name": "AWS Solutions Architect", "provider": "AWS", "level": "INTERMEDIATE"}],
        "platforms": [{"name": "KodeKloud", "desc": "Hands-on labs.", "url": "#"}],
        "jobs": [{"company": "Amazon", "title": "Cloud Architect", "salary": "₹35L - ₹55L"}],
        "youtube_query": "DevOps Roadmap India 2026"
    },
    "datascience": {
        "id": "datascience",
        "title": "Data Science",
        "icon": "🧠",
        "tagline": "Extract intelligence from raw data",
        "growth": 45,
        "color": "#e91e63",
        "description": "Data Scientists use ML to predict insights. GenAI has supercharged demand in India's top hubs.",
        "salary": "₹10L – ₹50L",
        "yoy_growth": "45%",
        "career_paths": "6+",
        "sub_roles": ["Data Analyst", "Data Scientist", "ML Engineer"],
        "job_roles": [
            {
                "title": "Data Scientist",
                "desc": "Apply ML models to solve business problems.",
                "salary": "₹12L - ₹30L",
                "skills": ["Python", "Statistics", "MLOps"],
                "locations": ["Bengaluru", "Hyderabad"],
                "trend": [30, 40, 58, 70, 85, 100],
                "interview_tips": [{"type": "Theory", "advice": "Understand the Bias-Variance tradeoff."}]
            },
            {
                "title": "Data Analyst",
                "desc": "Analyze company data and create dashboards.",
                "salary": "₹6L - ₹12L",
                "skills": ["SQL", "Excel", "Tableau"],
                "locations": ["Bangalore", "Hyderabad", "Pune"],
                "trend": [35, 45, 55, 65, 75, 90],
                "interview_tips": [{"type": "Technical", "advice": "Expect live SQL coding tests."}]
            },
            {
                "title": "ML Engineer",
                "desc": "Deploy machine learning models.",
                "salary": "₹12L - ₹30L",
                "skills": ["Python", "TensorFlow/PyTorch", "Deployment"],
                "locations": ["Hyderabad", "Bangalore"],
                "trend": [28, 42, 55, 72, 88, 100],
                "interview_tips": [{"type": "System Design", "advice": "Design an ML model serving infrastructure."}]
            },
            {
                "title": "BI Analyst",
                "desc": "Business dashboards and reporting.",
                "salary": "₹7L - ₹14L",
                "skills": ["Power BI", "SQL", "Data Warehousing"],
                "locations": ["Pune", "Chennai"],
                "trend": [25, 35, 48, 62, 75, 90],
                "interview_tips": [{"type": "Visualization", "advice": "Create a dashboard to track sales performance."}]
            },
            {
                "title": "AI Engineer",
                "desc": "Build AI apps and automation tools.",
                "salary": "₹15L - ₹35L",
                "skills": ["Python", "NLP", "Computer Vision"],
                "locations": ["Bangalore", "Mumbai"],
                "trend": [20, 38, 55, 75, 92, 100],
                "interview_tips": [{"type": "Project", "advice": "Discuss a recent AI project you worked on."}]
            }
        ],
        "market_data": [25, 38, 52, 68, 85, 96, 100],
        "quote": "Master the data cleaning; that's 80% of the job.",
        "academic_paths": [{"title": "BTech / MSc Stats", "duration": "4 years", "recommended": True}],
        "certifications": [{"name": "IBM Data Science", "provider": "IBM", "level": "BEGINNER"}],
        "platforms": [{"name": "Kaggle", "desc": "Competitions and data.", "url": "#"}],
        "jobs": [{"company": "Microsoft", "title": "ML Engineer", "salary": "₹30L - ₹50L"}],
        "youtube_query": "Data Science Roadmap India"
    },
    "cybersecurity": {
        "id": "cybersecurity",
        "title": "Cybersecurity",
        "icon": "🛡️",
        "tagline": "Defend digital assets from threats",
        "growth": 38,
        "color": "#00bcd4",
        "description": "Professionals protect India's infrastructure. Ethical hacking is in high demand.",
        "salary": "₹8L – ₹40L",
        "yoy_growth": "38%",
        "career_paths": "5+",
        "sub_roles": ["Ethical Hacker", "SOC Analyst", "Security Engineer"],
        "job_roles": [
            {
                "title": "Ethical Hacker",
                "desc": "Conduct pentests to find vulnerabilities.",
                "salary": "₹12L - ₹28L",
                "skills": ["Linux", "Burp Suite", "Networking"],
                "locations": ["Mumbai", "Bengaluru"],
                "trend": [30, 45, 65, 85, 100, 100],
                "interview_tips": [{"type": "Technical", "advice": "Explain a recent SQLi exploit."}]
            },
            {
                "title": "SOC Analyst",
                "desc": "Monitor networks for real-time security threats.",
                "salary": "₹6L - ₹12L",
                "skills": ["SIEM", "Incident Response", "Threat Detection"],
                "locations": ["Chennai", "Hyderabad"],
                "trend": [40, 55, 70, 85, 95, 100],
                "interview_tips": [{"type": "Scenario", "advice": "Respond to a phishing attack alert."}]
            },
            {
                "title": "Application Security Engineer",
                "desc": "Ensure secure code throughout the SDLC.",
                "salary": "₹15L - ₹30L",
                "skills": ["SAST/DAST", "Secure Coding", "Cloud Security"],
                "locations": ["Pune", "Gurgaon"],
                "trend": [20, 35, 55, 75, 90, 100],
                "interview_tips": [{"type": "Code Review", "advice": "Identify vulnerabilities in a given code snippet."}]
            },
            {
                "title": "Incident Responder",
                "desc": "Manage and mitigate the impact of active breaches.",
                "salary": "₹14L - ₹25L",
                "skills": ["Forensics", "Malware Analysis", "Crisis Management"],
                "locations": ["Mumbai", "Delhi"],
                "trend": [15, 30, 50, 70, 90, 100],
                "interview_tips": [{"type": "Scenario", "advice": "Outline steps for a major data breach."}]
            },
            {
                "title": "Compliance Officer (GRC)",
                "desc": "Manage DPDP Act and regulatory audit standards.",
                "salary": "₹10L - ₹22L",
                "skills": ["ISO 27001", "DPDP Act", "Risk Assessment"],
                "locations": ["Bengaluru", "Remote"],
                "trend": [10, 25, 45, 65, 85, 100],
                "interview_tips": [{"type": "Regulations", "advice": "Explain GDPR vs. DPDP Act."}]
            }
        ],
        "market_data": [28, 38, 50, 64, 80, 93, 100],
        "quote": "Security is not a product, it's a process.",
        "academic_paths": [{"title": "BTech CSE", "duration": "4 years", "recommended": True}],
        "certifications": [{"name": "OSCP", "provider": "OffSec", "level": "ADVANCED"}],
        "platforms": [{"name": "TryHackMe", "desc": "Gamified learning.", "url": "#"}],
        "jobs": [{"company": "Razorpay", "title": "Security Analyst", "salary": "₹18L - ₹30L"}],
        "youtube_query": "Cybersecurity Roadmap India"
    },
    "fullstack": {
        "id": "fullstack",
        "title": "Full-Stack Dev",
        "icon": "💻",
        "tagline": "Engineer end-to-end web applications",
        "growth": 22,
        "color": "#4caf50",
        "description": "Full-Stack devs build from DB to UI. MERN stack is the dominant requirement.",
        "salary": "₹7L – ₹35L",
        "yoy_growth": "22%",
        "career_paths": "4+",
        "sub_roles": ["Frontend Dev", "Backend Dev", "Tech Lead"],
        "job_roles": [
            {
                "title": "Full-Stack Engineer",
                "desc": "Master of both client and server-side logic.",
                "salary": "₹12L - ₹30L",
                "skills": ["React", "Node.js", "MongoDB"],
                "locations": ["Bengaluru", "Mumbai"],
                "trend": [45, 60, 75, 90, 100, 100],
                "interview_tips": [{"type": "Performance", "advice": "Discuss Core Web Vitals optimization."}]
            },
            {
                "title": "Backend Developer (Node/Go)",
                "desc": "Architect APIs and robust server architectures.",
                "salary": "₹10L - ₹25L",
                "skills": ["Node.js", "Go", "Microservices"],
                "locations": ["Hyderabad", "Pune"],
                "trend": [35, 50, 65, 80, 95, 100],
                "interview_tips": [{"type": "System Design", "advice": "Design a scalable API for a social media app."}]
            },
            {
                "title": "Frontend Architect (React)",
                "desc": "Design highly scalable and performant UI systems.",
                "salary": "₹14L - ₹32L",
                "skills": ["React", "Next.js", "Web Performance"],
                "locations": ["Remote", "Bengaluru"],
                "trend": [30, 45, 60, 80, 95, 100],
                "interview_tips": [{"type": "Architectural", "advice": "Handle state synchronization across micro-frontends."}]
            },
            {
                "title": "DevOps-focused Developer",
                "desc": "Developer who manages their own cloud infrastructure.",
                "salary": "₹15L - ₹35L",
                "skills": ["Docker", "AWS", "CI/CD"],
                "locations": ["Gurgaon", "Bengaluru"],
                "trend": [20, 35, 55, 75, 90, 100],
                "interview_tips": [{"type": "Automation", "advice": "Automate a deployment pipeline."}]
            },
            {
                "title": "Full-Stack Lead",
                "desc": "Lead engineering teams and set coding standards.",
                "salary": "₹25L - ₹50L",
                "skills": ["Leadership", "System Design", "Mentorship"],
                "locations": ["Bengaluru", "Mumbai"],
                "trend": [15, 30, 50, 70, 90, 100],
                "interview_tips": [{"type": "Leadership", "advice": "Discuss a time you mentored a junior developer."}]
            }
        ],
        "market_data": [42, 52, 62, 70, 80, 90, 100],
        "quote": "Master JS fundamentals, and frameworks will follow.",
        "academic_paths": [{"title": "BTech CSE", "duration": "4 years", "recommended": True}],
        "certifications": [{"name": "Meta Full Stack", "provider": "Meta", "level": "INTERMEDIATE"}],
        "platforms": [{"name": "The Odin Project", "desc": "Open source curriculum.", "url": "#"}],
        "jobs": [{"company": "Freshworks", "title": "Product Engineer", "salary": "₹14L - ₹22L"}],
        "youtube_query": "Full Stack Developer Roadmap India"
    }
}

PROJECT_DATA = {
    "title": "Navigator Intelligence",
    "tagline": "Simplifying the tech career journey for India's next generation.",
    "description": "Navigator is a smart guide designed to eliminate career confusion. Instead of overwhelming you with endless options, we focus on the top 8 trajectories currently dominating the Indian market.",
    "philosophy": "In an era of information overload, clarity is the ultimate competitive advantage.",
    "target_audience": [
        {"group": "Graduating Students", "need": "Bridge the gap between academic theory and the reality of the Indian tech market.", "icon": "🎓"},
        {"group": "Career Switchers", "need": "Navigate the pivot from legacy roles into high-growth modern tech paths.", "icon": "🔄"},
        {"group": "Junior Talent", "need": "Benchmark your current skills against 2026 industry standards.", "icon": "📈"}
    ],
    "core_values": [
        {"title": "Zero Noise", "desc": "We curate, we don't aggregate. No 50-step roadmaps—just the vital few skills.", "icon": "🔇"},
        {"title": "Hyper-Local", "desc": "Focused on what Bengaluru, Hyderabad, and Pune are actually paying.", "icon": "🇮🇳"},
        {"title": "AI-Augmented", "desc": "Combines industry expertise with real-time AI guidance.", "icon": "🤖"}
    ],
    "how_it_works": [
        {"step": "Explore", "desc": "Identify a career path using interactive 3D visualizations.", "icon": "🎯"},
        {"step": "Deep Dive", "desc": "Access high-fidelity roadmaps and salary benchmarks in INR.", "icon": "📈"},
        {"step": "Consult", "desc": "Get instant answers from our integrated AI Career Guide.", "icon": "⚡"}
    ],
    "what_it_does": [
        "Step-by-step learning roadmaps.",
        "Real-time salary trends in India.",
        "Instant AI-driven career guidance.",
        "Benchmarked market growth data."
    ],
    "what_it_not_does": [
        "Issue certificates or video lessons.",
        "Guarantee a job or specific salary.",
        "Track or store your personal identity.",
        "Replace the need for hard practice."
    ],
    "future_enhancements": [
        "Direct Job Board Integration",
        "AI-Powered Mock Interviewer",
        "Live Mentorship Networks",
        "Vernacular Language Support"
    ],
    "data_methodology": "Our engine synthesizes data from 500+ weekly job listings, platforms like AmbitionBox, and input from mentors in top Indian Unicorns.",
    "how_to_use": [
        {"step": "Navigate Dashboard", "desc": "Explore our interactive grid of high-velocity tech careers tailored for the Indian market.", "icon": "🧭"},
        {"step": "Unlock Intelligence", "desc": "Access high-fidelity roadmaps to uncover precise skill requirements, salary benchmarks, and interview tips.", "icon": "🔓"},
        {"step": "Consult AI Guide", "desc": "Engage with our specialized AI assistant, fine-tuned to answer specific queries on Indian hiring patterns.", "icon": "💬"}
    ]
}

@app.route('/explore')
def index():
    careers_list = list(CAREERS.values())
    return render_template('index.html', careers=careers_list)

@app.route('/')
def about():
    return render_template('about.html', project=PROJECT_DATA)

@app.route('/career/<career_id>')
def career_detail(career_id):
    career = CAREERS.get(career_id)
    if not career:
        return redirect(url_for('index'))
    return render_template('career.html', career=career)

@app.errorhandler(404)
def handle_404(e):
    return redirect(url_for('index'))

@app.route('/api/career/<career_id>')
def career_api(career_id):
    career = CAREERS.get(career_id)
    if not career:
        return jsonify({"error": "Not found"}), 404
    return jsonify(career)

@app.route('/api/chat/<career_id>', methods=['POST'])
def chat(career_id):
    career = CAREERS.get(career_id)
    if not career:
        return jsonify({"error": "Not found"}), 404
    
    data = request.get_json()
    question = data.get('question', '').lower()
    
    # 1. Define Knowledge Base Keywords to detect relevant vs outside questions
    knowledge_keywords = [
        'salary', 'pay', 'earn', 'lpa', 'money', 'income', 'package',
        'work', 'environment', 'culture', 'stress', 'daily', 'day',
        'role', 'job', 'work', 'career', 'position', 'opportunity', 'sub-role', 'specialization',
        'start', 'how', 'begin', 'step', 'first',
        'learn', 'roadmap', 'path', 'guide', 'journey', 'syllabus', 'interview', 'prep', 'tips', 'questions', 'cracking', 'course', 'training', 'classes',
        'company', 'hiring', 'hub', 'city', 'location', 'place', 'bengaluru', 'pune', 'hyderabad', 'mumbai',
        'skill', 'tool', 'tech', 'code', 'software', 'language', 'stack',
        'degree', 'college', 'study', 'education', 'academic', 'btech', 'mca', 'bca',
        'cert', 'growth', 'market', 'trend', 'future', 'scope'
    ]

    # 2. Extract career-specific terms (sub-roles and skills) to broaden knowledge
    career_terms = [kw.lower() for kw in career.get('sub_roles', [])]
    career_terms.append(career['title'].lower())
    career_terms.extend([r['title'].lower() for r in career.get('job_roles', [])])
    for role in career.get('job_roles', []):
        career_terms.extend([s.lower() for s in role.get('skills', [])])
    
    # 3. Fuzzy Matching Helper for typo tolerance
    def has_intent(targets, cutoff=0.7):
        # Prioritize exact substring match first
        if any(t in question for t in targets):
            return True
        # Then check for fuzzy word matches
        for word in question.split():
            if len(word) > 2: # Only fuzzy match words longer than 2 chars
                if difflib.get_close_matches(word, targets, n=1, cutoff=cutoff):
                    return True
        return False

    is_related = has_intent(knowledge_keywords + career_terms)
    
    # Unified Role Detection: Detect if a specific role is mentioned early
    suggested_role = None
    for r in career.get('job_roles', []):
        if r['title'].lower() in question:
            suggested_role = r['title']
            break
            
    if not suggested_role and career.get('job_roles'):
        # Default to the primary role if no specific role is mentioned
        suggested_role = career['job_roles'][0]['title']

    if not is_related:
        return jsonify({
            "response": f"I am your specialized Career Guide for **{career['title']}**. To provide the most accurate guidance, please keep your questions focused on career paths, salaries, skills, or certifications within this field.",
            "suggested_role": None
        })

    # 4. Knowledge-Based responses
    if has_intent(['salary', 'pay', 'earn', 'lpa', 'package']):
        # Check for specific role mentions
        for r in career.get('job_roles', []):
            if r['title'].lower() in question:
                return jsonify({
                    "response": f"For a **{r['title']}** in the **{career['title']}** field, the salary in India typically ranges from **{r['salary']}**, depending on the company and your experience level.",
                    "suggested_role": r['title']
                })
        
        roles_info = [f"{r['title']} (**{r['salary']}**)" for r in career.get('job_roles', [])[:3]]
        resp = f"The salary range for **{career['title']}** in India typically spans **{career['salary']}**. Specifically, roles like {', '.join(roles_info)} offer competitive packages."
        return jsonify({"response": resp, "suggested_role": suggested_role})
    
    if has_intent(['role', 'sub-role', 'specialization', 'position', 'types of jobs']):
        roles = career.get('sub_roles', [])
        if not roles:
            roles = [r['title'] for r in career.get('job_roles', [])]
        if roles:
            return jsonify({
                "response": f"Key specializations in **{career['title']}** include: **{', '.join(roles)}**. You can explore details for each of these by clicking the cards in the 'Top Job Roles' section.",
                "suggested_role": suggested_role
            })

    if has_intent(['low-code', 'high-code', 'coding', 'programming', 'no-code']):
        if career['id'] in ['uiux', 'product']:
            resp = f"**{career['title']}** is primarily a **low-code to no-code** field. While you don't need to write production code, understanding technical workflows is very beneficial for collaboration."
        elif career['id'] in ['servicenow', 'salesforce']:
            resp = f"**{career['title']}** is a hybrid. It offers **low-code** administration paths and **high-code** development paths (using JavaScript or Apex). It's a great choice if you want to choose your level of technical depth."
        else:
            resp = f"**{career['title']}** is a **high-code** technical career. Proficiency in programming languages and technical logic is essential for success in this field."
        return jsonify({
            "response": resp,
            "suggested_role": suggested_role
        })

    if has_intent(['start', 'how', 'begin', 'step', 'first']):
        first_cert = career['certifications'][0]['name'] if career['certifications'] else "industry certifications"
        path = career['academic_paths'][0]['title'] if career['academic_paths'] else "a relevant degree"
        return jsonify({
            "response": f"To begin a career in **{career['title']}**, we recommend: 1) Pursuing **{path}**, 2) Mastering core skills, and 3) Targeting the **'{first_cert}'** certification.",
            "suggested_role": suggested_role
        })

    if has_intent(['skill', 'tool', 'tech', 'code', 'stack', 'language']):
        # Check for specific role skills
        for r in career.get('job_roles', []):
            if r['title'].lower() in question:
                skills_str = ", ".join(r.get('skills', []))
                return jsonify({
                    "response": f"To succeed as a **{r['title']}**, you should master: **{skills_str}**. These are the core tools hiring managers look for in this specialization.",
                    "suggested_role": r['title']
                })
        
        all_skills = set()
        for r in career.get('job_roles', []):
            all_skills.update(r.get('skills', []))
        skill_list = list(all_skills)[:6]
        skill_hint = f" including {', '.join(skill_list)}" if skill_list else ""
        return jsonify({
            "response": f"Success in {career['title']} requires a robust toolset{skill_hint}. You can view the full technical stack by selecting any specialization card.",
            "suggested_role": suggested_role
        })

    if has_intent(['cert', 'certification', 'course', 'training', 'learn']):
        certs = career.get('certifications', [])
        if certs:
            cert_list = "\n".join([f"• **{c['name']}** ({c['provider']}) - [Start Course]({c.get('url', '#')})" for c in certs])
            return jsonify({
                "response": f"To master **{career['title']}**, we recommend these top-tier certifications and courses:\n\n{cert_list}",
                "suggested_role": suggested_role
            })

    if has_intent(['roadmap', 'path', 'guide', 'syllabus', 'degree', 'college', 'academic', 'education']):
        path_title = career['academic_paths'][0]['title'] if career['academic_paths'] else "the recommended path"
        return jsonify({
            "response": f"The {career['title']} field involves {career['career_paths']} distinct paths. We generally recommend starting with {path_title}.",
            "suggested_role": suggested_role
        })

    if has_intent(['company', 'hiring', 'hub', 'city', 'location', 'place', 'where']):
        # Check specific role locations
        for r in career.get('job_roles', []):
            if r['title'].lower() in question:
                locs = ", ".join(r.get('locations', []))
                return jsonify({
                    "response": f"The **{r['title']}** role is currently in high demand in hubs like **{locs}**. Remote opportunities are also quite common in this specialization.",
                    "suggested_role": r['title']
                })

        companies = [j['company'] for j in career['jobs'][:3]]
        return jsonify({
            "response": f"Major hiring hubs for **{career['title']}** include Bengaluru, Hyderabad, and Pune. Top companies currently recruiting in India include **{', '.join(companies)}**.",
            "suggested_role": suggested_role
        })

    if has_intent(['interview', 'prep', 'tips', 'questions', 'cracking']):
        # If a specific role was detected in the question
        if suggested_role:
            role_obj = next((r for r in career.get('job_roles', []) if r['title'] == suggested_role), None)
            if role_obj:
                tips = role_obj.get('interview_tips', [])
                if tips:
                    tips_str = "\n".join([f"• **{t['type']}**: {t['advice']}" for t in tips])
                    return jsonify({
                        "response": f"To crack an interview for **{suggested_role}**, focus on these core areas:\n\n{tips_str}",
                        "suggested_role": suggested_role
                    })
                else:
                    return jsonify({
                        "response": f"For **{suggested_role}** interviews, master tools like {', '.join(role_obj.get('skills', [])[:3])}, prepare a strong portfolio walkthrough, and use the STAR method for behavioral rounds.",
                        "suggested_role": suggested_role
                    })
        
        return jsonify({
            "response": f"In **{career['title']}** interviews, hiring managers usually look for a combination of technical depth, process clarity, and cultural fit. Would you like specific tips for a particular role?",
            "suggested_role": suggested_role
        })

    if has_intent(['growth', 'market', 'trend', 'future', 'scope']):
        return jsonify({
            "response": f"{career['title']} is seeing an impressive {career['yoy_growth']} YoY growth in India. With digital transformation accelerating, the long-term scope for this field is exceptionally strong.",
            "suggested_role": suggested_role
        })

    if has_intent(['work', 'environment', 'culture', 'stress', 'daily', 'day']):
        return jsonify({
            "response": f"In a typical {career['title']} role, the work culture is fast-paced. "
                        f"You'll usually find a mix of deep focus work and collaborative syncs. "
                        f"Click on any of the 'Job Role' cards above to see a detailed 'Day in the Life' schedule for that specific path!",
            "suggested_role": suggested_role
        })

    # Fallback knowledge-based response
    return jsonify({
        "response": f"As your {career['title']} guide, I can confirm this field offers a {career['yoy_growth']} growth rate with salaries up to {career['salary']}. Would you like to know more about specific sub-roles, required skills, or the recommended academic path?",
        "suggested_role": suggested_role
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)