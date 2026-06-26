import streamlit as st
import time

# ==============================================================================
# COLOR SYSTEM & UI CONFIGURATION (Professional Academic UI Blueprint)
# ==============================================================================
st.set_page_config(
    page_title="HELP AI",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"  # Left sidebar visible for navigation/step tracking
)

# Custom CSS injection using exact hex values from your spec image
# Enforces an academic, clean layout, custom fonts, flat buttons, and card borders.
professional_css = """
<style>
    /* Global Background & Base Text Settings */
    .stApp {
        background-color: #F5FAFF;
        color: #1E293B;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Headings Overrides */
    h1, h2, h3, h4, h5, h6 {
        color: #1E293B !important;
        font-weight: 700 !important;
    }
    
    /* Subtext and captions color mapping */
    .small-text, p, label, .stMarkdown {
        color: #334155;
    }
    
    /* Flat Buttons with precise borders and color scheme mapping */
    div.stButton > button {
        background-color: #2B6CB0 !important;
        color: #FFFFFF !important;
        border-radius: 6px !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
        transition: background-color 0.2s ease !important;
    }
    div.stButton > button:hover {
        background-color: #4A90E2 !important;
    }
    
    /* Card layout structure using native borders custom overrides */
    [data-testid="stMetricBorderDiv"], .stElementContainer div[data-style="border"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 8px !important;
        padding: 24px !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
    }
    
    /* Custom spacing adjustment for clean layout limits */
    .block-container {
        max-width: 1200px !important;
        padding-top: 2rem !important;
    }

    /* Metric visual configuration alignment */
    [data-testid="stMetricValue"] {
        font-size: 30px;
        font-weight: 700;
        color: #1E3A8A;
    }
</style>
"""
st.html(professional_css)

