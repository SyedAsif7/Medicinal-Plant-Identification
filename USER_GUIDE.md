# 📖 Medicinal Plant AI Classifier - User Guide

## 🎯 Getting Started

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux
- **Python**: Version 3.8 or higher
- **RAM**: Minimum 4GB recommended
- **Storage**: 500MB free space
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation Steps

#### Method 1: Quick Setup (Recommended)
1. Double-click `start_app.bat` (Windows) or run `python setup.py`
2. Follow the on-screen instructions
3. The application will start automatically

#### Method 2: Manual Installation
1. Open terminal/command prompt
2. Navigate to the project directory
3. Run: `pip install -r requirements.txt`
4. Run: `streamlit run app.py`

## 🖱️ Using the Web Application

### Basic Usage
1. **Open the Application**: Navigate to `http://localhost:8501` in your browser
2. **Upload Image**: Click the upload area and select a plant leaf image
3. **Identify Plant**: Click the "Identify Plant" button
4. **View Results**: See the plant identification with detailed information

### Interface Overview
```
┌─────────────────────────────────────────────────────────────┐
│  🌿 Medicinal Plant Identification                          │
├─────────────────────────┬───────────────────────────────────┤
│  📤 Upload Image        │  📊 Analysis Results              │
│  [File Upload Area]     │  ┌─────────────────────────────┐ │
│                         │  │ Plant Name & Scientific Name│ │
│  [Uploaded Image]       │  │ Confidence Score            │ │
│                         │  └─────────────────────────────┘ │
│                         │                                   │
│                         │  [Description Tab]                │
│                         │  [Medicinal Uses Tab]             │
│                         │  [Safety & Notes Tab]             │
└─────────────────────────┴───────────────────────────────────┘
```

### Features Explained

#### 📤 Image Upload
- **Supported formats**: JPG, JPEG, PNG
- **Image quality**: Clear, well-lit images work best
- **Plant focus**: Center the leaf in the image for better results
- **File size**: Images are automatically resized

#### 📊 Analysis Results
- **Plant Identification**: Scientific name and common name
- **Confidence Score**: How certain the AI is (0-100%)
- **Scientific Information**: Detailed botanical description
- **Medicinal Uses**: Traditional applications and benefits
- **Safety Information**: Important precautions and warnings

### Best Practices for Accurate Results

#### Image Quality Tips
✅ **Good Images**:
- Clear focus and sharp details
- Good lighting (natural light preferred)
- Leaf centered in the frame
- Minimal background clutter
- Single leaf or clear leaf group

❌ **Avoid**:
- Blurry or out-of-focus images
- Very dark or overexposed photos
- Multiple different plants in one image
- Heavy shadows or reflections
- Damaged or diseased leaves (may affect accuracy)

#### Plant Preparation
- Use fresh, healthy leaves when possible
- Remove dirt or debris from leaves
- Position leaves flat for better recognition
- Include both top and bottom sides if possible

## 🧪 Testing the Application

### Command Line Testing
Test specific images without the web interface:

```bash
# Test a specific image
python test_project.py images/Amla/1300.jpg

# Test random image from dataset
python test_project.py

# Test your own image
python test_project.py path/to/your/image.jpg
```

### Expected Output
```
Testing image: images/Amla/1300.jpg
------------------------------
Predicted Class Index: 1
Predicted Class: Amla
Confidence: 0.92
------------------------------
```

## 📱 Mobile Usage

The application is fully responsive and works on mobile devices:

1. **Access**: Open your phone's browser
2. **URL**: Navigate to your computer's IP address on port 8501
3. **Example**: `http://192.168.1.100:8501`
4. **Usage**: Same interface, touch-friendly controls

## ⚠️ Important Safety Information

### Medical Disclaimer
**This tool is for educational purposes only**
- Results should not replace professional medical advice
- Always consult healthcare professionals before using plants medicinally
- Some plants may be toxic or cause allergic reactions
- Misidentification can be dangerous

### When to Seek Professional Help
- If you have medical conditions
- If you're taking medications
- If you're pregnant or nursing
- If you have allergies
- For serious health concerns

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Application Won't Start
**Problem**: Error when running `streamlit run app.py`
**Solutions**:
- Check Python version (3.8+ required)
- Reinstall dependencies: `pip install -r requirements.txt`
- Ensure all files are in the correct directory

#### Model Loading Error
**Problem**: "Model file not found" error
**Solutions**:
- Verify `medicinal_plant_classifier.h5` exists
- Check file permissions
- Re-download the model file if corrupted

#### Poor Prediction Accuracy
**Problem**: Incorrect plant identification
**Solutions**:
- Use higher quality images
- Ensure leaf is clearly visible
- Try different angles of the same leaf
- Check if the plant is in the supported species list

#### Slow Performance
**Problem**: Long loading or processing times
**Solutions**:
- Close other applications to free memory
- Use smaller image files
- Ensure adequate system resources

### Error Messages and Meanings

| Error Message | Meaning | Solution |
|---------------|---------|----------|
| "Module not found" | Missing dependency | Run `pip install -r requirements.txt` |
| "Model file not found" | Model file missing | Check if `.h5` file exists |
| "Invalid image format" | Wrong file type | Use JPG, JPEG, or PNG files |
| "CUDA out of memory" | GPU memory full | Close other applications or use CPU |

## 📚 Learning Resources

### Understanding Results
- **Confidence Score**: Higher = more certain (80%+ is good)
- **Scientific Names**: Latin names used by botanists
- **Medicinal Uses**: Traditional applications, not medical advice
- **Safety Notes**: Important warnings and precautions

### Supported Plants
The model currently identifies 40+ medicinal plant species including:
- **Common Herbs**: Tulasi, Neem, Amla, Mint
- **Flowering Plants**: Rose, Jasmine, Hibiscus
- **Trees**: Mango, Lemon, Papaya
- **Specialty Plants**: Ashwagandha, Brahmi, Aloevera

### Accuracy Information
- **Overall Accuracy**: ~85-90% on validation data
- **High Confidence**: 80%+ predictions are usually reliable
- **Limitations**: May struggle with very similar species
- **Improvement**: Accuracy improves with better image quality

## 🤝 Getting Help

### Support Resources
- **Documentation**: Check `PROJECT_DOCUMENTATION.md` for technical details
- **Issues**: Report problems on the project repository
- **Community**: Join discussions about plant identification

### Feedback and Suggestions
We welcome your input to improve the application:
- Feature requests
- Accuracy improvements
- New plant species suggestions
- User experience enhancements

## 📝 Quick Reference

### Essential Commands
```bash
# Start the application
streamlit run app.py

# Run setup script
python setup.py

# Test specific image
python test_project.py path/to/image.jpg

# Stop the application
# Press CTRL+C in the terminal
```

### File Locations
- **Main App**: `app.py`
- **Model**: `medicinal_plant_classifier.h5`
- **Plant Info**: `plant_info.py`
- **Configuration**: `.streamlit/config.toml`

### Keyboard Shortcuts (Web Interface)
- **R**: Rerun the application
- **C**: Clear cache
- **/**: Show command menu

---
*For technical documentation, see PROJECT_DOCUMENTATION.md*