import streamlit as st
from PIL import Image
import time
from utils import load_model, predict_plant
from plant_info import PLANT_INFO
from styles import get_custom_css

# Page Config
st.set_page_config(
    page_title="Medicinal Plant AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

def render_sidebar():
    """Render the sidebar content"""
    st.sidebar.title("Medicinal Plant AI")
    st.sidebar.markdown("---")
    st.sidebar.info(
        "Identify medicinal plants instantly using deep learning. "
        "Upload a leaf image to get started."
    )
    
    st.sidebar.markdown("### 🛠️ Features")
    features = [
        ("📸", "Instant Analysis"),
        ("📚", "Scientific Info"),
        ("💊", "Medicinal Uses"),
        ("⚠️", "Safety Precautions")
    ]
    for icon, text in features:
        st.sidebar.markdown(f"**{icon} {text}**")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ℹ️ About")
    st.sidebar.caption(
        "This tool uses a Convolutional Network (CNN) "
        "trained on thousands of plant images to assist in identification."
    )
    st.sidebar.markdown("---")
    st.sidebar.caption("Developed by Snehal H. Pimple")
    st.sidebar.caption("© 2026 Medicinal Plant AI Project")

def render_hero():
    """Render the Hero Section"""
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">🌿 Medicinal Plant Identification</h1>
            <p class="hero-subtitle">
                Discover nature's pharmacy with the power of Artificial Intelligence. 
                Identify plants, learn their uses, and explore traditional medicine.
            </p>
        </div>
    """, unsafe_allow_html=True)

def render_empty_state():
    """Render the empty state message"""
    st.markdown("""
    <div style="background-color: white; padding: 3rem; border-radius: 12px; text-align: center; margin-top: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <h3 style="color: #2e7d32; margin-bottom: 1rem;">👋 Welcome to Your Personal Botanist</h3>
        <p style="color: #666; font-size: 1.1rem; line-height: 1.6;">
            To get started, please upload a clear image of a medicinal plant leaf on the left panel.
            <br>Our advanced AI will analyze the leaf patterns and provide detailed medicinal information.
        </p>
        <div style="margin-top: 30px; font-size: 3rem; opacity: 0.8;">🌿 🔍 💊</div>
    </div>
    """, unsafe_allow_html=True)

def main():
    render_sidebar()
    render_hero()
    
    # Main Layout
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.markdown("### 📤 Upload Image")
        # Wrap uploader in a custom div for styling hooks if needed (though stFileUploader is hard to wrap directly in pure markdown without component)
        # We rely on global CSS for stFileUploader
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        
        if uploaded_file:
            try:
                image_pil = Image.open(uploaded_file)
                st.markdown('<div class="upload-section">', unsafe_allow_html=True)
                st.image(image_pil, caption="Uploaded Image", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error opening image: {e}")
                uploaded_file = None
            
    with col2:
        if uploaded_file:
            st.markdown("### 📊 Analysis Results")
            
            # Load model
            model = load_model()
            
            if model:
                if st.button("🔍 Identify Plant", help="Click to analyze the image"):
                    with st.spinner("Analyzing plant features..."):
                        # Artificial delay for UX perception
                        time.sleep(0.8)
                        
                        # Prediction
                        label, confidence = predict_plant(model, image_pil)
                        
                        if label:
                            plant_data = PLANT_INFO.get(label, {})
                            
                            # Result Card
                            st.markdown(f"""
                                <div class="prediction-card">
                                    <div class="card-header">
                                        <h2 class="plant-name">{label}</h2>
                                        <div class="scientific-name">{plant_data.get('scientific_name', 'Scientific name unavailable')}</div>
                                        <div class="confidence-badge">Confidence: {confidence:.1%}</div>
                                    </div>
                                    <div class="card-body">
                                        <!-- Content is in tabs below -->
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)
                            
                            # Detailed Info Tabs
                            tab1, tab2, tab3 = st.tabs(["📝 Description", "💊 Medicinal Uses", "⚠️ Safety & Notes"])
                            
                            with tab1:
                                st.markdown('<div class="info-box">', unsafe_allow_html=True)
                                st.markdown("#### About this Plant")
                                st.write(plant_data.get('description', 'No description available.'))
                                st.markdown('</div>', unsafe_allow_html=True)
                            
                            with tab2:
                                st.markdown('<div class="info-box" style="border-left-color: #4CAF50;">', unsafe_allow_html=True)
                                st.markdown("#### Traditional & Medicinal Uses")
                                uses = plant_data.get('uses', [])
                                if uses:
                                    for use in uses:
                                        st.markdown(f"✅ {use}")
                                else:
                                    st.info("No medicinal uses listed.")
                                st.markdown('</div>', unsafe_allow_html=True)
                                    
                            with tab3:
                                st.warning(
                                    "**Disclaimer:** This tool is for educational purposes only. "
                                    "Always consult a qualified healthcare professional, botanist, or herbalist "
                                    "before using any plant for medicinal purposes. "
                                    "Misidentification can be dangerous."
                                )
                        else:
                            st.error("Could not identify the plant. Please try another image.")
        else:
            render_empty_state()
            
    # Footer
    st.markdown("""
        <div class="footer">
            <p>Made with by Snehal H. Pimple</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