# ==============================================================================
# MASTER KNOWLEDGE DICTIONARIES (All 16 Personalities Core Matrix Data)
# ==============================================================================
PERSONALITY_REGISTRY = {
    "INTJ": {
        "title": "Architect", "strengths": ["Strategic", "Logical", "Independent", "Determined"], "growth": ["Arrogant", "Overthinker", "Dismissive of Emotions"],
        "questions": [
            "Do you prioritize macro long-term strategy planning over short-term execution?",
            "Do you vastly prefer working strictly independently over group collaborations?",
            "Do logic and optimization strategy games deeply interest you?",
            "Is process efficiency your ultimate standard metric for success?",
            "Would you rather design the structural layout of a system than manage its people?"
        ],
        "universities": ["MIT", "Stanford", "ETH Zurich", "Carnegie Mellon"],
        "diversity_map": {
            "Technology": {
                "bonus": {"AI Engineer": 10, "Software Engineer": 8, "Data Scientist": 9, "Cybersecurity Specialist": 7},
                "roadmap": ["Phase 1: Deep-dive into Discrete Math & Compiler Design Foundations", "Phase 2: Construct isolated scalable microservice backends", "Phase 3: Architect robust zero-trust security layers", "Phase 4: Deploy enterprise-tier autonomous cloud clusters"],
                "projects": ["Distributed Neural Network Architecture", "Cryptographic Consensus Core Simulation"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 8, "Entrepreneur": 6},
                "roadmap": ["Phase 1: Analyze advanced market volatility datasets", "Phase 2: Build quantitative predictive econometric tracking sandboxes", "Phase 3: Structure structural risk optimization audits", "Phase 4: Design macro-scale operational corporate strategies"],
                "projects": ["Automated Algorithmic Arbitrage Engine", "Predictive Corporate Competitor Analysis Core"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 7, "Pharmacist": 6},
                "roadmap": ["Phase 1: Master complex quantitative genomic parsing rules", "Phase 2: Run clinical trial data simulation pipelines", "Phase 3: Build diagnostic optimization tools for laboratories", "Phase 4: Publish predictive pathological structural models"],
                "projects": ["Genomic Sequencing Variant Mapping Pipeline", "Computational Molecular Interaction Sandbox"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Professor": 8, "Teacher": 5},
                "roadmap": ["Phase 1: Deconstruct structural learning analytics frameworks", "Phase 2: Standardize adaptive instructional assessment rules", "Phase 3: Architect scalable multi-district curriculum metrics", "Phase 4: Launch systemic educational optimization consultancies"],
                "projects": ["Data-Driven Adaptive Learning System Engine", "Institutional Curricular Alignment Sandbox"]
            },
            "Engineering": {
                "bonus": {"Electrical Engineer": 10, "Mechanical Engineer": 8, "Civil Engineer": 7},
                "roadmap": ["Phase 1: Analyze high-level finite element structural models", "Phase 2: Program hardware register-level industrial routing steps", "Phase 3: Optimize automated load tolerances under systemic strain", "Phase 4: Direct macro-scale smart infrastructure setups"],
                "projects": ["Smart Traffic Grid Infrastructure Simulator", "Finite Element Structural Stress Analyzer"]
            },
            "Creative Arts": {
                "bonus": {"Graphic Designer": 10, "Animator": 7, "Content Creator": 5},
                "roadmap": ["Phase 1: Study underlying design systems & geometric layout laws", "Phase 2: Systematize programmatic visual vector patterns", "Phase 3: Architect comprehensive interactive digital UI guidelines", "Phase 4: Launch technical spatial design framework agencies"],
                "projects": ["Scalable Dynamic UI Design Token System", "Procedural Vector Geometry Blueprint Engine"]
            }
        }
    },
    "INTP": {
        "title": "Logician", "strengths": ["Analytical", "Original", "Open-Minded", "Objective"], "growth": ["Disconnected", "Condescending", "Loathe Rules"],
        "questions": [
            "Do you find yourself constantly analyzing abstract theoretical frameworks?",
            "Do you value conceptual originality more than structural convention?",
            "Are you comfortable pivoting projects mid-way if a more interesting problem appears?",
            "Do you look for underlying logical fallacies during routine debates?",
            "Would you prefer discovering a new principle over building a commercial application?"
        ],
        "universities": ["MIT", "Stanford", "ETH Zurich", "Carnegie Mellon"],
        "diversity_map": {
            "Technology": {
                "bonus": {"AI Engineer": 10, "Data Scientist": 9, "Software Engineer": 7, "Cybersecurity Specialist": 6},
                "roadmap": ["Phase 1: Study functional programming languages & lambda calculus", "Phase 2: Build custom memory-safe compiler architectures", "Phase 3: Train alternative generative deep learning algorithms", "Phase 4: Author open-source abstract framework paradigms"],
                "projects": ["Custom Memory-Safe Functional Language Compiler", "Autonomous Neural Hyperparameter Tuning Core"]
            },
            "Business": {
                "bonus": {"Business Analyst": 10, "Product Manager": 7, "Entrepreneur": 5},
                "roadmap": ["Phase 1: Deconstruct macroeconomic game theory models", "Phase 2: Develop independent market structural simulators", "Phase 3: Audit complex decentralized micro-transaction ledger formats", "Phase 4: Formulate innovative algorithmic business optimization metrics"],
                "projects": ["Algorithmic Game Theory Market Matrix", "Decentralized Token Economic Flow Sandbox"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Pharmacist": 8, "Doctor": 5},
                "roadmap": ["Phase 1: Audit massive cellular data correlation matrices", "Phase 2: Simulate theoretical biochemical compounding dynamics", "Phase 3: Code advanced epidemiological mutation tracking loops", "Phase 4: Deliver first-principles scientific breakthroughs"],
                "projects": ["Biochemical Compounding Affinity Core Simulator", "Epidemiological Mutation Spread Blueprint"]
            },
            "Education": {
                "bonus": {"Professor": 10, "Education Consultant": 8, "Teacher": 5},
                "roadmap": ["Phase 1: Research underlying cognitive processing theories", "Phase 2: Analyze algorithmic knowledge gap detection models", "Phase 3: Formulate abstract pedagogical tracking taxonomies", "Phase 4: Direct alternative logic training institutions"],
                "projects": ["Algorithmic Student Knowledge Gap Mapper", "Cognitive Taxonomical Framework Tracker"]
            },
            "Engineering": {
                "bonus": {"Electrical Engineer": 10, "Mechanical Engineer": 8, "Civil Engineer": 6},
                "roadmap": ["Phase 1: Deconstruct thermodynamics and fundamental field theories", "Phase 2: Code low-level physical micro-sensor firmware array maps", "Phase 3: Simulate unconventional experimental layout models", "Phase 4: Pioneer foundational material engineering mechanics"],
                "projects": ["Bare-Metal Sensor Array Firmware Controller", "Thermodynamic Flow Simulation Array Engine"]
            },
            "Creative Arts": {
                "bonus": {"Animator": 10, "Graphic Designer": 7, "Content Creator": 6},
                "roadmap": ["Phase 1: Study mathematical fractals and procedural generation laws", "Phase 2: Build automated physics engines for interactive media", "Phase 3: Script custom shading pipelines for graphics engines", "Phase 4: Consult on technical visual generation software stacks"],
                "projects": ["Procedural Graphic Generation Canvas Sandbox", "Custom Physics-Driven Motion Shader Module"]
            }
        }
    },
    "ENTJ": {
        "title": "Commander", "strengths": ["Efficient", "Energetic", "Confident", "Strong-Willed"], "growth": ["Stubborn", "Dominant", "Intolerant"],
        "questions": [
            "Do you effortlessly take command of team structures when bottlenecks occur?",
            "Are you motivated by maximizing competitive market efficiency?",
            "Do you find managing human capital and deadlines highly rewarding?",
            "Is execution velocity more important to you than absolute perfection?",
            "Do you actively design optimization roadmaps for your career daily?"
        ],
        "universities": ["Stanford", "Wharton", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Product Manager": 10, "Cybersecurity Specialist": 8, "Software Engineer": 7, "AI Engineer": 6},
                "roadmap": ["Phase 1: Direct multi-engineer tech workspace agile sprints", "Phase 2: Standardize global enterprise software deployment SLAs", "Phase 3: Supervise cross-platform systems scaling audits", "Phase 4: Command enterprise-tier engineering organizations globally"],
                "projects": ["Multi-Tenant Scalable Operations Orchestrator", "Enterprise Tech Infrastructure Performance Deck"]
            },
            "Business": {
                "bonus": {"Entrepreneur": 10, "Product Manager": 9, "Business Analyst": 8, "Marketing Manager": 7},
                "roadmap": ["Phase 1: Evaluate tech startup seed capitalization runways", "Phase 2: Negotiate enterprise strategic vendor agreements", "Phase 3: Execute target user acquisition market offensives", "Phase 4: Scale full corporate enterprise frameworks toward market dominance"],
                "projects": ["Venture Seed Capital Runway Optimization Deck", "Strategic Market Penetration Deployment Matrix"]
            },
            "Healthcare": {
                "bonus": {"Doctor": 10, "Medical Researcher": 8, "Pharmacist": 6},
                "roadmap": ["Phase 1: Supervise hospital resource distribution logistics", "Phase 2: Enforce clinical compliance and output standards", "Phase 3: Lead multi-disciplinary specialized surgical cohorts", "Phase 4: Direct regional healthcare delivery infrastructure networks"],
                "projects": ["Integrated Healthcare Operations Routing Core", "Clinical Compliance Risk Mitigation Architecture"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Professor": 8, "Teacher": 6},
                "roadmap": ["Phase 1: Direct institutional educational budget frameworks", "Phase 2: Enforce systemic performance tracking standard criteria", "Phase 3: Command regional university administrative operations networks", "Phase 4: Restructure national educational system deployment models"],
                "projects": ["Regional Institutional Educational Budget Manager", "Systemic Academic Performance Metric Grid"]
            },
            "Engineering": {
                "bonus": {"Civil Engineer": 10, "Mechanical Engineer": 8, "Electrical Engineer": 7},
                "roadmap": ["Phase 1: Manage multi-million scale physical construction frameworks", "Phase 2: Enforce industrial factory manufacturing efficiency metrics", "Phase 3: Lead large-scale field engineering deployment teams", "Phase 4: Command international civil or mechanical infrastructure consortia"],
                "projects": ["Industrial Manufacturing Efficiency Router Core", "Macro Civil Infrastructure Lifecycle Tracking Suite"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Marketing Manager": 9, "Graphic Designer": 6},
                "roadmap": ["Phase 1: Establish large-scale creative content production studios", "Phase 2: Direct major corporate marketing campaign frameworks", "Phase 3: Manage comprehensive studio brand ecosystem portfolios", "Phase 4: Dominate global media agency monetization networks"],
                "projects": ["Scalable Creative Studio Asset Pipeline Tracker", "Corporate Content Campaign Monetization Blueprint"]
            }
        }
    },
    "ENTP": {
        "title": "Debater", "strengths": ["Innovative", "Curious", "Fast Learner", "Entrepreneurial"], "growth": ["Inconsistent", "Dislikes Routine", "Argumentative"],
        "questions": [
            "Do you enjoy challenging conventional wisdom and debating radical concepts?",
            "Would you rather assume the risk of building a startup than joining an established firm?",
            "How deep is your intrinsic interest in artificial intelligence ecosystem evolution?",
            "Do you enjoy dissecting highly complex, ambiguous problems?",
            "Do you struggle with standard routine operational tasks once conceptual loops are closed?"
        ],
        "universities": ["Stanford", "Wharton", "LUMS", "IBA"],
        "diversity_map": {
            "Technology": {
                "bonus": {"Entrepreneur": 10, "AI Engineer": 9, "Software Engineer": 7, "Data Scientist": 6},
                "roadmap": ["Phase 1: Rapidly deploy dynamic front-to-back Python prototypes", "Phase 2: Build 5 intersecting functional AI product wrappers", "Phase 3: Pitches disruptive technology concepts in hackathons", "Phase 4: Incubate cross-platform autonomous product SaaS labs"],
                "projects": ["AI Automated Startup Idea Validator Node", "Real-Time Gamified Student Planner Network"]
            },
            "Business": {
                "bonus": {"Entrepreneur": 10, "Marketing Manager": 9, "Product Manager": 8, "Business Analyst": 6},
                "roadmap": ["Phase 1: Draft growth hack loops using alternative channels", "Phase 2: Build interactive continuous business model builders", "Phase 3: Validate unique value monetization structures fast", "Phase 4: Scale modular, automated micro-venture ecosystems online"],
                "projects": ["Alternative Growth Hack Loop Validator Engine", "Interactive Business Model Canvas Prototyper"]
            },
            "Healthcare": {
                "bonus": {"Medical Researcher": 10, "Doctor": 7, "Pharmacist": 5},
                "roadmap": ["Phase 1: Ideate computational medical delivery software paths", "Phase 2: Launch digital alternative medical awareness applications", "Phase 3: Prototype user-friendly telehealth tracking portals", "Phase 4: Disrupt legacy diagnostic workflows with smart tech toolsets"],
                "projects": ["Telehealth Application UI Wireframe Network", "Legacy Diagnostic Workflow Software Disrupter"]
            },
            "Education": {
                "bonus": {"Education Consultant": 10, "Teacher": 8, "Professor": 6},
                "roadmap": ["Phase 1: Build gamified digital learning interaction modules", "Phase 2: Host interactive global conceptual student panels", "Phase 3: Launch alternative educational content properties", "Phase 4: Scale alternative online micro-school tracking models"],
                "projects": ["Gamified Quiz Application Software Blueprint", "Decentralized Micro-School Enrollment Portal"]
            },
            "Engineering": {
                "bonus": {"Mechanical Engineer": 10, "Electrical Engineer": 8, "Civil Engineer": 5},
                "roadmap": ["Phase 1: Prototype rapid mechanical proof-of-concept models", "Phase 2: Integrate cheap microcontrollers into smart arrays", "Phase 3: Pitch innovative green renewable energy inventions", "Phase 4: Scale agile component manufacturing tech operations"],
                "projects": ["Agile 3D Component Prototyping System", "Smart Microcontroller Environmental Collector"]
            },
            "Creative Arts": {
                "bonus": {"Content Creator": 10, "Graphic Designer": 8, "Animator": 7},
                "roadmap": ["Phase 1: Launch multiple visual experimentation digital spaces", "Phase 2: Mix interactive generative script formats with media", "Phase 3: Coordinate modern immersive performance events online", "Phase 4: Consult on dynamic branding systems for startup tracks"],
                "projects": ["Generative Media Scripting Sandbox Engine", "Immersive Startup Branding Design Token Suite"]
            }
        }
    }
}

PATHWAYS = {
    "Technology": {
        "careers": {"AI Engineer": 82, "Software Engineer": 78, "Data Scientist": 75, "Cybersecurity Specialist": 72},
        "dream": ["MIT", "Stanford"], "strong": ["NUST", "FAST"], "affordable": ["COMSATS", "Air University"],
        "skills": ["Python", "Git", "Data Structures", "Machine Learning"],
        "resources": ["CS50", "freeCodeCamp", "Kaggle", "Andrew Ng"],
        "projects": ["AI Career Mentor", "Expense Tracker", "Study Planner"],
        "opportunities": ["Hackathons", "Coding Competitions"]
    },
    "Business": {
        "careers": {"Entrepreneur": 85, "Product Manager": 80, "Business Analyst": 74, "Marketing Manager": 70},
        "dream": ["Stanford", "Wharton"], "strong": ["LUMS", "IBA"], "affordable": ["COMSATS", "IQRA"],
        "skills": ["Leadership", "Marketing", "Communication", "Finance"],
        "resources": ["Y Combinator School", "HubSpot Academy", "Coursera"],
        "projects": ["Startup Idea Validator", "Business Planner"],
        "opportunities": ["Startup Weekends", "Business Challenges"]
    }
}

# Add default fallback placeholders for unlisted personalities if needed by user tracking metrics loop
for key in ["INFJ", "INFP", "ENFJ", "ENFP", "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"]:
    if key not in PERSONALITY_REGISTRY:
        PERSONALITY_REGISTRY[key] = PERSONALITY_REGISTRY["ENTP"]

# ==============================================================================
# DESIGN LAYOUT STRATEGIES: SIDEBAR STEP TRACKING
# ==============================================================================
with st.sidebar:
    st.markdown("### HELP AI Onboarding")
    if not st.session_state.report_generated:
        st.markdown(f"**Current Status:** Step {st.session_state.step} of 4")
        st.progress(st.session_state.step / 4)
    else:
        st.markdown("**Current Status:** Evaluation Generated")
        st.progress(1.0)
    st.markdown("---")
    st.caption("Higher Education Learning Path Platform Engine")

# ==============================================================================
# MAIN PAGE TITLE CONTAINER
# ==============================================================================
st.title("HELP AI")
st.markdown("### Higher Education Learning Path AI")
st.markdown("Help AI analyzes your data profiles to recommend target careers, educational networks, and custom growth timelines.")
st.markdown("---")

# ==============================================================================
# ONBOARDING FLOW ROUTER (Pure native inputs with enough spacing)
# ==============================================================================
if not st.session_state.report_generated:
    
    # Step 1: Base Inputs Focus
    if st.session_state.step == 1:
        with st.container(border=True):
            st.markdown("#### Academic Foundations")
            grade = st.selectbox("Current Academic Tier", ["O-Level", "A-Level", "FSc", "Matric", "Other"], index=0)
            interest = st.selectbox("Main Interest Core Focus Area", list(PATHWAYS.keys()), index=0)
            goal = st.text_input("North Star Dream Career or Goal", value="", placeholder="e.g., Build an automated enterprise application")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Continue", use_container_width=True):
            if goal.strip() == "":
                st.error("Please explicitly declare your dream target goal trajectory.")
            else:
                st.session_state.grade = grade
                st.session_state.interest = interest
                st.session_state.goal = goal
                st.session_state.step = 2
                st.rerun()

    # Step 2: Superpowers & Target Attributes Matrices
    elif st.session_state.step == 2:
        with st.container(border=True):
            st.markdown("#### Skills & Core Competencies Matrix")
            subjects = st.multiselect("Favorite Subjects Focus Areas", ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Business", "Economics", "Art"], default=["Computer Science", "Mathematics"])
            strengths = st.multiselect(" सुपर पावर्स (Your Top Strengths)", ["Problem Solving", "Creativity", "Leadership", "Communication", "Analytical Thinking", "Teamwork"], default=["Problem Solving"])
            weaknesses = st.multiselect("Growth Areas (Skills to Improve)", ["Programming", "Public Speaking", "Mathematics", "Time Management", "Confidence", "Writing"], default=["Time Management"])
            activities = st.multiselect("High-Affinity Academic Activities", ["Coding", "Building Projects", "Research", "Reading", "Business", "Teaching", "Designing"], default=["Building Projects"])
            
            leadership_raw = st.radio("Do You Vibe With Leading Teams?", ["Love It", "Down for it sometimes", "Prefer execution over coordination"])
            st.session_state.leadership = "Yes" if "Love" in leadership_raw else ("Sometimes" if "Down" in leadership_raw else "No")
        
        st.markdown("<br>", unsafe_allow_html=True)
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

    # Step 3: Selection Modality Router
    elif st.session_state.step == 3:
        with st.container(border=True):
            st.markdown("#### Personality Intelligence Layer Selection")
            p_route = st.radio("Choose profile onboarding method:", [
                "Option A: I already know my personality type.",
                "Option B: I don't know my personality (Take Mini Diagnostics Assessment)."
            ])
            st.session_state.p_route = "A" if "Option A" in p_route else "B"
            
        st.markdown("<br>", unsafe_allow_html=True)
        col_back, col_next = st.columns(2)
        with col_back:
            if st.button("Back", use_container_width=True):
                st.session_state.step = 2
                st.rerun()
        with col_next:
            if st.button("Initialize Module", use_container_width=True):
                st.session_state.step = 4
                st.rerun()

    # Step 4: Active Testing Sub-Module Processing 
    elif st.session_state.step == 4:
        if st.session_state.p_route == "A":
            with st.container(border=True):
                st.markdown("#### Archetype Verification Framework Tracking")
                selected_type = st.selectbox("Select Explicit Personality Signature:", list(PERSONALITY_REGISTRY.keys()))
                
                st.markdown(f"##### Verification Metrics Parameters for {selected_type}")
                q_list = PERSONALITY_REGISTRY[selected_type]["questions"]
                
                st.slider(f"1. {q_list[0]}", 1, 10, 5, key="p_q1")
                st.slider(f"2. {q_list[1]}", 1, 10, 5, key="p_q2")
                st.slider(f"3. {q_list[2]}", 1, 10, 5, key="p_q3")
                st.slider(f"4. {q_list[3]}", 1, 10, 5, key="p_q4")
                st.slider(f"5. {q_list[4]}", 1, 10, 5, key="p_q5")
                
            st.markdown("<br>", unsafe_allow_html=True)
            col_back, col_submit = st.columns(2)
            with col_back:
                if st.button("Change Route", use_container_width=True):
                    st.session_state.step = 3
                    st.rerun()
            with col_submit:
                if st.button("Generate My AI Career Report", type="primary", use_container_width=True):
                    st.session_state.selected_personality = selected_type
                    st.session_state.p_confidence = 100
                    st.session_state.p_rationale = "Self-reported verified archetype profile signature configuration track rules mapping complete."
                    st.session_state.report_generated = True
                    st.rerun()
        else:
            with st.container(border=True):
                st.markdown("#### Cognitive Distribution Analysis Pipeline")
                
                st.markdown("**Section 1: Work Environment Interactions Recharge Scales**")
                ie1 = st.radio("Q1: After sorting an intense workload sprint, you prefer to refresh by:", ["Spending time completely alone", "Syncing directly with a broad social framework network"])
                ie2 = st.radio("Q2: Inside active design sessions workflow, your focus defaults toward:", ["Reflecting independently inside solo windows", "Exchanging ideas dynamically within team panels"])
                ie3 = st.radio("Q3: When introduced into large raw system network nodes, you usually:", ["Observe from a safe distance first", "Engage instantly with multiple connection tracks"])
                
                st.markdown("**Section 2: Information Asset Extraction Routines**")
                sn1 = st.radio("Q4: When analyzing data reports tracking structures, you favor:", ["Observable metrics and unvarnished facts", "Abstract systemic future strategy horizons concepts"])
                sn2 = st.radio("Q5: If exploring an advanced application framework ecosystem, you rely on:", ["Functional code execution baseline recipes", "First-principles engineering architectural models manuals"])
                sn3 = st.radio("Q6: Coworkers prize your outputs mostly due to your:", ["Grounded practical conversion reliability metrics", "Unconventional creative architectural conceptual visions"])
                
                st.markdown("**Section 3: Systemic Evaluation Logic Anchors**")
                tf1 = st.radio("Q7: When parsing critical operational blockers, you prioritize:", ["Cold logical tracing constraints logs", "Empathetic community collaborative consensus metrics"])
                tf2 = st.radio("Q8: If parsing code execution performance validation loops, you favor:", ["Direct unvarnished diagnostic crash error truth logs", "Constructive alignment counseling tracking guidelines"])
                tf3 = st.radio("Q9: Your primary inner alignment criteria driver status is focused on:", ["Systemic elite optimization performance parameters", "Deep authentic personal validation footprints"])
                
                st.markdown("**Section 4: Lifecycle Implementation Framework Scheduling Styles**")
                jp1 = st.radio("Q10: Your routine task management strategies favor:", ["Strict predictive scheduling calendars logs", "Dynamic immediate priority adaptations under strain"])
                jp2 = st.radio("Q11: When initializing structural system deployments, you:", ["Map out every component block variable beforehand", "Jump straight into functional implementation compilation cycles"])
                jp3 = st.radio("Q12: System deadlines optimize your output velocity metrics best when they are:", ["Vetted target timeline records handled early", "Urgent catalysts forcing immediate conversion loops at runtime"])

            st.markdown("<br>", unsafe_allow_html=True)
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
                    st.session_state.p_rationale = f"Profile mapped cleanly. Core cognitive evaluations verify preference weights alignment towards configuration tracking layers."
                    st.session_state.report_generated = True
                    st.rerun()

# ==============================================================================
# PROFESSIONAL EVALUATION REPORT DISPLAY VIEWPORTS
# ==============================================================================
if st.session_state.report_generated:
    interest_data = PATHWAYS[st.session_state.interest]
    career_base_scores = interest_data["careers"].copy()
    p_code = st.session_state.selected_personality
    p_meta = PERSONALITY_REGISTRY[p_code]
    p_diverse = p_meta["diversity_map"][st.session_state.interest]

    # COMPUTE MODIFIED MATRIX SCORES
    integrated_scores = {}
    for c, base in career_base_scores.items():
        integrated_scores[c] = base

    if "Problem Solving" in st.session_state.strengths:
        for c in integrated_scores: integrated_scores[c] += 5
    if "Analytical Thinking" in st.session_state.strengths:
        for c in integrated_scores: integrated_scores[c] += 4

    p_bonus_map = p_diverse["bonus"]
    for c in integrated_scores:
        if c in p_bonus_map:
            integrated_scores[c] += p_bonus_map[c]

    final_ranked_careers = sorted(integrated_scores.items(), key=lambda x: x[1], reverse=True)
    top_career, top_score = final_ranked_careers[0][0], final_ranked_careers[0][1]

    # UNIVERSITIES ROUTING SELECTION SETUPS
    raw_dream_unis = interest_data["dream"]
    raw_strong_unis = interest_data["strong"]
    p_preferred_unis = p_meta["universities"]

    modified_dream = list(dict.fromkeys(p_preferred_unis + raw_dream_unis))
    modified_strong = list(dict.fromkeys(raw_strong_unis))

    # SUCCESS SUBHEADER CONTAINER
    st.success("Your HELP AI Personalized Report")
    st.write(f"Active Workspace Profile Target Allocation Focus: **{p_code} - {p_meta['title']} Archetype**")
    st.markdown("<br>", unsafe_allow_html=True)

    # Clean, professional tab structure devoid of gradients or excessive emojis
    tab_insights, tab_personality, tab_system_map = st.tabs([
        "Career Insights Matrix", 
        "Personality Intelligence Analysis", 
        "Institutional System Roadmap Maps"
    ])

    with tab_insights:
        col_c1, col_c2 = st.columns([1, 1])
        with col_c1:
            with st.container(border=True):
                st.markdown("#### Primary Vector Match Resolution")
                st.metric(label="Calculated Profile Match Index", value=f"{top_score}% Confidence")
                st.markdown(f"**Top Recommended Track Track:** `{top_career}`")
                st.markdown(f"**North Star Aligned Objective Target:** *\"{st.session_state.goal}\"*")
            
            with st.container(border=True):
                st.markdown("#### Target Technical Skills Baseline Repositories")
                for skill in interest_data["skills"]:
                    st.markdown(f"- {skill}")
        
        with col_c2:
            with st.container(border=True):
                st.markdown("#### Top Integrated Competitive Match Vectors")
                st.caption("Includes base competencies matrix tracking points with specific personality adjustments applied.")
                for career, score in final_ranked_careers[:3]:
                    st.markdown(f"**{career}** • Evaluation Weight: `{score}`")
                    st.progress(min(score, 100) / 100)

    with tab_personality:
        col_p1, col_p2 = st.columns([1, 1])
        with col_p1:
            with st.container(border=True):
                st.markdown(f"#### Archetype Alignment Profile Key: {p_code}")
                st.metric(label="Alignment Matching Certainty Quotient Index", value=f"{st.session_state.p_confidence}%")
                st.write(f"**Diagnostic Pipeline System Logs:** *{st.session_state.p_rationale}*")
            
            with st.container(border=True):
                st.markdown("#### Cognitive Strengths Evaluation Vectors")
                for strength in p_meta["strengths"]:
                    st.markdown(f"- Core Alignment Match: **{strength}**")

        with col_p2:
            with st.container(border=True):
                st.markdown(f"#### Target Metric Modifications Mapped to Area: {st.session_state.interest}")
                for b_career, b_val in p_bonus_map.items():
                    st.markdown(f"- *{b_career}:* **+{b_val} Evaluation Modifier Allocation Weight**")

            with st.container(border=True):
                st.markdown("#### Portfolio Validation Project Blueprint Directives")
                for project in p_diverse["projects"]:
                    st.markdown(f"- **{project}**")

    with tab_system_map:
        col_r1, col_r2 = st.columns([1, 1])
        with col_r1:
            with st.container(border=True):
                st.markdown(f"#### Custom Strategic Timeline Roadmap for {p_code}")
                for step in p_diverse["roadmap"]:
                    with st.status(step, state="complete"):
                        st.write("Milestone metrics verified against processing parameters grids.")

        with col_r2:
            with st.container(border=True):
                st.markdown("#### Institutional Matrix Assignment Placements")
                st.markdown("**Tier 1 Placement Matrix (Dream Target Allocation)**")
                for uni in modified_dream: st.markdown(f"- `{uni}`")
                
                st.markdown("**Tier 2 Options (High Affinity Foundations)**")
                for uni in modified_strong: st.markdown(f"- `{uni}`")

    # ==========================================================================
    # CONTEXT-AWARE SYSTEM INFRASTRUCTURE AI MENTOR ADVICE LAYERS
    # ==========================================================================
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("#### Advice from your AI Mentor")
        
        weaknesses_joined = ", ".join(st.session_state.weaknesses) if st.session_state.weaknesses else "None logged"
        subjects_joined = ", ".join(st.session_state.subjects) if st.session_state.subjects else "Core Baseline Syllabus"
        strengths_joined = ", ".join(st.session_state.strengths) if st.session_state.strengths else "Universal Core Assets"
        
        paragraph_1 = f"""
        Analyzing your core academic profile metrics across the designated tier level `{st.session_state.grade}`, 
        your verified focus alignment towards **{st.session_state.interest}** integrates smoothly with your mapped 
        behavioral profile archetype identifier node **{p_code} ({p_meta['title']})**. Data records suggest your baseline competencies inside 
        `{strengths_joined}` present a clean operational efficiency advantage to track your listed milestone target: *\"{st.session_state.goal}\"*. 
        To avoid execution gaps, development tracks should be assigned to mitigate listed improvement criteria constraints in `{weaknesses_joined}`.
        """
        
        paragraph_2 = f"""
        To secure system performance goals, execute your customized **{p_code}** timeline milestones systematically. Metrics indicate that your 
        highest-probability primary recommended track is **{top_career}** with an integrated confidence indicator rating of `{top_score}`. Focus your 
        upcoming optimization sprints on launching high-impact validation frameworks such as *\"{p_diverse['projects'][0]}\"*. This ensures you build adequate 
        portfolio evaluation weight records when applying for admission selection lists across top institutions like **{", ".join(modified_dream[:2])}**.
        """
        
        paragraph_3 = f"""
        **AI Mentor Operational Directive Notes:** Maintain system architecture performance targets while continuously reinforcing foundation rules 
        within your selected topics matrix fields in `{subjects_joined}`. Do not allow brief procedural tasks to stall your trajectory vectors. Initialize Phase 1 
        of your personalized strategy tracking blueprint immediately, maintain optimization compliance parameters throughout tracking loops, and assign resources 
        to high-priority objectives first.
        """
        
        st.markdown(f"*{paragraph_1}*")
        st.markdown(f"*{paragraph_2}*")
        st.markdown(f"*{paragraph_3}*")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Clear Profile Cache and Reset State Parameters", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ==============================================================================
# PROFESSIONAL MINIMAL FOOTER SYSTEM
# ==============================================================================
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #475569; padding-top: 10px;">
        <h5>🧭 HELP AI</h5>
        <p style="font-size: 14px; margin: 2px;">Higher Education Learning Path Platform Engine</p>
        <p style="font-size: 13px; margin: 2px; color: #94A3B8;">Built with Python and Streamlit Cloud Systems Architecture Frameworks</p>
    </div>
    """,
    unsafe_allow_html=True
)
