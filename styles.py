def get_custom_css():
    return """
    <style>
    /* 
       -------------------------------------------------------------------------
       MEDICINAL PLANT AI - DESIGN SYSTEM
       -------------------------------------------------------------------------
    */
    
    :root {
        --primary-color: #2E7D32;       /* Dark Green */
        --primary-light: #4CAF50;       /* Standard Green */
        --primary-dark: #1B5E20;        /* Forest Green */
        --secondary-color: #E8F5E9;     /* Very Light Green Background */
        --accent-color: #F9A825;        /* Yellow/Gold for highlights */
        --text-main: #212121;           /* Almost Black */
        --text-secondary: #555555;      /* Dark Gray */
        --bg-main: #FAFAFA;             /* Off White */
        --card-bg: #FFFFFF;             /* Pure White */
        --shadow-light: 0 4px 6px rgba(0,0,0,0.05);
        --shadow-medium: 0 8px 15px rgba(0,0,0,0.1);
        --radius-std: 12px;
    }

    /* Global Settings */
    .stApp {
        background-color: var(--bg-main);
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    /* --------------------------
       HEADER & HERO SECTION 
       -------------------------- */
    .hero-container {
        background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary-color) 100%);
        padding: 3rem 2rem;
        border-radius: var(--radius-std);
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: var(--shadow-medium);
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: white !important;
        letter-spacing: -1px;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 300;
        max-width: 600px;
        margin: 0 auto;
    }

    /* --------------------------
       UPLOAD SECTION
       -------------------------- */
    .upload-section {
        background-color: var(--card-bg);
        padding: 2rem;
        border-radius: var(--radius-std);
        box-shadow: var(--shadow-light);
        border: 1px solid #eee;
    }

    /* Streamlit File Uploader Customization */
    [data-testid="stFileUploader"] {
        padding: 30px;
        border: 2px dashed var(--primary-light);
        border-radius: var(--radius-std);
        background-color: var(--secondary-color);
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: var(--primary-dark);
        background-color: #DCEDC8;
    }

    /* --------------------------
       PREDICTION CARD
       -------------------------- */
    .prediction-card {
        background: var(--card-bg);
        border-radius: var(--radius-std);
        padding: 0;
        overflow: hidden;
        box-shadow: var(--shadow-medium);
        margin-bottom: 2rem;
        position: relative;
        border-top: 5px solid var(--primary-color);
    }
    
    .card-header {
        background-color: var(--secondary-color);
        padding: 1.5rem;
        text-align: center;
        border-bottom: 1px solid #e0e0e0;
    }
    
    .plant-name {
        color: var(--primary-dark);
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
        line-height: 1.2;
    }
    
    .scientific-name {
        color: var(--text-secondary);
        font-style: italic;
        font-size: 1.1rem;
        margin-top: 5px;
    }
    
    .confidence-badge {
        background-color: var(--primary-color);
        color: white;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        display: inline-block;
        margin-top: 10px;
    }

    .card-body {
        padding: 1.5rem;
    }

    /* --------------------------
       BUTTONS
       -------------------------- */
    .stButton > button {
        width: 100%;
        background: linear-gradient(to right, var(--primary-color), var(--primary-light));
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 8px;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(46, 125, 50, 0.4);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }

    /* --------------------------
       TABS & INFO
       -------------------------- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        border-bottom: 2px solid #eee;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        border-radius: 8px 8px 0 0;
        padding: 0 20px;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: var(--secondary-color) !important;
        color: var(--primary-dark) !important;
    }
    
    .info-box {
        background-color: #FFF8E1;
        border-left: 4px solid var(--accent-color);
        padding: 1rem;
        border-radius: 4px;
        margin-top: 1rem;
    }

    /* --------------------------
       SIDEBAR
       -------------------------- */
    [data-testid="stSidebar"] {
        background-color: white;
        border-right: 1px solid #eee;
    }
    
    .sidebar-header {
        text-align: center;
        padding-bottom: 1rem;
        margin-bottom: 1rem;
        border-bottom: 1px dashed #ddd;
    }

    /* --------------------------
       FOOTER
       -------------------------- */
    .footer {
        text-align: center;
        padding: 2rem;
        color: var(--text-secondary);
        font-size: 0.9rem;
        border-top: 1px solid #eee;
        margin-top: 3rem;
    }
    
    </style>
    """
