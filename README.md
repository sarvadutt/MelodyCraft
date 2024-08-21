# **MelodyCraft**

Welcome to **MelodyCraft** – an advanced music transcription app that transforms audio files into sheet music. This project utilizes Python, Streamlit, and LilyPond to deliver a seamless experience for musicians and audio engineers alike.

## **Features**

- **Audio to Sheet Music**: Convert audio files (MP3, WAV, FLAC) to beautiful sheet music in PDF format.
- **Spectrogram Display**: Visualize the frequency spectrum of your audio with an interactive spectrogram.
- **Pitch Detection**: Analyze and detect pitches using the powerful pYIN algorithm.
- **Rhythm Analysis**: Automatically detect note onsets and assign appropriate durations.
- **LilyPond Integration**: Generate high-quality sheet music using the LilyPond music engraving software.

## **Installation**

To run **MelodyCraft** locally, follow these steps:

### **1. Clone the Repository**

git clone https://github.com/sarvadutt/MelodyCraft

cd MelodyCraft

### **2. Install Python Dependencies**

Ensure you have Python installed on your machine. Then, install the required Python packages:


pip install -r requirements.txt


### **3. Install LilyPond**

LilyPond is required for generating the sheet music PDF. Download and install it from the [official website](http://lilypond.org/download.html).

After installation, ensure that the LilyPond executable is in your system's PATH, or update the path in the `environment.UserSettings()` line in the code.

### **4. Run the App**

Launch the Streamlit app:


streamlit run Miniproject.py


### **5. Upload and Transcribe**

Upload your audio file in the Streamlit interface, and let **MelodyCraft** do the magic. Once the transcription is complete, you can download the generated sheet music in PDF format.

## **How It Works**

1. **Audio Processing**: The app loads and processes the audio file using `librosa`, performing mono conversion, frequency analysis, and pitch detection.
2. **Pitch and Rhythm Detection**: Detected pitches are filtered, smoothed, and matched to valid musical notes. Onsets are detected to define the rhythm.
3. **Music Notation**: The processed data is transformed into music notation using `music21`, with appropriate time signatures and note durations.
4. **Sheet Music Generation**: The musical score is exported to a `.ly` file and compiled into a PDF using LilyPond.

## **Contributing**

Contributions are welcome! If you'd like to enhance **MelodyCraft**, please fork the repository and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Acknowledgements**

- **Librosa**: For the powerful music and audio analysis tools.
- **Streamlit**: For making the app development so intuitive and interactive.
- **LilyPond**: For providing a way to create beautiful sheet music.
- **Music21**: For the fantastic music theory and notation tools.

---

### **Contact**

For any inquiries or support, feel free to reach out to me at **Sarvadutt25@gmail.com**.


