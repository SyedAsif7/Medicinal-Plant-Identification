# 🌿 Medicinal and Cosmetic Plant Identification Using Deep Learning

A sophisticated AI-powered system for identifying medicinal and cosmetic plants from leaf images using deep learning technology. This project bridges traditional botanical knowledge with modern artificial intelligence to provide accessible plant identification for healthcare, cosmetic, and educational applications.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)](https://streamlit.io/)
[![Accuracy](https://img.shields.io/badge/Accuracy-87.8%25-green)]()

## ✨ Features

### Core Capabilities
- **🎯 Dual-Purpose Identification**: Identifies both medicinal and cosmetic plants with specialized categorization
- **🔍 High Accuracy**: 87.8% classification accuracy on 50+ plant species
- **⚡ Fast Processing**: Sub-3-second response time for complete analysis
- **📱 User-Friendly Interface**: Intuitive web application accessible to all skill levels
- **💊 Comprehensive Information**: Detailed medicinal uses, cosmetic applications, and safety information
- **🔒 Safety First**: Confidence scoring and safety warnings for responsible use

### Technical Highlights
- MobileNetV2 architecture optimized for efficiency
- Transfer learning with ImageNet pre-trained weights
- Automated image quality assessment
- Confidence-based prediction reliability
- Responsive design for mobile and desktop

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone or Download the Project**
   ```bash
   cd medicinal_plant
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

4. **Access the Web Interface**
   Open your browser to `http://localhost:8501`

## 📖 Usage Guide

### How to Use

1. **Upload Image**: Click the upload area and select a clear photo of a plant leaf
2. **Identify Plant**: Click the "Identify Plant" button
3. **View Results**: See detailed information including:
   - Plant name and scientific classification
   - Confidence score
   - Medicinal applications
   - Cosmetic uses
   - Safety precautions
   - Quality indicators

### Best Practices for Accurate Results

✅ **For Best Results:**
- Use clear, well-focused images
- Ensure good lighting (natural light preferred)
- Center the leaf in the frame
- Use healthy, undamaged leaves
- Minimize background clutter

❌ **Avoid:**
- Blurry or out-of-focus images
- Very dark or overexposed photos
- Multiple different plants in one image
- Heavy shadows or reflections
- Damaged or diseased leaves

## 🌱 Supported Plants

The system identifies **50+ plant species** across three categories:

### Medicinal Plants (30 species)
Including: Aloevera, Neem, Tulasi, Ashwagandha, Brahmi, Amla, and more...

### Cosmetic Plants (25 species)
Including: Rose, Jasmine, Lavender, Hibiscus, Marigold, and more...

### Dual-Purpose Plants (5 species)
Including: Mint, Papaya, Lemon, Coconut, Turmeric

*See `plant_info.py` for complete list and detailed information.*

## 🏗️ Project Structure

```
medicinal_plant/
├── app.py                          # Main Streamlit web application
├── utils.py                        # Model loading and prediction utilities
├── plant_info.py                   # Plant information database
├── styles.py                       # Custom CSS styling
├── test_project.py                 # Command-line testing utility
├── plant.ipynb                     # Model training notebook
├── requirements.txt                # Python dependencies
├── .streamlit/                     # Streamlit configuration
│   └── config.toml
├── images/                         # Training dataset (optional)
│   ├── Aloevera/
│   ├── Neem/
│   └── ...
└── medicinal_plant_classifier.h5   # Trained Keras model
```

## 🔧 Technical Details

### Model Architecture
- **Base Model**: MobileNetV2 (ImageNet pre-trained)
- **Input Size**: 224×224 RGB images
- **Custom Layers**: Global Average Pooling + Dense layers
- **Output**: 50-class softmax classification
- **Parameters**: 3.4 million
- **Model Size**: 24.6 MB

### Performance Metrics
| Metric | Value |
|--------|-------|
| Overall Accuracy | 87.8% |
| Precision (Macro) | 89.2% |
| Recall (Macro) | 86.7% |
| F1-Score (Macro) | 87.9% |
| Inference Time | 1.9 seconds |
| Total Response Time | 2.7 seconds |

### System Requirements
**Minimum:**
- CPU: Intel i5 or equivalent
- RAM: 4GB
- Storage: 500MB free space

**Recommended:**
- CPU: Intel i7 or equivalent
- RAM: 8GB
- GPU: CUDA-compatible (optional for acceleration)

## 🧪 Testing

### Test via Command Line
```bash
# Test specific image
python test_project.py images/Amla/1300.jpg

# Test random image
python test_project.py
```

### Expected Output
```
Testing image: images/Amla/1300.jpg
------------------------------
Predicted Class: Amla
Confidence: 0.92
------------------------------
```

## 📊 Dataset

### Dataset Characteristics
- **Total Images**: 5,200+ images
- **Species Coverage**: 50+ plant species
- **Categories**: Medicinal, Cosmetic, Dual-purpose
- **Image Resolution**: 224×224 pixels
- **Train/Validation Split**: 80%/20%

### Data Augmentation
- Horizontal/vertical flipping
- Rotation (±15 degrees)
- Zoom scaling (0.8-1.2×)
- Shear transformations
- Brightness adjustment

## 🔒 Safety & Disclaimer

⚠️ **Important Notice**: This tool is for **educational and informational purposes only**.

- Always consult qualified healthcare professionals before using any plant for medicinal purposes
- Some plants may be toxic or cause allergic reactions
- Misidentification can be dangerous
- Results should not replace professional medical advice
- The developers are not liable for any adverse effects from misuse

## 🤝 Contributing

Contributions are welcome! Areas for contribution:
- Adding more plant species
- Improving model accuracy
- Enhancing UI/UX design
- Adding multilingual support
- Mobile application development
- Documentation improvements

## 📄 License

This project is provided as-is for educational and research purposes.

## 👥 Authors

**Snehal H. Pimple**  
MTech Student, Department of CSE  
Deogiri Institute of Engineering and Management Studies  
Chh. Sambhajinagar, Maharashtra, India  
Email: snehalshelke3397@gmail.com

**Dr. Ashwini S. Gaikwad**  
Assistant Professor, Department of CSE  
Deogiri Institute of Engineering and Management Studies  
Chh. Sambhajinagar, Maharashtra, India  
Email: ashwinigaikwad5056@gmail.com

## 🙏 Acknowledgments

- TensorFlow and Keras teams for the deep learning framework
- Streamlit community for the excellent web framework
- Botanical and herbal medicine resources
- Open source community for various libraries and tools
- Deogiri Institute of Engineering and Management Studies for support

## 📞 Support

For questions, issues, or suggestions:
- Open an issue on the project repository
- Contact the authors via email
- Check documentation files in the project

## 🔗 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [TensorFlow Documentation](https://www.tensorflow.org)
- [MobileNetV2 Paper](https://arxiv.org/abs/1801.04381)
- [Plant Identification Research](https://plantmethods.biomedcentral.com)

---

## 🌟 Citation

If you use this work in your research, please cite:

```
@article{pimple2024medicinal,
  title={Identification of Medicinal and Cosmetic Plant Using Deep Learning},
  author={Pimple, Snehal H and Gaikwad, Ashwini S},
  journal={Journal of AI Applications},
  year={2024}
}
```

---

*Made with by Snehal H. Pimple*  
