import streamlit as st
import time

# ==============================================================================
# PREMIUM MODERN UI CONFIGURATION & OVERRIDES (Light Theme SaaS Style)
# ==============================================================================
st.set_page_config(
    page_title="HELP AI",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom injection to enforce the Apple/Linear light aesthetic across native widgets
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    /* Global Base Reset to Premium Light SaaS Palette */
    .stApp {
        background-color: #F7FAFC !important;
        color: #111827 !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Target Typography overrides */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Standardize Container Card Styling (White Layout, Soft Shadows, Minimal Borders) */
    [data-testid="stMetricBorderDiv"], .stElementContainer div[data-style="border"], .stForm {
        background-color: #FFFFFF !important;
        border: 1px solid #E5E7EB !important;
        border-radius: 12px !important;
        padding: 24px !important;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px -1px rgba(0, 0, 0, 0.05) !important;
        color: #111827 !important;
    }

    /* Metric Data Rendering Style Overrides */
    [data-testid="stMetricValue"] {
        font-size: 36px !important;
        font-weight: 800 !important;
        color: #4F8EF7 !important;
        letter-spacing: -0.02em !important;
    }
    [data-testid="stMetricLabel"] {
        color: #6B7280 !important;
        font-weight: 500 !important;
    }

    /* Premium Startup Button Component Rules */
    div.stButton > button {
        background-color: #4F8EF7 !important;
        color: #FFFFFF !important;
        border-radius: 8px !important;
        border: 1px solid #4F8EF7 !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05) !important;
    }
    div.stButton > button:hover {
        background-color: #3B7DDD !important;
        border-color: #3B7DDD !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
    }
    div.stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* Input Widget Cleanups */
    .stSelectbox div[data-baseweb="select"], .stMultiSelect div[data-baseweb="select"], .stTextInput input {
        background-color: #FFFFFF !important;
        border: 1px solid #E5E7EB !important;
        border-radius: 8px !important;
        color: #111827 !important;
    }
    
    /* Clean Sidebar Customization */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E5E7EB !important;
    }
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label {
        color: #111827 !important;
    }

    /* Premium custom timeline wrapper */
    .timeline-container {
        border-left: 2px solid #E5E7EB;
        margin-left: 16px;
        padding-left: 24px;
        position: relative;
    }
    .timeline-step {
        margin-bottom: 24px;
        position: relative;
    }
    .timeline-step::before {
        content: '';
        position: absolute;
        left: -33px;
        top: 4px;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        background-color: #4F8EF7;
        border: 4px solid #FFFFFF;
        box-shadow: 0 0 0 1px #E5E7EB;
    }
</style>
"""
st.html(custom_css)

# ==============================================================================
# MASTER KNOWLEDGE DICTIONARIES (All 16 Personalities Core Matrix Data)
# ==============================================================================
PERSONALITY_REGISTRY = {
    "INTJ": {
        "title": "The Planner", 
        "strengths": ["Great at planning", "Logical thinker", "Works well alone", "Never gives up"], 
        "growth": ["Can seem a bit stubborn", "Overthinks simple things", "Forgets to think about feelings"],
        "questions": [
            "Do you prefer focusing on big, long-term plans rather than small day-to-day tasks?",
            "Do you prefer working completely by yourself instead of in a group?",
            "Do you love strategy games, logic puzzles, or finding shortcuts?",
            "Is making a process run perfectly the most important goal for you?",
            "Would you rather design a master blueprint than manage a team of people?"
        ],
        "universities": ["MIT", "Stanford", "ETH Zurich", "Carnegie Mellon"],
        "diversity_map": {
            "Technology": {
                "bonus": {"AI Engineer": 10, "Software Engineer": 8, "Data Scientist": 9, "Cybersecurity Specialist": 7},
                "roadmap": [
                    "Phase 1: Learn the basics of logic, coding foundations, and Python.", 
                    "Phase 2: Build a few small automation apps and backend programs by yourself.", 
                    "Phase 3: Create secure system networks and learn how encryption works.", 
                    "Phase 4: Set up automated cloud computing clusters online."
                ],
                "projects": ["Build an AI Neural Network Blueprint", "Create a Private Code-Based Hacking Defense Center"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 8, "Entrepreneur": 6},
                "roadmap": [
                    "Phase 1: Read up on charts, finance, and how store sales numbers change.", 
                    "Phase 2: Use spreadsheets to practice predicting sales for an imaginary startup.", 
                    "Phase 3: Map out systemic corporate growth models and company safety checks.", 
                    "Phase 4: Design a master operational plan for a mock tech business launch."
                ],
                "projects": ["Create a Smart Market Tracker Spreadsheet", "Write a Multi-Year Business Strategy Plan"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 7, "Pharmacist": 6},
                "roadmap": [
                    "Phase 1: Study biology data, cell blueprints, and basic DNA code patterns.", 
                    "Phase 2: Use a simulator to see how health records are handled securely.", 
                    "Phase 3: Design a step-by-step layout program to speed up hospital labs.", 
                    "Phase 4: Complete a study on tracing the speed of new illness variants."
                ],
                "projects": ["Design a Digital DNA Code Mapping Model", "Build a Hospital Lab Tracking Simulator"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Professor": 8, "Teacher": 5},
                "roadmap": [
                    "Phase 1: Explore studies about how students learn and complete school tasks.", 
                    "Phase 2: Plan an automated testing model that adapts to student grades.", 
                    "Phase 3: Design a new digital study checklist for multiple schools to use.", 
                    "Phase 4: Launch your own plan to show schools how to improve student scores."
                ],
                "projects": ["Build an Adaptive Student Learning App", "Design a School District Report Card System"]
            },
            "Engineering": {
                "bonus": {"Electrical Engineer": 10, "Mechanical Engineer": 8, "Civil Engineer": 7},
                "roadmap": [
                    "Phase 1: Look at computer models showing weight limits for structural parts.", 
                    "Phase 2: Learn how to program microcontrollers and circuit board logic lines.", 
                    "Phase 3: Run structural strain test designs using software on a laptop.", 
                    "Phase 4: Design blueprints for a large-scale automated infrastructure layout."
                ],
                "projects": ["Create a Smart Traffic Infrastructure Simulator", "Build a Software Stress-Tester for Bridges"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Animator": 7, "Content Creator": 5},
                "roadmap": [
                    "Phase 1: Learn the hidden grid rules and geometry behind clean design systems.", 
                    "Phase 2: Write short design scripts to auto-generate vector icons and patterns.", 
                    "Phase 3: Create an official user interface design book for your favorite apps.", 
                    "Phase 4: Design complete digital interactive prototypes for tech clients."
                ],
                "projects": ["Design a Universal Mobile UI Token Theme", "Build a Code-Driven Art Pattern Builder"]
            }
        }
    },
    "INTP": {
        "title": "The Thinker", 
        "strengths": ["Deeply analytical", "Highly original", "Open-minded", "Fair and honest"], 
        "growth": ["Can feel a bit disconnected", "Might sound critical", "Does not like strict rules"],
        "questions": [
            "Do you find yourself constantly trying to figure out how big, abstract ideas work?",
            "Do you care more about coming up with brand-new ideas than following old rules?",
            "Are you happy to switch projects halfway if you discover a more interesting puzzle?",
            "Do you naturally spot logic mistakes or weak points when people argue?",
            "Would you rather discover a new scientific rule than build a product to sell?"
        ],
        "universities": ["MIT", "Stanford", "ETH Zurich", "Carnegie Mellon"],
        "diversity_map": {
            "Technology": {
                "bonus": {"AI Engineer": 10, "Data Scientist": 9, "Software Engineer": 7, "Cybersecurity Specialist": 6},
                "roadmap": [
                    "Phase 1: Dive into computer science code theory and functional logic rules.", 
                    "Phase 2: Build a mini coding language engine to learn how code runs.", 
                    "Phase 3: Experiment with training new and different types of AI systems.", 
                    "Phase 4: Write your own open-source code libraries for other programmers to use."
                ],
                "projects": ["Create Your Own Mini Coding Language Engine", "Build an AI Auto-Tuning Code Module"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 7, "Entrepreneur": 5},
                "roadmap": [
                    "Phase 1: Study economic patterns and game strategy concepts.", 
                    "Phase 2: Build a model simulation to see how prices shift in a digital store.", 
                    "Phase 3: Look at how blockchain data ledgers verify records safely.", 
                    "Phase 4: Think up totally new models for running and funding future tech setups."
                ],
                "projects": ["Build a Game Theory Strategy Simulator", "Design a Digital Coin Economic System Map"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Pharmacist": 8, "Doctor": 5},
                "roadmap": [
                    "Phase 1: Study huge tables of clinical cell data to look for patterns.", 
                    "Phase 2: Map out how different molecules change when mixed together.", 
                    "Phase 3: Write code logic that predicts how an illness can change over time.", 
                    "Phase 4: Present completely fresh scientific theories on cellular health."
                ],
                "projects": ["Build a Chemical Compounding Mixer Simulator", "Create an Illness Variation Tracking Map"]
            },
            "Education": {
                "bonus": {"Professor": 10, "Education Consultant": 8, "Teacher": 5},
                "roadmap": [
                    "Phase 1: Study how the brain captures information and solves mental blocks.", 
                    "Phase 2: Build a program that calculates exactly where a student got confused.", 
                    "Phase 3: Create a clean framework chart of learning skills for schools.", 
                    "Phase 4: Start an independent logic training bootcamp class online."
                ],
                "projects": ["Build a Student Learning Gap Map Application", "Design a Brain-Based Study Skill Tracker"]
            },
            "Engineering": {
                "bonus": {"Electrical Engineer": 10, "Mechanical Engineer": 8, "Civil Engineer": 6},
                "roadmap": [
                    "Phase 1: Learn about physical energy, heat rules, and waves from first principles.", 
                    "Phase 2: Code your own low-level chip program instructions for sensor devices.", 
                    "Phase 3: Simulate untraditional product designs using virtual spaces.", 
                    "Phase 4: Test out brand-new material compounds to see how they handle stress."
                ],
                "projects": ["Write Code for a Custom Sensor Controller Box", "Build a Virtual Energy-Flow Simulation Test"]
            },
            "Creative Arts": {
                "bonus": {"Animator": 10, "Graphic Designer": 7, "Content Creator": 6},
                "roadmap": [
                    "Phase 1: Discover how geometry rules create endless algorithmic patterns.", 
                    "Phase 2: Code your own mini physics rule tools for cartoon motion frames.", 
                    "Phase 3: Write rendering filters to change shadows and lighting in graphics.", 
                    "Phase 4: Act as a master consultant on art generation engine code platforms."
                ],
                "projects": ["Code an Automatic Math-Based Pattern Canvas", "Build a Custom Motion Physics Animation Tool"]
            }
        }
    },
    "ENTJ": {
        "title": "The Captain", 
        "strengths": ["Highly organized", "Full of energy", "Confident", "Strong leader"], 
        "growth": ["Can be strict", "Likes to control things", "Becomes impatient easily"],
        "questions": [
            "Do you naturally step up and guide a group when an assignment gets stuck?",
            "Are you driven by competing and winning in a fast-moving market?",
            "Do you find it rewarding to manage deadlines and assign tasks to teammates?",
            "Is finishing a project quickly more important to you than making it 100% flawless?",
            "Do you actively plan out your next educational steps and career milestones every single day?"
        ],
        "universities": ["Stanford", "Wharton", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Product Manager": 10, "Cybersecurity Specialist": 8, "Software Engineer": 7, "AI Engineer": 6},
                "roadmap": [
                    "Phase 1: Lead a group of youth programmers inside a coding club project.", 
                    "Phase 2: Set strict code safety and release standards for your app builds.", 
                    "Phase 3: Supervise how apps are updated and kept running under heavy use.", 
                    "Phase 4: Manage a real development team to deploy major software platforms globally."
                ],
                "projects": ["Build a Multi-User Project Planner Tool", "Design a Tech Infrastructure Performance Report"]
            },
            "Business": {
                "bonus": {"Entrepreneur": 10, "Product Manager": 9, "Business Analyst": 8, "Marketing Manager": 7},
                "roadmap": [
                    "Phase 1: Research how startups raise money and plan their cash runways.", 
                    "Phase 2: Practice pitching and writing deals with real-world target sponsors.", 
                    "Phase 3: Launch a major customer growth campaign for a small store or project.", 
                    "Phase 4: Build your own full corporate enterprise to scale up in the market."
                ],
                "projects": ["Create a Startup Cash Runway Pitch Deck", "Design a Market Expansion Launch Matrix"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Medical Researcher": 8, "Pharmacist": 6},
                "roadmap": [
                    "Phase 1: Manage schedules and medicine supply counts for a mockup clinic.", 
                    "Phase 2: Ensure all laboratory safety checks are met perfectly during tests.", 
                    "Phase 3: Lead an emergency team simulation to coordinate doctors in a crisis.", 
                    "Phase 4: Direct a full network of public regional clinics and health workers."
                ],
                "projects": ["Build a Clinic Staff Schedule Routing Core", "Design a Hospital Compliance Audit System"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Professor": 8, "Teacher": 6},
                "roadmap": [
                    "Phase 1: Structure budget blueprints and spending balances for a virtual school.", 
                    "Phase 2: Enforce high test score goals across digital classroom groups.", 
                    "Phase 3: Direct team building workshops for student body organizers.", 
                    "Phase 4: Lead an entire university group or regional school network system."
                ],
                "projects": ["Build a Virtual School Budget Tracker App", "Design an Academic Performance Score Grid"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 8, "Electrical Engineer": 7},
                "roadmap": [
                    "Phase 1: Supervise timelines for a large building development sandbox project.", 
                    "Phase 2: Put manufacturing speed targets into action for factory product builds.", 
                    "Phase 3: Lead a big crew of junior mechanics or field builders on a challenge.", 
                    "Phase 4: Direct a multinational structural infrastructure engineering project."
                ],
                "projects": ["Design a Factory Line Speed Optimization Tool", "Build an Infrastructure Lifecycle Asset Matrix"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Marketing Manager": 9, "Graphic Designer": 6},
                "roadmap": [
                    "Phase 1: Launch your own high-volume content creator group and studio space.", 
                    "Phase 2: Manage major advertising campaign graphics for student festivals.", 
                    "Phase 3: Handle total visual brand rules for a collection of dynamic brands.", 
                    "Phase 4: Command a world-class creative agency network or movie house."
                ],
                "projects": ["Design a Creative Studio Media Production Tracker", "Build a Multi-Channel Brand Asset Monetization Plan"]
            }
        }
    },
    "ENTP": {
        "title": "The Inventor", 
        "strengths": ["Very creative", "Super curious", "Learns quickly", "Startup mindset"], 
        "growth": ["Gets bored with routines", "Hates repetitive tasks", "Argues a lot"],
        "questions": [
            "Do you love questioning old rules and debating wild, unusual ideas?",
            "Would you rather start an experimental startup than work at an established company?",
            "Are you excited to discover how Artificial Intelligence is changing the world?",
            "Do you enjoy taking apart confusing, complicated problems to solve them your way?",
            "Do you struggle to finish daily tasks once the creative part is done?"
        ],
        "universities": ["Stanford", "Wharton", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Entrepreneur": 10, "AI Engineer": 9, "Software Engineer": 7, "Data Scientist": 6},
                "roadmap": [
                    "Phase 1: Code quick app ideas using Python.", 
                    "Phase 2: Launch 5 fast AI web wrappers over a single weekend.", 
                    "Phase 3: Pitch your unique ideas at high-energy hackathon tournaments.", 
                    "Phase 4: Create an open software lab to build and launch automated applications."
                ],
                "projects": ["Build an AI-Powered Startup Name Validator App", "Create a Gamified Student Daily Study App"]
            },
            "Business": {
                "bonus": {"Entrepreneur": 10, "Marketing Manager": 9, "Product Manager": 8, "Business Analyst": 6},
                "roadmap": [
                    "Phase 1: Invent clever growth tricks using free online channels.", 
                    "Phase 2: Build canvas sketches for weird and wild store monetization choices.", 
                    "Phase 3: Test your ideas out on small audiences to see if they sell.", 
                    "Phase 4: Run multiple small, automated digital micro-ventures simultaneously."
                ],
                "projects": ["Create a Growth-Hack Marketing Test Sandbox", "Design an Interactive Digital Business Canvas Tool"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 7, "Pharmacist": 5},
                "roadmap": [
                    "Phase 1: Sketch ideas for mobile medical companion apps.", 
                    "Phase 2: Set up alternative online channels to share clean health advice.", 
                    "Phase 3: Build a quick, user-friendly video call portal for mock clinics.", 
                    "Phase 4: Shake up old clinical systems by introducing fast digital tools."
                ],
                "projects": ["Design a Telehealth App User Experience Interface", "Build a Workflow Disruption Map for Old Clinics"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Teacher": 8, "Professor": 6},
                "roadmap": [
                    "Phase 1: Build points-based quiz games for high school test revision.", 
                    "Phase 2: Run an alternative student group panel debate program.", 
                    "Phase 3: Start your own online edutainment channel or blog platform.", 
                    "Phase 4: Scale your own virtual learning system to kids around the world."
                ],
                "projects": ["Build a Points-Based Interactive Study Quiz App", "Design a Virtual Alternative Micro-School Portal"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 8, "Civil Engineer": 5},
                "roadmap": [
                    "Phase 1: Make quick 3D prototype models for a fun new invention idea.", 
                    "Phase 2: Connect simple microchip sensors to track indoor weather signs.", 
                    "Phase 3: Enter green energy design concepts into science fairs.", 
                    "Phase 4: Run an agile hardware lab focused on building fast design samples."
                ],
                "projects": ["Create a 3D Printing Prototyping Guide System", "Build an IoT Sensor Array Weather Tracker Box"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Graphic Designer": 8, "Animator": 7},
                "roadmap": [
                    "Phase 1: Create multiple digital profiles to share modern art ideas.", 
                    "Phase 2: Write custom visual code scripts that mix code with art frames.", 
                    "Phase 3: Run interactive digital show streams for youth artists.", 
                    "Phase 4: Consult for fast-moving business tech setups on their creative branding."
                ],
                "projects": ["Build a Generative Code Art Playground Engine", "Design an Immersive Startup Brand Identity Token Set"]
            }
        }
    },
    "INFJ": {
        "title": "The Counselor", "strengths": ["Creative", "Insightful", "Principled", "Passionate"], "growth": ["Sensitive", "Extremely Private", "Perfectionist"],
        "questions": [
            "Does helping people matter more to you than how much money you earn?",
            "Can you easily feel what other people are planning or feeling long-term?",
            "Do you have a deep set of morals that you refuse to break for any reason?",
            "Do you prefer mentoring a single close friend over talking to a massive crowd?",
            "Do you want to fix human unfairness using clever, systemic design plans?"
        ],
        "universities": ["Harvard", "Johns Hopkins", "Oxford", "Aga Khan University"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Data Scientist": 8, "AI Engineer": 7, "Cybersecurity Specialist": 6},
                "roadmap": ["Phase 1: Code open-source privacy apps that protect user data safety.", "Phase 2: Build clean data charts for humanitarian and charity groups.", "Phase 3: Design app layouts that are accessible for people with disabilities.", "Phase 4: Lead software engineering teams at major non-profit organizations."],
                "projects": ["Build an Open-Source Data Privacy Guard App", "Design an Accessible User Interface Template for Seniors"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 7, "Marketing Manager": 6},
                "roadmap": ["Phase 1: Create a charter plan for a community-first charity store business.", "Phase 2: Study how ethical trade choices impact small community makers.", "Phase 3: Write growth guidelines focused on employee wellness and safety.", "Phase 4: Direct a global network focused on ethical social impact investments."],
                "projects": ["Design a Fair-Trade Supply Flow Audit Sheet", "Build a Social Enterprise Investment Matrix Tracker"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Medical Researcher": 9, "Pharmacist": 6},
                "roadmap": ["Phase 1: Study how to give warm, supportive mental guidance to patients.", "Phase 2: Help lead community health drives to prevent local illnesses.", "Phase 3: Write empathetic medical communication rules for hospital helpers.", "Phase 4: Manage your own specialized clinic focused on compassionate care."],
                "projects": ["Create a Community Health Awareness Database Tracker", "Design a Patient Care Communication Strategy Plan"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 9, "Professor": 8},
                "roadmap": ["Phase 1: Build helpful custom study guides for students who are stuck.", "Phase 2: Design supportive learning tools for special education classrooms.", "Phase 3: Set up safe, supportive student peer mentoring groups in schools.", "Phase 4: Write research papers to make school funding more fair for everyone."],
                "projects": ["Build a Student Progress Support Portal App", "Design a School Peer Mentoring Program Framework"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 7, "Electrical Engineer": 6},
                "roadmap": ["Phase 1: Read up on eco-friendly green building rules and solar designs.", "Phase 2: Map out layout pipelines to bring fresh water to rural towns.", "Phase 3: Review public park structures to make sure they are totally safe.", "Phase 4: Direct international engineering relief operations around the world."],
                "projects": ["Design a Rural Clean Water Pipe Grid Layout", "Build an Eco-Friendly Building Material Strain Checker"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Content Creator": 8, "Animator": 7},
                "roadmap": ["Phase 1: Create powerful poster designs for human rights charity groups.", "Phase 2: Write thoughtful story booklets about overcoming hard life events.", "Phase 3: Design welcoming app interface formats that feel calm and safe.", "Phase 4: Run an independent design studio that assists purposeful brands."],
                "projects": ["Design a Visual Identity Asset Set for a Non-Profit", "Create a High-Empathy User Experience UI Wireframe"]
            }
        }
    },
    "INFA": { "title": "The Dreamer", "strengths": ["Kind-hearted", "Generous", "Very imaginative", "Open-minded"], "growth": ["Can be unrealistic", "Stays alone too much", "Gets feelings hurt easily"], "questions": ["Do you choose your class tracks based on how well they match your personal morals?", "Do you find creative storytelling, poetry, or sketching deeply comforting?", "Do you need lots of quiet, alone time to recharge your mental battery?", "Are you highly sensitive to arguments, shouting, or fierce competitions?", "Do you look at tech tools as a creative canvas to share your inner worldview?"], "universities": ["RISD", "CalArts", "NCA", "Harvard"], "diversity_map": { "Technology": { "bonus": {"Software Engineer": 10, "AI Engineer": 7, "Data Scientist": 6}, "roadmap": ["Phase 1: Learn markdown writing, text tags, and minimalist web code.", "Phase 2: Build a personal online poetry or art gallery page.", "Phase 3: Create localized chat spaces for creative student groups.", "Phase 4: Oversee product layouts that focus entirely on user peace of mind."], "projects": ["Build a Minimalist Creative Writing App Prototype", "Design a Local Student Art Sharing Platform Web Node"] }, "Business": { "bonus": {"Business Analyst": 10, "Marketing Manager": 7, "Product Manager": 6}, "roadmap": ["Phase 1: Read up on supportive, stress-free workplace rules for teams.", "Phase 2: Plan business tracks for independent handmade product artists.", "Phase 3: Set up authentic brand strategies that do not use pushy sales tricks.", "Phase 4: Counsel startup business founders on keeping their staff happy and calm."], "projects": ["Create a Business Tracker for Independent Handcrafted Shops", "Design an Office Wellness Environment Audit System"] }, "Healthcare": { "bonus": {"Medical Researcher": 10, "Doctor": 6, "Pharmacist": 5}, "roadmap": ["Phase 1: Research how listening to music or painting can heal stress levels.", "Phase 2: Design a simple layout guide using art therapy for therapy rooms.", "Phase 3: Review health support access levels for families in tiny remote villages.", "Phase 4: Advocate for community-based emotional relief and wellness networks."], "projects": ["Design an Art Therapy Progress Logging System Tracker", "Map Out Healthcare Access Differences in Remote Towns"] }, "Education": { "bonus": {"Teacher": 10, "Education Consultant": 8, "Professor": 6}, "roadmap": ["Phase 1: Write sweet, imaginative narrative storybooks for early readers.", "Phase 2: Run your own online creative writing workshops for teenagers.", "Phase 3: Map out individualized home-study progress plans for distance learning.", "Phase 4: Build niche emotional intelligence courses to help kids understand feelings."], "projects": ["Create an Illustrated Storybook Lesson Module Deck", "Build an Emotional Intelligence Goal Tracker App for Kids"] }, "Engineering": { "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 7, "Civil Engineer": 5}, "roadmap": ["Phase 1: Sketch model blueprints based on organic forms found in nature.", "Phase 2: Design affordable alternative tool concepts for low-income areas.", "Phase 3: Review how smart building layouts can capture raw morning sunlight.", "Phase 4: Consult on tiny, sustainable local engineering projects for villages."], "projects": ["Build a Nature-Inspired Moving Toy Model Rig", "Design an Affordable Low-Income Mechanical Tool Concept"] }, "Creative Arts": { "bonus": {"Graphic Designer": 10, "Content Creator": 9, "Animator": 8}, "roadmap": ["Phase 1: Fill up a large sketchbook with deeply personal vector artwork.", "Phase 2: Code your own visual choose-your-own-adventure story app.", "Phase 3: Draw a complete custom character library with matching descriptions.", "Phase 4: Run an independent digital illustration brand showing your art styles."], "projects": ["Code an Interactive Visual Story App Blueprint", "Create a Bespoke Character Vector Asset Library Node"] } } },
    "INFP": {
        "title": "The Dreamer", "strengths": ["Kind-hearted", "Generous", "Very imaginative", "Open-minded"], "growth": ["Can be unrealistic", "Stays alone too much", "Gets feelings hurt easily"],
        "questions": [
            "Do you choose your class tracks based on how well they match your personal morals?",
            "Do you find creative storytelling, poetry, or sketching deeply comforting?",
            "Do you need lots of quiet, alone time to recharge your mental battery?",
            "Are you highly sensitive to arguments, shouting, or fierce competitions?",
            "Do you look at tech tools as a creative canvas to share your inner worldview?"
        ],
        "universities": ["RISD", "CalArts", "NCA", "Harvard"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "AI Engineer": 7, "Data Scientist": 6},
                "roadmap": ["Phase 1: Learn markdown writing, text tags, and minimalist web code.", "Phase 2: Build a personal online poetry or art gallery page.", "Phase 3: Create localized chat spaces for creative student groups.", "Phase 4: Oversee product layouts that focus entirely on user peace of mind."],
                "projects": ["Build a Minimalist Creative Writing App Prototype", "Design a Local Student Art Sharing Platform Web Node"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Marketing Manager": 7, "Product Manager": 6},
                "roadmap": ["Phase 1: Read up on supportive, stress-free workplace rules for teams.", "Phase 2: Plan business tracks for independent handmade product artists.", "Phase 3: Set up authentic brand strategies that do not use pushy sales tricks.", "Phase 4: Counsel startup business founders on keeping their staff happy and calm."],
                "projects": ["Create a Business Tracker for Independent Handcrafted Shops", "Design an Office Wellness Environment Audit System"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 6, "Pharmacist": 5},
                "roadmap": ["Phase 1: Research how listening to music or painting can heal stress levels.", "Phase 2: Design a simple layout guide using art therapy for therapy rooms.", "Phase 3: Review health support access levels for families in tiny remote villages.", "Phase 4: Advocate for community-based emotional relief and wellness networks."],
                "projects": ["Design an Art Therapy Progress Logging System Tracker", "Map Out Healthcare Access Differences in Remote Towns"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 8, "Professor": 6},
                "roadmap": ["Phase 1: Write sweet, imaginative heirloom storybooks for early readers.", "Phase 2: Run your own online creative writing workshops for teenagers.", "Phase 3: Map out individualized home-study progress plans for distance learning.", "Phase 4: Build niche emotional intelligence courses to help kids understand feelings."],
                "projects": ["Create an Illustrated Storybook Lesson Module Deck", "Build an Emotional Intelligence Goal Tracker App for Kids"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 7, "Civil Engineer": 5},
                "roadmap": ["Phase 1: Sketch model blueprints based on organic forms found in nature.", "Phase 2: Design affordable alternative tool concepts for low-income areas.", "Phase 3: Review how smart building layouts can capture raw morning sunlight.", "Phase 4: Consult on tiny, sustainable local engineering projects for villages."],
                "projects": ["Build a Nature-Inspired Moving Toy Model Rig", "Design an Affordable Low-Income Mechanical Tool Concept"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Content Creator": 9, "Animator": 8},
                "roadmap": ["Phase 1: Fill up a large sketchbook with deeply personal vector artwork.", "Phase 2: Code your own visual choose-your-own-adventure story app.", "Phase 3: Draw a complete custom character library with matching descriptions.", "Phase 4: Run an independent digital illustration brand showing your art styles."],
                "projects": ["Code an Interactive Visual Story App Blueprint", "Create a Bespoke Character Vector Asset Library Node"]
            }
        }
    },
    "ENFJ": {
        "title": "The Guide", "strengths": ["Charismatic", "Inspiring", "Caring", "Natural leader"], "growth": ["Expects too much", "Forgets their own needs", "Worries what peers think"],
        "questions": [
            "Do you truly love helping your peers unlock their hidden talents?",
            "Are you always selected to lead collaborative projects or student councils?",
            "Do you care more about team happiness than cold, technical speed?",
            "Can you easily explain complicated subjects to a large, confused crowd?",
            "Do you feel energized when you receive open, honest praise from your group?"
        ],
        "universities": ["Stanford", "Harvard", "LUMS", "Oxford"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Product Manager": 10, "Software Engineer": 7, "AI Engineer": 6},
                "roadmap": ["Phase 1: Run helpful software learning meetups for local high schoolers.", "Phase 2: Organize student project sign-ups for open-source code setups.", "Phase 3: Act as the main voice bridging the tech group with real-world users.", "Phase 4: Lead your own high-level technology consulting agency team."],
                "projects": ["Design a Student Developer Collaboration Hub Platform", "Build a Cross-Team Code Project Progress Sync Dashboard"]
            },
            "Business": {
                "bonus": {"Marketing Manager": 10, "Product Manager": 9, "Entrepreneur": 7, "Business Analyst": 6},
                "roadmap": ["Phase 1: Design fun team-building workshops for new group members.", "Phase 2: Map out friendly public relationship announcements for student clubs.", "Phase 3: Run charity events to connect local stores with schools.", "Phase 4: Act as the main manager for popular public consumer brands."],
                "projects": ["Write a Friendly Team Member Onboarding System Manual", "Build a Charity Event Campaign Impact Tracker Sheet"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 7, "Medical Researcher": 6},
                "roadmap": ["Phase 1: Organize community informational flyers about basic health tips.", "Phase 2: Coordinate student support groups for kids dealing with heavy stress.", "Phase 3: Create medical communication modules that teach helpers to listen.", "Phase 4: Manage a complete public clinical health network system."],
                "projects": ["Create a Public Health Awareness Action Guide Book", "Build a Patient Advisory Network Tracking Layout Matrix"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 9, "Professor": 8},
                "roadmap": ["Phase 1: Lead your school's speech, debate, or presentation activities.", "Phase 2: Build a helpful older-to-younger student mentoring program.", "Phase 3: Run development workshops to help new tutors learn to teach.", "Phase 4: Serve as the principal head or president of a progressive school."],
                "projects": ["Design an Institutional School Mentoring Match Matrix", "Create a Tutor Training Checklist Progress Application"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 7, "Electrical Engineer": 6},
                "roadmap": ["Phase 1: Manage workflow harmony inside a busy high school robotics team.", "Phase 2: Run a presentation to gather neighborhood thoughts on a new park layout.", "Phase 3: Resolve schedule overlaps among field crews to prevent stress.", "Phase 4: Serve as the main relations director for massive engineering firms."],
                "projects": ["Create a Community Park Layout Feedback Collector", "Build a Multi-Crew Robotics Assignment Sync Center"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Marketing Manager": 9, "Graphic Designer": 6},
                "roadmap": ["Phase 1: Lead an active group of student artists on a combined mural project.", "Phase 2: Run community art creation workshops to teach illustration steps.", "Phase 3: Present design styles directly to school boards for event signs.", "Phase 4: Manage full creative content teams inside busy marketing firms."],
                "projects": ["Design a Multi-Artist Collaborative Art Workshop Plan", "Build a Creative Presentation Interface Layout for Clients"]
            }
        }
    },
    "ENFP": {
        "title": "The Motivator", "strengths": ["Full of enthusiasm", "Highly creative", "Excellent speaker", "Fun to be around"], "growth": ["Can be messy", "Says yes to too many tasks", "Gets restless quickly"],
        "questions": [
            "Does your brain constantly flash with tons of unexpected creative project ideas?",
            "Do you feel energized when juggling three different creative tasks at once?",
            "Do you love making friends with unusual, uniquely artistic individuals?",
            "Do you lose focus fast once a project gets into slow, repetitive steps?",
            "Do you prefer absolute personal freedom over strict corporate rules?"
        ],
        "universities": ["RISD", "CalArts", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Entrepreneur": 10, "Software Engineer": 7, "AI Engineer": 6},
                "roadmap": ["Phase 1: Design vibrant, animated web buttons and layouts using code.", "Phase 2: Build a fun online discussion space for sharing youth ideas.", "Phase 3: Enter high-energy tech hackathons and present your ideas visually.", "Phase 4: Consult on making app features highly entertaining for young consumers."],
                "projects": ["Design a Colorful Community Social App UI Concept", "Create a Visual Onboarding Flow for an Educational App"]
            },
            "Business": {
                "bonus": {"Marketing Manager": 10, "Entrepreneur": 9, "Product Manager": 7, "Business Analyst": 5},
                "roadmap": ["Phase 1: Launch viral social media challenges for a school event.", "Phase 2: Practice pitching a fun business concept to mock investors.", "Phase 3: Invent alternative ways to sell custom products directly to friends.", "Phase 4: Direct a high-energy startup hub space supporting new founders."],
                "projects": ["Build a Viral Social Media Marketing Campaign Guide", "Create a Direct-to-Consumer Custom Shop Startup Pitch"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 6, "Pharmacist": 5},
                "roadmap": ["Phase 1: Create colorful health guide comics for young children.", "Phase 2: Build simple, rewarding fitness milestone app mockups.", "Phase 3: Start interactive online support channels for young patients.", "Phase 4: Lead creative marketing styles for digital modern healthcare platforms."],
                "projects": ["Design a Gamified Mobile Fitness Goal Tracker App", "Build a Visual Patient Support Network Connection Concept"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 9, "Professor": 6},
                "roadmap": ["Phase 1: Create highly energetic, game-style flashcard tools for class.", "Phase 2: Host interactive study live streams for student clubs.", "Phase 3: Start non-traditional alternative study groups on digital message apps.", "Phase 4: Scale your own cool video-based learning channel for global kids."],
                "projects": ["Build an Animated Educational Card App Blueprint", "Design a High-Energy Student Engagement App Dashboard"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 7, "Civil Engineer": 5},
                "roadmap": ["Phase 1: Sketch wild, futuristic look concepts for consumer devices.", "Phase 2: Build simple device items using clean, recycled materials.", "Phase 3: Present friendly, ergonomic layout styles for heavy tools.", "Phase 4: Lead the fast invention team inside a manufacturing product shop."],
                "projects": ["Design an Ergonomic Student Computer Mouse Case CAD", "Build a Rapid-Invention Component Workshop Guide"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Graphic Designer": 9, "Animator": 8},
                "roadmap": ["Phase 1: Start your own experimental video channels online.", "Phase 2: Publish fun, animated storytelling video series for teens.", "Phase 3: Connect with independent digital artists to share graphic packs.", "Phase 4: Direct an entire collaborative digital entertainment creative house."],
                "projects": ["Create a Multi-Platform Interactive Video Interface Portfolio", "Build an Art Collaboration Content Delivery Network Guide"]
            }
        }
    },
    "ISTJ": {
        "title": "The Organizer", "strengths": ["Highly responsible", "Dutiful", "Orderly", "Very reliable"], "growth": ["Can be stubborn", "Sticks strictly to books", "Judges messy plans quickly"],
        "questions": [
            "Do you feel best when there are clear instructions and proven routines to follow?",
            "Do you take massive pride in being exactly on time and completely accurate?",
            "Do you prefer handling factual, proven numbers over guessing abstract ideas?",
            "Are you comfortable running predictable, structured, step-by-step tasks?",
            "Can people always count on you to turn your assignments in exactly when due?"
        ],
        "universities": ["MIT", "Carnegie Mellon", "NUST", "FAST"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Cybersecurity Specialist": 10, "Software Engineer": 8, "Data Scientist": 7, "AI Engineer": 5},
                "roadmap": ["Phase 1: Study official internet safety, protocol rules, and network codes.", "Phase 2: Set up automated test files to check code blocks for errors.", "Phase 3: Look through log files to spot broken entries or system leaks.", "Phase 4: Direct security compliance operations for institutional data banks."],
                "projects": ["Build an Automated Code Bug Tester Tool", "Write a Database Access Log Safety Checker Script"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 6, "Entrepreneur": 4},
                "roadmap": ["Phase 1: Learn operational accounting basics and small-business legal codes.", "Phase 2: Maintain clear, orderly inventory counting logs for a mock shop.", "Phase 3: Keep structured financial ledger record pages updated safely.", "Phase 4: Serve as the chief audit compliance officer for major corporations."],
                "projects": ["Create a Corporate Inventory Tracking Sheet System", "Build a Structured Business Risk Audit Metric Grid"]
            },
            "Healthcare": {
                "bonus": {"Pharmacist": 10, "Doctor": 7, "Medical Researcher": 6},
                "roadmap": ["Phase 1: Study safety codes regarding medication labeling rules.", "Phase 2: Maintain an exact, auditable medicine supply logbook.", "Phase 3: Review hospital research records to confirm formatting rules.", "Phase 4: Manage high-level historical health records data systems."],
                "projects": ["Build a Medicine Inventory Supply Log Tracker", "Design a Clinical Safety Compliance Log Check Tool"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Professor": 7, "Teacher": 6},
                "roadmap": ["Phase 1: Create orderly, fair spreadsheet calculators for grading scores.", "Phase 2: Run institutional study logs keeping student counts correct.", "Phase 3: Manage secure digital archiving for school report card files.", "Phase 4: Direct regional school board official qualification reviews."],
                "projects": ["Build a Standardized Class Grade Calculator Tool", "Design a Secure School Report Card Filing Framework"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Electrical Engineer": 8, "Mechanical Engineer": 7},
                "roadmap": ["Phase 1: Study regional construction safety codes and material guidelines.", "Phase 2: Run strict step-by-step circuit wiring checks on hardware pieces.", "Phase 3: Keep detailed maintenance logs for electrical gear machines.", "Phase 4: Serve as the primary quality control manager for a manufacturing center."],
                "projects": ["Create a Civil Structural Code Strain Verifier Sheet", "Design an Electronic Wiring Quality Checklist System"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Animator": 6, "Content Creator": 4},
                "roadmap": ["Phase 1: Sort thousands of design asset files into clear, named folders.", "Phase 2: Use version control trackers to keep project steps neatly archived.", "Phase 3: Check screen display colors against printed ink sheets for exact matching.", "Phase 4: Manage production schedules inside professional design firms."],
                "projects": ["Build an Art Asset Folder Version Control Grid", "Design a Media Resolution Color Output Tester Guide"]
            }
        }
    },
    "ISFJ": {
        "title": "The Protector", "strengths": ["Super supportive", "Dependable", "Observant", "Hardworking"], "growth": ["Too humble", "Takes on too much work", "Does not like unexpected shifts"],
        "questions": [
            "Do you prefer assisting behind the scenes to keep things calm and stable?",
            "Do you easily remember personal details, birthdays, and facts about friends?",
            "Do you find it hard to say no when peers ask you to do tasks for them?",
            "Are you highly motivated by a desire to be genuinely loyal and helpful to people?",
            "Do you feel best with a clear, predictable daily schedule?"
        ],
        "universities": ["Harvard", "Johns Hopkins", "Aga Khan University", "King Edward"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Cybersecurity Specialist": 7, "Data Scientist": 6},
                "roadmap": ["Phase 1: Learn how to design clean app setups that are clear for users.", "Phase 2: Maintain helpful error tracking logs for your computer science group.", "Phase 3: Build step-by-step user helper guides for everyday website pages.", "Phase 4: Handle data safety lists to keep personal user profiles secure."],
                "projects": ["Build an Internal Tech Support Ticket Dashboard", "Create a User Access Control Registration App Log"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Marketing Manager": 6, "Product Manager": 5},
                "roadmap": ["Phase 1: Handle notes, plans, and files neatly for your student project team.", "Phase 2: Keep orderly customer history charts for an imaginary shop.", "Phase 3: Track everyday supply counts across school offices safely.", "Phase 4: Direct team support and helpdesk divisions for large businesses."],
                "projects": ["Design a Secure Customer Record Archiving System", "Build an Office Resource Usage Tracking Tool Sheet"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 9, "Medical Researcher": 6},
                "roadmap": ["Phase 1: Practice checking basic clinical sign charts for patients.", "Phase 2: Track stock numbers for essential healthcare products cleanly.", "Phase 3: Keep highly structured patient medical history journals updated.", "Phase 4: Supervise administrative care and community clinic systems."],
                "projects": ["Build a Patient Medical History File Registry App", "Create a Pharmacy Supply Count Log Management Dashboard"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 8, "Professor": 5},
                "roadmap": ["Phase 1: Set up a clear daily homework logging chart for a classroom.", "Phase 2: Design friendly extra study guide packets for slow learners.", "Phase 3: Help track class attendance numbers to find kids who need help.", "Phase 4: Direct student care programs and daily support tasks at local schools."],
                "projects": ["Build a Classroom Assignment Organizer Interface", "Create a Student Attendance Status Monitor Tool"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Electrical Engineer": 7, "Mechanical Engineer": 6},
                "roadmap": ["Phase 1: Keep engineering diagram data files organized in order.", "Phase 2: Run a structural maintenance checklist loop for equipment parts.", "Phase 3: Watch instrument metrics to catch machine tiredness signs early.", "Phase 4: Supervise the everyday infrastructure maintenance crew inside a plant."],
                "projects": ["Design a Blueprint File Record Tracking Application", "Create a Structural Maintenance Milestone Verification Sheet"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Animator": 6, "Content Creator": 5},
                "roadmap": ["Phase 1: Apply small, specific layout edits from your art manager's notes.", "Phase 2: Create a deep vault of pre-made templates for company files.", "Phase 3: Catalog old artwork library sets so they are safe and clean.", "Phase 4: Review project visuals to ensure they match company quality rules."],
                "projects": ["Build a Corporate Graphic Template Storage Hub", "Design an Art Project Quality Sign-Off Checklist"]
            }
        }
    },
    "ESTJ": {
        "title": "The Manager", "strengths": ["Very dedicated", "Direct speaker", "Super organized", "Excellent administrator"], "growth": ["Not very flexible", "Dislikes unusual approaches", "Focuses too much on ranks"],
        "questions": [
            "Do you instantly create clear rules and task lists for messy groups?",
            "Do you value cold, unvarnished facts over theoretical or vague ideas?",
            "Do you find disorganized, chaotic workspaces deeply frustrating?",
            "Do you excel at coordinating timetables, tools, and delivery grids?",
            "Do you judge an assignment's success strictly by real past outcomes?"
        ],
        "universities": ["Stanford", "Wharton", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Cybersecurity Specialist": 9, "Data Scientist": 7},
                "roadmap": ["Phase 1: Build clear task priority boards for your programming group.", "Phase 2: Enforce precise rules for combining code blocks safely.", "Phase 3: Run quick sprint review timers for student code assignments.", "Phase 4: Command the primary operational IT architecture system for an enterprise."],
                "projects": ["Build a Code Approval Rules Enforcement Script", "Create a Team Programming Sprint Allocation Interface"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 8, "Marketing Manager": 7, "Entrepreneur": 6},
                "roadmap": ["Phase 1: Systematize sales operations funnel analytics steps.", "Phase 2: Create clear checklist target marks to review team progress fairly.", "Phase 3: Coordinate purchasing paths to buy assets for your project.", "Phase 4: Act as the Chief Operating Officer running market production flows."],
                "projects": ["Build a Sales Performance Pipeline Analyzer", "Create a Business Asset Procurement Lifecycle Tracker"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 8, "Medical Researcher": 5},
                "roadmap": ["Phase 1: Put clear hygiene rules and room guidelines into actions.", "Phase 2: Plan precise truck supply schedules for medical supply units.", "Phase 3: Manage daily work calendars for massive teams of clinic assistants.", "Phase 4: Direct total administrative operations for regional public hospitals."],
                "projects": ["Design a Clinical Protocol Safety Check Application", "Build a Hospital Staff Shift Scheduling Matrix Tool"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Teacher": 7, "Professor": 6},
                "roadmap": ["Phase 1: Put strong, organized school conduct rules into action plans.", "Phase 2: Direct secure exam delivery workflows to prevent cheating.", "Phase 3: Set up strict data reporting templates for class teachers.", "Phase 4: Preside as the administrative superintendent over school systems."],
                "projects": ["Design a School Exam Delivery Security Blueprint", "Build a Teacher Reporting Metric System App Interface"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 8, "Electrical Engineer": 7},
                "roadmap": ["Phase 1: Enforce clear, strict helmet and safety rule posters on a worksite.", "Phase 2: Track manufacturing output metrics against daily factory goals.", "Phase 3: Review equipment data logs to spot aging parts that need repairs.", "Phase 4: Serve as the lead plant director for giant production setups."],
                "projects": ["Build a Factory Assembly Line Output Tracking Sheet", "Design a Site Safety Protocol Compliance Verification Grid"]
            },
            "Creative Arts": {
                "bonus": {"Marketing Manager": 10, "Graphic Designer": 7, "Content Creator": 5},
                "roadmap": ["Phase 1: Set up strict delivery calendar goals for media designers.", "Phase 2: Coordinate work contracts across external printing centers.", "Phase 3: Keep direct billing and hours logs updated for studio clients.", "Phase 4: Manage the central project management office at major ad firms."],
                "projects": ["Create a Creative Studio Client Billing Monitor App", "Build a Graphic Design Printing Vendor Alignment Tracker"]
            }
        }
    },
    "ESFJ": {
        "title": "The Connector", "strengths": ["Loyal teammate", "Very social", "Warm personality", "Brings people together"], "growth": ["Worries about fitting in", "Dislikes sudden changes", "Sensitive to criticism"],
        "questions": [
            "Do you love planning group parties, games, or events for your classmates?",
            "Do you view helping with the practical needs of your friends as your job?",
            "Do you feel incredibly happy when your group functions in total harmony?",
            "Do you enjoy being noticed and appreciated for your community work?",
            "Are you skilled at calming arguments and helping friends get along?"
        ],
        "universities": ["LUMS", "IBA", "Stanford", "Harvard"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Product Manager": 8, "Cybersecurity Specialist": 5},
                "roadmap": ["Phase 1: Organize welcoming local student user group meetups for tech.", "Phase 2: Manage survey reviews from testing real student users on an app.", "Phase 3: Oversee customer help desks answering student software problems.", "Phase 4: Direct user onboarding support systems for software firms."],
                "projects": ["Build a Product Testing User Review Form Collector", "Create an App Technical Help Desk Response Interface"]
            },
            "Business": {
                "bonus": {"Marketing Manager": 10, "Product Manager": 8, "Business Analyst": 6, "Entrepreneur": 5},
                "roadmap": ["Phase 1: Run comprehensive event schedules for local student business fairs.", "Phase 2: Set up friendly communication portals to speak with project clients.", "Phase 3: Coordinate loyal user appreciation programs for local brands.", "Phase 4: Direct central customer experience setups at major consumer stores."],
                "projects": ["Design a Store Event Planning Framework Guide", "Build a Client Relations Communication Sync Portal Box"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 8, "Medical Researcher": 5},
                "roadmap": ["Phase 1: Help greet and settle arriving guests nicely at health centers.", "Phase 2: Manage welcoming information booths at student health camps.", "Phase 3: Help organize clinic scheduling tables to make visits relaxing.", "Phase 4: Serve as the main patient relations director for a clinical setup."],
                "projects": ["Create a Local Health Camp Event Activation Portal", "Build a Patient Care Feedback Collection Dashboard Hub"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 9, "Professor": 6},
                "roadmap": ["Phase 1: Set up open dialogue circles between parents and student mentors.", "Phase 2: Coordinate high school graduation parties and award panels.", "Phase 3: Manage helpful peer interaction files for school advisors.", "Phase 4: Lead community engagement programs across regional school groups."],
                "projects": ["Design a Parent-Teacher Council Communication Sheet System", "Build a Student Event Enrichment Registration Web Portal"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 7, "Electrical Engineer": 6},
                "roadmap": ["Phase 1: Plan morning safety summary talks for vocational work teams.", "Phase 2: Coordinate community surveys asking neighbors about a new bridge layout.", "Phase 3: Track crew scheduling logs to prevent shift overlap confusion.", "Phase 4: Lead public interaction and support branches for civil engineering firms."],
                "projects": ["Design a Building Project Morning Briefing Schedule", "Build a Community Land Impact Survey Review Sheet"]
            },
            "Creative Arts": {
                "bonus": {"Marketing Manager": 10, "Graphic Designer": 7, "Content Creator": 6},
                "roadmap": ["Phase 1: Manage welcoming team introductory calls for creative projects.", "Phase 2: Organize friendly local visual art showcases for student makers.", "Phase 3: Keep shared master calendars organized across creative teams.", "Phase 4: Lead client onboarding groups inside busy web design houses."],
                "projects": ["Design an Art Exhibition Event Schedule Tracker", "Build a Creative Studio Account Onboarding Interface Grid"]
            }
        }
    },
    "ISTP": {
        "title": "The Builder", "strengths": ["Hands-on helper", "Always optimistic", "Adapts quickly", "Calm in emergencies"], "growth": ["Very quiet", "Can overlook feelings", "Gets bored by theory lessons"],
        "questions": [
            "Do you learn best by taking apart, repairing, and building gadgets or code systems?",
            "Do you feel focused and ready when tools break down or unexpected tech glitches occur?",
            "Do you dislike micromanagement, rules, and endless paperwork?",
            "Do you always want to figure out how a machine operates under the hood?",
            "Do you value practical, useful tools much more than decorative styles?"
        ],
        "universities": ["MIT", "ETH Zurich", "NUST", "UET"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Cybersecurity Specialist": 10, "Software Engineer": 9, "AI Engineer": 6, "Data Scientist": 5},
                "roadmap": ["Phase 1: Master raw computer terminal inputs and router internet commands.", "Phase 2: Build swift, terminal-based tools to clean text data lists.", "Phase 3: Code scripts that act instantly to close broken background server ports.", "Phase 4: Lead immediate emergency digital security recovery teams."],
                "projects": ["Build a Command-Line Text Utility Tool Core", "Write a Server Threat Response Emergency Script Tool"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 6, "Entrepreneur": 5},
                "roadmap": ["Phase 1: Master database spreadsheet formulas and code scripts.", "Phase 2: Build a personal dashboard app to chart product purchase trends.", "Phase 3: Sift through raw transaction sheets to spot math inconsistencies.", "Phase 4: Direct operational data troubleshooting branches for data hubs."],
                "projects": ["Build a Spreadsheets Trend Visualization Dashboard", "Create a Transaction Balance Data Error Extractor Tool"]
            },
            "Healthcare": {
                "bonus": {"Pharmacist": 10, "Doctor": 7, "Medical Researcher": 6},
                "roadmap": ["Phase 1: Explore hardware wires inside modern biometric measuring items.", "Phase 2: Calibrate precision gears on clinical fluid tracking items.", "Phase 3: Fix background network wire errors for medical imaging rooms.", "Phase 4: Manage engineering support repairs inside critical trauma fields."],
                "projects": ["Design a Patient Sensor Calibration System Script", "Build a Medical Device Local Network Sync Core Module"]
            },
            "Education": {
                "bonus": {"Professor": 10, "Teacher": 7, "Education Consultant": 5},
                "roadmap": ["Phase 1: Construct manual wooden or wire block logic toys for young kids.", "Phase 2: Code your own lightweight computer program that auto-grades simple text files.", "Phase 3: Run interactive, physical training workshops inside computer lab spaces.", "Phase 4: Supervise real technical training setups at hardware trade programs."],
                "projects": ["Write an Automated Homework Grading Code script", "Build an Electronic Logic Block Learning Board Mockup"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 9, "Civil Engineer": 7},
                "roadmap": ["Phase 1: Write microcode programs for mechanical test engine meters.", "Phase 2: Connect real wires and chips on circuit testing rows by hand.", "Phase 3: Put structural alloys under heavy physical weight to record snap points.", "Phase 4: Direct urgent field repair work at broken hardware facilities."],
                "projects": ["Code an Embedded Machine Diagnostics Program File", "Build an Electronic Sensor Component Wiring Grid Board"]
            },
            "Creative Arts": {
                "bonus": {"Animator": 10, "Graphic Designer": 7, "Content Creator": 5},
                "roadmap": ["Phase 1: Master digital bone anchor rigs inside 3D software items.", "Phase 2: Write lightweight script utilities to chop up video frames fast.", "Phase 3: Put together physical camera stands and light mounts manually.", "Phase 4: Direct technical file compilation pipelines at video game studios."],
                "projects": ["Build a 3D Character Rig Bone Skeletal Matrix", "Write a Video Frame Filter Processing Pipeline Script"]
            }
        }
    },
    "ISFP": {
        "title": "The Artist", "strengths": ["Deeply creative", "Highly imaginative", "True passion", "Very curious"], "growth": ["Extremely private", "Hard to predict", "Stresses out easily"],
        "questions": [
            "Do you see your workspace as a clean blank page to show your style?",
            "Do you prefer following unexpected creative ideas rather than checking timeline plans?",
            "Do you feel trapped and tired when locked into heavy math tables?",
            "Is visual color harmony and beautiful styling a massive goal for you?",
            "Do you require complete independence over when and how you build your art?"
        ],
        "universities": ["RISD", "CalArts", "NCA", "AIVA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "AI Engineer": 6, "Data Scientist": 5},
                "roadmap": ["Phase 1: Study beautiful CSS style formatting codes and graphic design themes.", "Phase 2: Build pixel-perfect visual website sample page views on your laptop.", "Phase 3: Design a portfolio of custom app icon drawings and vector packs.", "Phase 4: Serve as the central creative look designer for client app interfaces."],
                "projects": ["Design a Beautiful Web App CSS Visual Theme System", "Build a Gorgeous Front-Page User Experience Mockup UI"]
            },
            "Business": {
                "bonus": {"Marketing Manager": 10, "Product Manager": 6, "Business Analyst": 4},
                "roadmap": ["Phase 1: Discover how trendy, minimalist brand logos are created.", "Phase 2: Create beautiful boxes and custom wrappers for a luxury store idea.", "Phase 3: Build elegant product shelf displays for a mockup storefront row.", "Phase 4: Consult on look themes for active corporate media campaigns."],
                "projects": ["Create a Boutique Store Brand Visual Identity Manual", "Design a Creative Commercial Box Packaging Layout System"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 6, "Pharmacist": 4},
                "roadmap": ["Phase 1: Practice drawing accurate, detailed scientific human anatomy shapes.", "Phase 2: Select beautiful, relaxing wall color tones for a kids' clinic sketch.", "Phase 3: Create colorful study flashcards for learning medical cell names.", "Phase 4: Consult on sensory lighting layout patterns for quiet health rooms."],
                "projects": ["Build a Human Anatomy Study Flashcard Graphic Deck", "Design a Pediatric Care Clinic Room Color Theme Sketch"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 7, "Professor": 5},
                "roadmap": ["Phase 1: Draw high-quality, friendly cartoon pages for basic school books.", "Phase 2: Organize clean, colored formatting layouts for online school boards.", "Phase 3: Build hands-on, touch-based crafts tutorials for student activities.", "Phase 4: Handle artistic layout choices for educational smartphone apps."],
                "projects": ["Design an Illustrated Primary Textbook Page Layout Grid", "Create a Tactile Art Craft Project Lesson Worksheet Book"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Civil Engineer": 7, "Electrical Engineer": 6},
                "roadmap": ["Phase 1: Draft smooth, organic protective outer plastic sheets for gadgets.", "Phase 2: Model beautiful 3D digital home views using architectural packages.", "Phase 3: Construct comfortable, smooth model bodies for handmade consumer products.", "Phase 4: Direct outer look styling choices inside major device testing rooms."],
                "projects": ["Design an Organic Product Outer Case Shell using CAD", "Build a 3D Architectural Home Spatial Layout Concept Rig"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Animator": 9, "Content Creator": 8},
                "roadmap": ["Phase 1: Create beautiful original painting canvases using a drawing tablet.", "Phase 2: Build high-quality vector scenes showing wonderful landscapes.", "Phase 3: Write your own original style booklet exploring clean font pairs.", "Phase 4: Launch your own high-end online fine arts studio shop showing your pieces."],
                "projects": ["Paint a Rich Immersive Digital Landscape Canvas Layout", "Design a Bespoke Typography Font Pair System Style Book"]
            }
        }
    },
    "ESTP": {
        "title": "The Doer", "strengths": ["Bold actions", "Direct speaker", "Very realistic", "Focused on results"], "growth": ["Loses patience easily", "Takes reckless risks", "Misses long-term trends"],
        "questions": [
            "Do you enjoy taking quick, calculated risks to win competitions?",
            "Do you feel most awake in hyper-fast settings where things shift instantly?",
            "Do you prefer jumping into direct tests over reading long instruction manuals?",
            "Are you highly persuasive when speaking with people to make quick group choices?",
            "Do you lose total motivation when stuck listening to abstract whiteboard history?"
        ],
        "universities": ["Stanford", "Wharton", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Cybersecurity Specialist": 8, "AI Engineer": 7},
                "roadmap": ["Phase 1: Run crash load tests on servers to see when they break down.", "Phase 2: Turn off malfunctioning software blocks instantly inside code rows.", "Phase 3: Build simple, fast mobile checklist tracker apps for field teams.", "Phase 4: Command real-time systems emergency tech restoration squads."],
                "projects": ["Build a Server Traffic Crash Load Generator Tool", "Create a Fast-Track Mobile Field Asset Logging App Module"]
            },
            "Business": {
                "bonus": {"Entrepreneur": 10, "Marketing Manager": 9, "Product Manager": 8, "Business Analyst": 6},
                "roadmap": ["Phase 1: Negotiate deals directly with student event organizers.", "Phase 2: Pitch a fast project concept to grab seed money slots.", "Phase 3: Shift store strategies instantly to sell product stocks out fast.", "Phase 4: Run your own disruptive startup lab building trendy ventures."],
                "projects": ["Create a Live Sales Deal Flow Milestone Tracker", "Build a Startup Pivot Conversion Strategy Metrics App"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 7, "Medical Researcher": 5},
                "roadmap": ["Phase 1: Train in high-velocity emergency room triage operations.", "Phase 2: Manage urgent traffic flows sorting patients arriving in a crisis.", "Phase 3: Pick fast equipment choices for emergency care transport boxes.", "Phase 4: Lead high-pressure rapid response medical crew lines dynamically."],
                "projects": ["Write an Emergency Triage Patient Sorting Logic Manual", "Design a Rapid-Response Medical Transport Case Equipment Layout Matrix"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Teacher": 7, "Professor": 5},
                "roadmap": ["Phase 1: Build high-energy outdoor team problem-solving camps.", "Phase 2: Design swift hands-on trade skills building courses.", "Phase 3: Host fast-paced live panel quiz challenge nights for peers.", "Phase 4: Lead corporate fast-track professional career bootcamps."],
                "projects": ["Build an Action-Oriented Trade Course Mobile App Prototype", "Design a High-Energy Problem Solving Field Camp Schedule"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 8, "Civil Engineer": 7},
                "roadmap": ["Phase 1: Adjust motor limits on model racing engine frames.", "Phase 2: Fix heavy tool issues directly on active field floors.", "Phase 3: Connect thick wire connections safely for heavy power boxes.", "Phase 4: Lead critical engineering response crews inside active facilities."],
                "projects": ["Build a Model Racing Motor Performance Tuning Tool", "Create a High-Voltage Circuit Connection Box Model Layout"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Marketing Manager": 9, "Graphic Designer": 6},
                "roadmap": ["Phase 1: Run quick, eye-catching surprise pop-up art show events.", "Phase 2: Design energetic guerrilla advertising ideas for school games.", "Phase 3: Run live video switching decks for action-packed media channels.", "Phase 4: Command high-growth creative activation crews for major media houses."],
                "projects": ["Design a Guerrilla Marketing Campaign Activation Playbook", "Build a Live Media Production Panel System Console Board"]
            }
        }
    },
    "ESFP": {
        "title": "The Performer", "strengths": ["Bold spirit", "Original style", "Very practical", "Wonderful people skills"], "growth": ["Gets bored instantly", "Weak long-term planning", "Loses focus easily"],
        "questions": [
            "Do you naturally lift up the energy and excitement of your full friend circle?",
            "Do you find creative group workshops highly empowering and fun?",
            "Do you look at the entire world as an open stage to make memories?",
            "Do you prioritize immediate fun and action over long-term tracking routines?",
            "Are you exceptionally skilled at styling visuals for high user engagement?"
        ],
        "universities": ["CalArts", "RISD", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Software Engineer": 10, "Product Manager": 7, "AI Engineer": 6},
                "roadmap": ["Phase 1: Learn how to code smooth canvas frame color changes and animations.", "Phase 2: Design custom, colorful button screens for gaming software pages.", "Phase 3: Present feature announcements live at school technology showcases.", "Phase 4: Consult on making app features highly entertaining for young consumers."],
                "projects": ["Code an Animated Web Canvas Graphic Visual Module", "Design a Colorful Mobile Game User Interface Layout Prototype"]
            },
            "Business": {
                "bonus": {"Marketing Manager": 10, "Entrepreneur": 8, "Product Manager": 8, "Business Analyst": 5},
                "roadmap": ["Phase 1: Host spectacular celebration launches for student products.", "Phase 2: Put together beautiful video pitch reels using energetic styles.", "Phase 3: Connect with micro-influencers to showcase a startup brand.", "Phase 4: Serve as the primary lifestyle creative head for modern stores."],
                "projects": ["Write a Brand Product Launch Party Activation Playbook", "Create a High-Impact Video Ad Campaign Storyboard Layout Deck"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Pharmacist": 6, "Medical Researcher": 5},
                "roadmap": ["Phase 1: Run happy, active exercise games for pediatric patient groups.", "Phase 2: Launch bright, animated digital flyers teaching health rules.", "Phase 3: Coordinate active group encouragement workouts for clinic visitors.", "Phase 4: Manage friendly media and public communication lines for healthcare hubs."],
                "projects": ["Design a Pediatric Patient Activity Schedule Application", "Create a Digital Health Information Social Media Asset Layout Grid"]
            },
            "Education": {
                "bonus": {"Teacher": 10, "Education Consultant": 9, "Professor": 6},
                "roadmap": ["Phase 1: Write interactive, theater-style educational acting play sheets.", "Phase 2: Host massive student academic challenge award show stages.", "Phase 3: Publish highly animated history or math summary clips online.", "Phase 4: Direct progressive, video-first edutainment study platform hubs."],
                "projects": ["Write an Interactive Classroom Drama Lesson Playbook", "Create a Fun Educational Video Segment Media Portfolio Asset"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Civil Engineer": 6, "Electrical Engineer": 6},
                "roadmap": ["Phase 1: Design glossy, high-style outer plastic layers for consumer devices.", "Phase 2: Sketch out immersive theme park ride entry structures using 3D layouts.", "Phase 3: Put together stylish conceptual car body model layouts using modeling tools.", "Phase 4: Lead live device performance showcase groups at trade shows."],
                "projects": ["Design a Theme Park Immersive Attraction Concept Model Layout", "Build an Electronic Device Enclosure CAD Design Case Study"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Graphic Designer": 9, "Animator": 8},
                "roadmap": ["Phase 1: Produce high-fidelity interactive media channel grids", "Phase 2: Orchestrate spectacular dynamic lighting visual sets", "Phase 3: Direct large-scale digital video cast production sets", "Phase 4: Command major contemporary digital entertainment studio houses"],
                "projects": ["Interactive Media Grid Video Production Array", "Dynamic Lighting Stage Visual Set Architecture"]
            }
        }
    }
}

# Static Academic-Career Knowledge Graphs
PATHWAYS = {
    "Technology": {
        "careers": {"AI Engineer": 82, "Software Engineer": 78, "Data Scientist": 75, "Cybersecurity Specialist": 72},
        "dream": ["MIT", "Stanford"], "strong": ["NUST", "FAST"], "affordable": ["COMSATS", "Air University"],
        "skills": ["Coding with Python", "Using Git Version Control", "Sorting Data Structures", "Understanding Machine Learning"],
        "resources": ["CS50 — Learn computer science foundations from Harvard University.", "freeCodeCamp — Practice coding with free interactive lessons and projects.", "Kaggle — Work on fun data puzzles and test out machine learning models.", "Andrew Ng Courses — Follow super simple video guides to understand AI secrets."],
        "projects": ["AI Career Assistant", "Personal Expense Calculator App", "Digital Homework Study Planner"],
        "opportunities": ["Weekend Hackathons", "School Coding Challenges"]
    },
    "Business": {
        "careers": {"Entrepreneur": 85, "Product Manager": 80, "Business Analyst": 74, "Marketing Manager": 70},
        "dream": ["Stanford", "Wharton"], "strong": ["LUMS", "IBA"], "affordable": ["COMSATS", "IQRA"],
        "skills": ["Team Leadership", "Brand Marketing", "Public Speaking", "Money Management"],
        "resources": ["Y Combinator Startup School — Learn how to pitch and launch your own company from tech leaders.", "HubSpot Academy — Take free certificates to learn digital social media marketing.", "Coursera Business — Discover how global markets and business managers think."],
        "projects": ["Startup Venture Idea Validator Tool", "Mini Shop Strategy Business Planner"],
        "opportunities": ["Startup Creation Weekends", "Youth Business Pitch Contests"]
    },
    "Healthcare": {
        "careers": {"Doctor": 88, "Medical Researcher": 82, "Pharmacist": 71},
        "dream": ["Harvard", "Johns Hopkins"], "strong": ["Aga Khan University", "King Edward"], "affordable": ["Public Medical Colleges"],
        "skills": ["Human Biology basics", "Scientific Lab Research", "Empathetic Patient Communication"],
        "resources": ["Khan Academy Health — Discover clear videos on anatomy and human cell operations.", "PubMed Archive — Read real scientific studies on medicine advances.", "Coursera Health — Learn simple definitions of medicine terms used by real clinics."],
        "projects": ["Daily Nutrition Tracker Sheet", "Clean Family Medical Information Website Portal"],
        "opportunities": ["Science Knowledge Olympiads", "Community Clinic Awareness Drives"]
    },
    "Education": {
        "careers": {"Teacher": 80, "Professor": 78, "Education Consultant": 71},
        "dream": ["Harvard", "Oxford"], "strong": ["LUMS", "NUST"], "affordable": ["Public Universities"],
        "skills": ["Teaching Techniques", "Confident Public Speaking", "Lesson and Quiz Design"],
        "resources": ["Coursera Education — Learn how professional teachers design fun workshops.", "edX Learning — Review courses on how text rules are explained to students.", "Teaching Channel — Watch videos of teachers using creative games in modern school spaces."],
        "projects": ["Gamified Revision Quiz App", "Mini Classroom Learning Management Portal"],
        "opportunities": ["Student Teaching Workshops", "Free Community Peer Tutoring Groups"]
    },
    "Engineering": {
        "careers": {"Mechanical Engineer": 80, "Electrical Engineer": 82, "Civil Engineer": 73},
        "dream": ["MIT", "Stanford"], "strong": ["NUST", "UET"], "affordable": ["COMSATS", "Air University"],
        "skills": ["Physics Rules", "Mathematics formulas", "3D CAD Modeling software", "Design Problem Solving"],
        "resources": ["MIT OpenCourseWare — Download free lecture notebooks from top college math courses.", "Khan Academy Physics — Review simple video modules to understand force rules.", "Engineering Explained — Watch animations showing how sports cars and engines operate."],
        "projects": ["Smart Traffic Flow Matrix Simulator", "IoT Home Sensor Asset Collector Tracker"],
        "opportunities": ["Robotics Engineering Competitions", "Science and Design Invention Fairs"]
    },
    "Creative Arts": {
        "careers": {"Graphic Designer": 85, "Animator": 80, "Content Creator": 78},
        "dream": ["RISD", "CalArts"], "strong": ["NCA", "AIVA"], "affordable": ["Local Design Institutes"],
        "skills": ["User Experience UI Design", "Visual Graphic Storytelling", "Adobe Creative Suite Software"],
        "resources": ["Canva Design School — Learn simple layout rules and color matching basics.", "Figma Learn — Follow free step-by-step guides to design clean user interfaces.", "Behance Showcase — Look at portfolios of master artists to gain creative ideas."],
        "projects": ["Interactive Portfolio Web Page Mock", "3D Moving Typography Design Frame Deck"],
        "opportunities": ["Logo Creation Design Contests", "Youth Art and Drawing Exhibitions"]
    }
}

# ==============================================================================
# LEFT SIDE NAVIGATION PANEL (Collapsible Sidebar Navigation Blueprint)
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color: #111827; margin-bottom: 4px; font-weight:700;'>HELP AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B7280; font-size:12px; margin-bottom:24px;'>Higher Education Learning Path</p>", unsafe_allow_html=True)
    
    st.markdown("### Navigation")
    nav_selection = st.radio(
        "Go to page:",
        ["Home Dashboard", "Profile Setup Assessment", "Personalized Report Card", "My Learning Plan Timeline", "Resource Explorer"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("<p style='color: #9CA3AF; font-size:11px;'>HELP AI Platform v2.0<br/>Premium EdTech Engine</p>", unsafe_allow_html=True)

# Synchronize Sidebar options with existing session state state-machines smoothly
if "app_mode" not in st.session_state:
    st.session_state.app_mode = "Home"

if nav_selection == "Home Dashboard":
    st.session_state.app_mode = "Home"
elif nav_selection == "Profile Setup Assessment":
    st.session_state.app_mode = "Assessment"
elif nav_selection == "Personalized Report Card":
    st.session_state.app_mode = "Report"
elif nav_selection == "My Learning Plan Timeline":
    st.session_state.app_mode = "Timeline"
elif nav_selection == "Resource Explorer":
    st.session_state.app_mode = "Resources"

# Initialize global workflow markers securely
if "wizard_active" not in st.session_state:
    st.session_state.wizard_active = False

# ==============================================================================
# VIEW ROUTER NODE: MODE 1 — STARTUP PRODUCT LANDING HERO PAGE
# ==============================================================================
if st.session_state.app_mode == "Home" and not st.session_state.wizard_active and not st.session_state.report_generated:
    st.markdown("<div style='text-align: center; padding: 60px 0 20px 0;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 52px; font-weight: 800; color: #111827; letter-spacing: -0.03em; margin-bottom: 8px;'>Discover Your True Path Forward</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px; color: #4F8EF7; font-weight: 500; margin-bottom: 24px;'>Higher Education Learning Path AI</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 16px; color: #6B7280; max-width: 600px; margin: 0 auto 40px auto; line-height: 1.6;'>HELP AI maps your high school profile choices, custom skills balance points, and optional personality structures directly to personalized career metrics dashboards, timeline roadmaps, and college tiers.</p>", unsafe_allow_html=True)
    
    col_btn_center, _ = st.columns([1, 1])
    with col_btn_center:
        if st.button("Start My Assessment →", use_container_width=True):
            st.session_state.wizard_active = True
            st.rerun()
            
    st.markdown("<p style='font-size: 13px; color: #9CA3AF; margin-top: 12px; margin-bottom: 60px;'>Takes less than 4 minutes • Rules-Based Intelligence Engine Enabled</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #9CA3AF; font-size: 12px; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 24px;'>Trusted by builders at modern schools</p>", unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    with col_f1: st.markdown("<p style='text-align: center; color: #6B7280; font-weight: 600;'>O-Level Hubs</p>", unsafe_allow_html=True)
    with col_f2: st.markdown("<p style='text-align: center; color: #6B7280; font-weight: 600;'>A-Level tracks</p>", unsafe_allow_html=True)
    with col_f3: st.markdown("<p style='text-align: center; color: #6B7280; font-weight: 600;'>FSc Colleges</p>", unsafe_allow_html=True)
    with col_f4: st.markdown("<p style='text-align: center; color: #6B7280; font-weight: 600;'>Matric Platforms</p>", unsafe_allow_html=True)

# ==============================================================================
# VIEW ROUTER NODE: MODE 2 — MULTI-STEP ASSESSMENT WIZARD MODULE
# ==============================================================================
elif st.session_state.wizard_active or st.session_state.app_mode == "Assessment" if not st.session_state.report_generated else False:
    st.markdown("<h2 style='font-weight:700; letter-spacing:-0.02em;'>Profile Assessment Engine</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #6B7280;'>Step {st.session_state.step} of 4</p>", unsafe_allow_html=True)
    
    # Modern horizontal segmented line layout progress tracker
    progress_bar_html = "".join([
        f"<div style='flex: 1; height: 4px; background-color: {'#4F8EF7' if i+1 <= st.session_state.step else '#E5E7EB'}; margin-right: 4px; border-radius: 2px;'></div>"
        for i in range(4)
    ])
    st.markdown(f"<div style='display: flex; width: 100%; margin-bottom: 32px;'>{progress_bar_html}</div>", unsafe_allow_html=True)

    if "step" not in st.session_state:
        st.session_state.step = 1

    # Step 1: Base Core Metrics Card Layout
    if st.session_state.step == 1:
        with st.container(border=True):
            st.markdown("<h4 style='font-weight:600; margin-bottom:16px;'>School Foundations</h4>", unsafe_allow_html=True)
            grade = st.selectbox("What is your current school tier?", ["O-Level", "A-Level", "FSc", "Matric", "Other"], index=0)
            interest = st.selectbox("Pick an industry that sounds exciting to you:", list(PATHWAYS.keys()), index=0)
            goal = st.text_input("What is your dream future goal? (e.g., Build a creative app, Cure illness, Run a cool shop)")
        
        if st.button("Continue", use_container_width=True):
            if goal.strip() == "":
                st.warning("Please share a quick dream target goal to start your learning path planner.")
            else:
                st.session_state.grade = grade
                st.session_state.interest = interest
                st.session_state.goal = goal
                st.session_state.step = 2
                st.rerun()

    # Step 2: Traits & Selection Grid
    elif st.session_state.step == 2:
        with st.container(border=True):
            st.markdown("<h4 style='font-weight:600; margin-bottom:16px;'>Skills & Core Strengths Checklist</h4>", unsafe_allow_html=True)
            subjects = st.multiselect("Pick your favorite subjects to study:", ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Business", "Economics", "Art"], default=["Computer Science", "Mathematics"])
            strengths = st.multiselect("Superpowers (What are you naturally great at?):", ["Problem Solving", "Creativity", "Leadership", "Communication", "Analytical Thinking", "Teamwork"], default=["Problem Solving"])
            weaknesses = st.multiselect("Growth Areas (What skills would you like to build up?):", ["Programming", "Public Speaking", "Mathematics", "Time Management", "Confidence", "Writing"], default=["Time Management"])
            activities = st.multiselect("What high-energy projects sound fun to try?", ["Coding", "Building Projects", "Research", "Reading", "Business", "Teaching", "Designing"], default=["Building Projects"])
            
            leadership_raw = st.radio("Do you enjoy leading teams and guiding group assignments?", ["I love it!", "I'm open to it sometimes.", "I prefer executing solo tasks."])
            st.session_state.leadership = "Yes" if "love" in leadership_raw else ("sometimes" in leadership_raw and "Sometimes" or "No")
        
        col_back, col_next = st.columns(2)
        with col_back:
            if st.button("Back", use_container_width=True):
                st.session_state.step = 1
                st.rerun()
        with col_next:
            if st.button("Continue", use_container_width=True):
                st.session_state.subjects = subjects
                st.session_state.strengths = strengths
                st.session_state.weaknesses = weaknesses
                st.session_state.activities = activities
                st.session_state.step = 3
                st.rerun()

    # Step 3: Personality Route Branch Selection
    elif st.session_state.step == 3:
        with st.container(border=True):
            st.markdown("<h4 style='font-weight:600; margin-bottom:16px;'>Personality Tracker Activation</h4>", unsafe_allow_html=True)
            st.write("Let's activate your behavioral style evaluation tool to discover your mentoring track adjustments.")
            
            p_route = st.radio("How would you like to set up your personality module?", [
                "Option A: I already know my four-letter personality type signature.",
                "Option B: I don't know my type (Take our quick mini student quiz)."
            ])
            st.session_state.p_route = "A" if "Option A" in p_route else "B"
            
        col_back, col_next = st.columns(2)
        with col_back:
            if st.button("Back", use_container_width=True):
                st.session_state.step = 2
                st.rerun()
        with col_next:
            if st.button("Initialize Module", use_container_width=True):
                st.session_state.step = 4
                st.rerun()

    # Step 4: Personality Engine Scoring Arrays Validation Nodes
    elif st.session_state.step == 4:
        if st.session_state.p_route == "A":
            with st.container(border=True):
                st.markdown("<h4 style='font-weight:600; margin-bottom:16px;'>Personality Type Input Verification</h4>", unsafe_allow_html=True)
                selected_type = st.selectbox("Pick your four-letter personality signature:", list(PERSONALITY_REGISTRY.keys()))
                
                st.markdown(f"##### Quick Verification Checks for the {selected_type} Profile")
                st.caption("Slide these toggles to match how you feel on a level from 1 to 10:")
                
                q_list = PERSONALITY_REGISTRY[selected_type]["questions"]
                
                st.slider(f"1. {q_list[0]}", 1, 10, 5, key="p_q1")
                st.slider(f"2. {q_list[1]}", 1, 10, 5, key="p_q2")
                st.slider(f"3. {q_list[2]}", 1, 10, 5, key="p_q3")
                st.slider(f"4. {q_list[3]}", 1, 10, 5, key="p_q4")
                st.slider(f"5. {q_list[4]}", 1, 10, 5, key="p_q5")
                
            col_back, col_submit = st.columns(2)
            with col_back:
                if st.button("Change Route", use_container_width=True):
                    st.session_state.step = 3
                    st.rerun()
            with col_submit:
                if st.button("Generate My AI Career Report", type="primary", use_container_width=True):
                    st.session_state.selected_personality = selected_type
                    st.session_state.p_confidence = 100
                    st.session_state.p_rationale = "We processed your self-reported profile signature and loaded your customized student data settings safely."
                    st.session_state.report_generated = True
                    st.session_state.wizard_active = False
                    st.session_state.app_mode = "Report"
                    st.rerun()

        else:
            with st.container(border=True):
                st.markdown("<h4 style='font-weight:600; margin-bottom:16px;'>Student Trait Questionnaire Dashboard</h4>", unsafe_allow_html=True)
                st.caption("Answer these questions naturally based on how you usually think, study, and behave.")
                
                st.markdown("**Section 1: How do you recharge your batteries?**")
                ie1 = st.radio("Q1: After a long, busy week at school, what sounds most relaxing?", ["Spending quiet time alone to focus on independent hobbies", "Hanging out with groups of friends and joining social networks"])
                ie2 = st.radio("Q2: When building a class project challenge, what role sounds best?", ["Thinking quietly by myself to outline concepts first", "Sharing ideas instantly inside an open group circle"])
                ie3 = st.radio("Q3: When arriving at a huge student event filled with new faces, you usually:", ["Observe from a safe distance before introducing yourself", "Jump right into the crowd to start conversations instantly"])
                
                st.markdown("**Section 2: How do you look at data?**")
                sn1 = st.radio("Q4: When processing a data spreadsheet report or project brief, you look for:", ["Real-world observable facts, figures, and true metrics", "Abstract conceptual ideas, future strategies, and macro patterns"])
                sn2 = st.radio("Q5: If learning an advanced technology infrastructure track, you favor:", ["Clear real-world execution recipes and simple functional code blocks", "First-principles engineering architecture books and structural blueprints"])
                sn3 = st.radio("Q6: Your classmates appreciate your study work vectors primarily because you are:", ["Grounded, practical, and highly reliable at getting tasks completed", "Unconventional, creative, and full of imaginative future options"])
                
                st.markdown("**Section 3: How do you make tough choices?**")
                tf1 = st.radio("Q7: When sorting out a major bottleneck or team argument, you anchor on:", ["Cold objective logic structures, data rules, and factual logs", "Human alignment variables, group kindness, and community feelings"])
                tf2 = st.radio("Q8: If giving feedback on a partner's project assignment, you prioritize:", ["Direct, completely unvarnished error diagnostic truth", "Constructive, warm, empathetic coaching cycles and friendly loops"])
                tf3 = st.radio("Q9: You feel highly motivated to finish tough assignments because you want:", ["Elite technical performance scores and structural perfection wins", "Authentic personal validation and a deep alignment with your values"])
                
                st.markdown("**Section 4: How do you handle school deadlines?**")
                jp1 = st.radio("Q10: Your personal school calendar and agenda tracker is handled via:", ["Strict predictive block planning schedules and preset milestones", "Dynamic fluid adjustments based on immediate runtime priorities"])
                jp2 = st.radio("Q11: When starting long-term technical project deployments, you:", ["Map all modular sub-component paths out neatly beforehand", "Jump right into creating layouts and editing functional code blocks"])
                jp3 = st.radio("Q12: System deadlines make you feel most optimized when they are:", ["Vetted target milestones tracked well ahead of the final stop", "Urgent high-stakes catalysts forcing fast creation steps at the tail end"])

            col_back, col_submit = st.columns(2)
            with col_back:
                if st.button("Change Route", use_container_width=True):
                    st.session_state.step = 3
                    st.rerun()
            with col_submit:
                if st.button("Generate My AI Career Report", type="primary", use_container_width=True):
                    i_score = sum([1 for x in [ie1, ie2, ie3] if "alone" in x or "solo" in x or "Observe" in x])
                    n_score = sum([1 for x in [sn1, sn2, sn3] if "abstract" in x or "architecture" in x or "innovative" in x])
                    t_score = sum([1 for x in [tf1, tf2, tf3] if "logic" in x or "unvarnished" in x or "performance" in x])
                    j_score = sum([1 for x in [jp1, jp2, jp3] if "predictive" in x or "Map" in x or "Vetted" in x])
                    
                    computed_type = f"{'I' if i_score >= 2 else 'E'}{'N' if n_score >= 2 else 'S'}{'T' if t_score >= 2 else 'F'}{'J' if j_score >= 2 else 'P'}"
                    
                    vec_max = max(i_score, 3-i_score) + max(n_score, 3-n_score) + max(t_score, 3-t_score) + max(j_score, 3-j_score)
                    st.session_state.p_confidence = int((vec_max / 12) * 100)
                    st.session_state.selected_personality = computed_type
                    st.session_state.p_rationale = f"Your traits mapped perfectly. Our math tracking shows your preferences align closely with the {'Introverted' if 'I' in computed_type else 'Extraverted'} {'Intuitive' if 'N' in computed_type else 'Observant'} student profile group rules."
                    st.session_state.report_generated = True
                    st.session_state.wizard_active = False
                    st.session_state.app_mode = "Report"
                    st.rerun()

# ==============================================================================
# VIEW ROUTER NODE: REAL-TIME ANALYTICAL REPORTS & DATA DASHBOARDS
# ==============================================================================
else:
    # Safe checks if user visits reports tabs via sidebar navigation panel before finishing inputs quiz
    if not st.session_state.report_generated:
        st.warning("Please complete the Profile Assessment questionnaire tool first to compile analytics logs context.")
        if st.button("Go to Assessment Wizard"):
            st.session_state.wizard_active = True
            st.rerun()
    else:
        # Load scoring engine variables from datasets without modifying formula scales
        interest_data = PATHWAYS[st.session_state.interest]
        career_base_scores = interest_data["careers"].copy()
        p_code = st.session_state.selected_personality
        p_meta = PERSONALITY_REGISTRY[p_code]
        p_diverse = p_meta["diversity_map"][st.session_state.interest]

        integrated_scores = {}
        for c, base in career_base_scores.items():
            integrated_scores[c] = base

        if "Problem Solving" in st.session_state.strengths:
            for c in integrated_scores: integrated_scores[c] += 5
        if "Analytical Thinking" in st.session_state.strengths:
            for c in integrated_scores: integrated_scores[c] += 4
        if st.session_state.leadership == "Yes":
            for c in integrated_scores: integrated_scores[c] += 6

        p_bonus_map = p_diverse["bonus"]
        for c in integrated_scores:
            if c in p_bonus_map:
                integrated_scores[c] += p_bonus_map[c]

        final_ranked_careers = sorted(integrated_scores.items(), key=lambda x: x[1], reverse=True)
        top_career, top_score = final_ranked_careers[0][0], final_ranked_careers[0][1]

        raw_dream_unis = interest_data["dream"]
        raw_strong_unis = interest_data["strong"]
        p_preferred_unis = p_meta["universities"]

        modified_dream = list(dict.fromkeys(p_preferred_unis + raw_dream_unis))
        modified_strong = list(dict.fromkeys(raw_strong_unis))

        readiness_score = min(40 + (len(st.session_state.strengths) * 8) + (len(st.session_state.activities) * 5), 100)
        workspace_tier = "Explorer Level 1" if readiness_score < 60 else ("Builder Level 2" if readiness_score < 80 else "Specialist Level 3")

        # ----------------------------------------------------------------------
        # MODE 3A: MAIN PERSONALIZED MATRICES TAB
        # ----------------------------------------------------------------------
        if st.session_state.app_mode == "Report":
            st.markdown("<h2 style='font-weight:700; letter-spacing:-0.02em;'>Personalized Career Matrix</h2>", unsafe_allow_html=True)
            
            # Premium Bento Top Executive Hero Layout Cards Row
            col_b1, col_b2, col_b3 = st.columns(3)
            with col_b1:
                st.metric("Primary Match Vector", top_career)
            with col_b2:
                st.metric("Match Index Rating", f"{top_score}%")
            with col_b3:
                st.metric("Workspace Platform Status", workspace_tier)
                
            st.markdown("<br/>", unsafe_allow_html=True)
            
            col_dash1, col_dash2 = st.columns([1, 1])
            with col_dash1:
                with st.container(border=True):
                    st.markdown("<h4 style='font-weight:600; margin-bottom:16px;'>Top Industry Matches</h4>", unsafe_allow_html=True)
                    for career, score in final_ranked_careers[:3]:
                        st.markdown(f"**{career}** • Match Level `{score}%`")
                        st.progress(min(score, 100) / 100)
                        st.markdown("<div style='margin-bottom:12px;'></div>", unsafe_allow_html=True)
                        
            with col_dash2:
                with st.container(border=True):
                    st.markdown("<h4 style='font-weight:600; margin-bottom:16px;'>Personality Attribute Discovery</h4>", unsafe_allow_html=True)
                    st.markdown(f"**Style Type:** `{p_code}` — *{p_meta['title']}*")
                    st.caption(f"Confidence Level Mapped at {st.session_state.p_confidence}% based on verification parameters logging data loops.")
                    st.markdown("---")
                    st.markdown("**Character Strengths Vectors:**")
                    for s in p_meta["strengths"]:
                        st.markdown(f"- {s}")

        # ----------------------------------------------------------------------
        # MODE 3B: STEP BY STEP ROADMAP TIMELINES
        # ----------------------------------------------------------------------
        elif st.session_state.app_mode == "Timeline":
            st.markdown("<h2 style='font-weight:700; letter-spacing:-0.02em;'>Your Execution Roadmap</h2>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#6B7280; margin-bottom:32px;'>Chronological action blueprint path designed dynamically for an active {p_code} profile inside {st.session_state.interest} tracks.</p>", unsafe_allow_html=True)
            
            col_r1, col_r2 = st.columns([7, 5])
            with col_r1:
                st.markdown("<div class='timeline-container'>", unsafe_allow_html=True)
                for step in p_diverse["roadmap"]:
                    st.markdown(f"""
                    <div class='timeline-step'>
                        <h5 style='font-weight:600; margin-bottom:4px; color:#111827;'>{step.split(':')[0]}</h5>
                        <p style='color:#6B7280; font-size:14px; margin:0;'>{step.split(':')[1] if ':' in step else step}</p>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
                
            with col_r2:
                with st.container(border=True):
                    st.markdown("<h4 style='font-weight:600; margin-bottom:16px;'>Tiered Institutional Alignment Placement Matrix</h4>", unsafe_allow_html=True)
                    st.markdown("<p style='color:#4F8EF7; font-weight:600; font-size:13px; text-transform:uppercase;'>Tier 1 Placement Matrix (Dream Systems)</p>", unsafe_allow_html=True)
                    for u in modified_dream[:2]:
                        st.markdown(f"- `{u}`")
                    st.markdown("<br/>", unsafe_allow_html=True)
                    st.markdown("<p style='color:#6B7280; font-weight:600; font-size:13px; text-transform:uppercase;'>Tier 2 Options (High Affinity Foundations)</p>", unsafe_allow_html=True)
                    for u in modified_strong[:2]:
                        st.markdown(f"- `{u}`")
                    st.markdown("<br/>", unsafe_allow_html=True)
                    st.markdown("<p style='color:#9CA3AF; font-weight:600; font-size:13px; text-transform:uppercase;'>Tier 3 Operational Value Matrices</p>", unsafe_allow_html=True)
                    for u in interest_data["affordable"][:2]:
                        st.markdown(f"- `{u}`")

        # ----------------------------------------------------------------------
        # MODE 3C: PORTFOLIO REPOSITORIES & OPEN CONNECTIONS LINKS
        # ----------------------------------------------------------------------
        elif st.session_state.app_mode == "Resources":
            st.markdown("<h2 style='font-weight:700; letter-spacing:-0.02em;'>Resource Explorer & Project Repositories</h2>", unsafe_allow_html=True)
            
            col_res1, col_res2 = st.columns(2)
            with col_res1:
                with st.container(border=True):
                    st.markdown("<h4 style='font-weight:600; margin-bottom:16px;'>Targeted Project Directives</h4>", unsafe_allow_html=True)
                    for p in p_diverse["projects"]:
                        st.markdown(f"""
                        <div style='background-color:#F9FAFB; padding:16px; border-radius:8px; border:1px solid #E5E7EB; margin-bottom:12px;'>
                            <p style='font-weight:600; color:#111827; margin:0 0 4px 0;'>{p}</p>
                            <span style='color:#4F8EF7; font-size:12px; font-weight:500;'>Bespoke Validation Prompt Active</span>
                        </div>
                        """, unsafe_allow_html=True)
                        
            with col_res2:
                with st.container(border=True):
                    st.markdown("<h4 style='font-weight:600; margin-bottom:16px;'>Curated Learning Resource Hub Connectors</h4>", unsafe_allow_html=True)
                    for res in interest_data["resources"]:
                        clean_name = res.split(" — ")[0] if " — " in res else res
                        clean_desc = res.split(" — ")[1] if " — " in res else "Open interactive curriculum portal vertical tracking links."
                        st.markdown(f"**{clean_name}**")
                        st.caption(clean_desc)
                        st.markdown(f"[Launch External Connection Matrix Link](https://www.google.com/search?q={clean_name.replace(' ', '+')}+course)")
                        st.markdown("<div style='margin-bottom:16px;'></div>", unsafe_allow_html=True)

        # ----------------------------------------------------------------------
        # ADVANCED MENTOR COGNITIVE INFERENCE COUNCILS (Always Appended at Base)
        # ----------------------------------------------------------------------
        st.markdown("---")
        with st.container(border=True):
            st.markdown("<h4 style='font-weight:600; color:#111827;'>Master AI Success Mentor Guidance Directives</h4>", unsafe_allow_html=True)
            
            weaknesses_joined = ", ".join(st.session_state.weaknesses) if st.session_state.weaknesses else "None listed"
            subjects_joined = ", ".join(st.session_state.subjects) if st.session_state.subjects else "General Foundation Curriculum"
            strengths_joined = ", ".join(st.session_state.strengths) if st.session_state.strengths else "General Adaptability Traits"
            
            paragraph_1 = f"""
            Hello there! Let's examine your school tracking statistics across your active grade bracket `{st.session_state.grade}`. 
            Your primary interest focus in **{st.session_state.interest}** creates an amazing combination with your calculated 
            personality archetype **{p_code} ({p_meta['title']})**. Our matching calculations prove that your awesome core skills 
            in `{strengths_joined}` give you a fantastic foundation advantage to work toward your dream milestone goal: *\"{st.session_state.goal}\"*. 
            To make sure your growth timeline runs without any hitches, let's practice adding training steps to strengthen your listed improvement needs in `{weaknesses_joined}`.
            """
            
            paragraph_2 = f"""
            To build high confidence scores, follow through with your specialized **{p_code}** action roadmap carefully. Your profile scores 
            indicate that your highest-probability primary career track is **{top_career}** with a final integrated confidence indicator level of `{top_score}`. 
            Focus your upcoming study windows on launching your very first portfolio project framework blueprint, such as *\"{p_diverse['projects'][0]}\"*. Building high-quality projects 
            is the smartest way to accumulate evaluation record points when you submit your name to entry lists at dream universities like **{", ".join(modified_dream[:2])}**.
            """
            
            paragraph_3 = f"""
            **AI Mentor Operational Reminder Notes:** Lean on your awesome natural personality traits while keeping your school marks high in your core focus subjects inside `{subjects_joined}`. 
            Do not let short, routine assignments stall your forward velocity parameters. Initialize Phase 1 of your personalized roadmap tracking strategies today, keep up a fantastic 
            disciplined effort throughout your learning circles, and tackle your highest-priority milestones first. You have the structural blueprints in front of you; now, let's go build your future!
            """
            
            st.markdown(f"<p style='line-height:1.6; color:#374151; font-style:italic; margin-bottom:16px;'>{paragraph_1}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='line-height:1.6; color:#374151; font-style:italic; margin-bottom:16px;'>{paragraph_2}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='line-height:1.6; color:#374151; font-style:italic;'>{paragraph_3}</p>", unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)
        if st.button("Reset State Profile Parameters & Cache Systems", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# ==============================================================================
# PREMIUM MINIMAL BRAND FOOTER SYSTEM
# ==============================================================================
st.markdown("<div style='margin-top: 80px; padding: 24px 0; border-top: 1px solid #E5E7EB; text-align: center;'>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 14px; font-weight: 600; color: #111827; margin: 0;'>HELP AI</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 12px; color: #6B7280; margin: 4px 0 0 0;'>Higher Education Learning Path Platform • Built with Python and Streamlit</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
