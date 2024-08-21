import streamlit as st
import librosa
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from music21 import stream, note, duration, meter, pitch, environment
import subprocess
import os

# Set LilyPond path
environment.UserSettings()['lilypondPath'] = r'.\LilyPond\usr\bin\lilypond.exe' 

# Streamlit app
st.title('Music Transcription App')

# Upload audio file
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "flac"])

if audio_file is not None:
    try:
        # Save the uploaded file to a temporary location
        temp_audio_file = "temp_audio_file"
        with open(temp_audio_file, "wb") as f:
            f.write(audio_file.getbuffer())

        # Load audio file
        y, sr = librosa.load(temp_audio_file, sr=None)
        st.write(f"Audio file duration: {librosa.get_duration(y=y, sr=sr)} seconds")
        
        # Convert to mono
        y = librosa.to_mono(y)
        
        # Frequency analysis using STFT
        D = np.abs(librosa.stft(y))
        
        # Display spectrogram
        st.subheader('Spectrogram')
        fig, ax = plt.subplots(figsize=(10, 6))
        img = librosa.display.specshow(librosa.amplitude_to_db(D, ref=np.max), sr=sr, x_axis='time', y_axis='log', ax=ax)
        fig.colorbar(img, ax=ax, format='%+2.0f dB')
        st.pyplot(fig)
        
        # Pitch detection using pYIN
        st.subheader('Pitch Detection')
        pitches, pitch_confidence, _ = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C6'), sr=sr)
        
        st.write(f"Total pitches detected: {len(pitches)}")
        
        # Filter out pitches with low confidence
        confidence_threshold = st.slider('Confidence Threshold', 0.0, 1.0, 0.8)
        pitches_filtered = np.where(pitch_confidence >= confidence_threshold, pitches, np.nan)
        
        # Smooth the pitch values
        pitches_filtered = pd.Series(pitches_filtered).interpolate().ffill().bfill()
        
        # Analyzing rhythm
        onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
        onset_times = librosa.frames_to_time(onset_frames, sr=sr)
        
        st.write(f"Total onset times detected: {len(onset_times)}")
        
        # Music notation
        s = stream.Stream()
        ts = meter.TimeSignature('4/4')  # Assuming 4/4 time signature
        s.insert(0, ts)
        
        # Function to map pitch values to the nearest valid note
        def get_valid_pitch(pitch_value):
            try:
                p = pitch.Pitch()
                p.frequency = pitch_value
                return p
            except ValueError:
                return pitch.Pitch('C4')  # Default to middle C if pitch is invalid
        
        note_count = 0
        measure = stream.Measure()
        measure.insert(0, ts)  # Insert time signature in the measure

        for i in range(len(onset_times) - 1):
            start_time = onset_times[i]
            end_time = onset_times[i + 1]
            duration_value = end_time - start_time
            
            # Determine the note duration and add to the stream
            if duration_value < 0.25:
                dur = 'eighth'
            elif duration_value < 0.5:
                dur = 'quarter'
            elif duration_value < 1.0:
                dur = 'half'
            else:
                dur = 'whole'
            
            pitch_value = pitches_filtered[onset_frames[i]]
            
            if not np.isnan(pitch_value):
                valid_pitch = get_valid_pitch(pitch_value)
            else:
                st.warning(f"Warning: Invalid pitch value ({pitch_value}), using middle C as fallback.")
                valid_pitch = pitch.Pitch('C4')
            
            n = note.Note(valid_pitch)
            n.duration = duration.Duration(dur)
            measure.append(n)
            note_count += 1
            st.write(f"Added note: {n.nameWithOctave}, Duration: {dur}, Start: {start_time}, End: {end_time}")
            
            # If the measure is full (e.g., 4 quarter notes), add it to the stream and start a new measure
            if measure.quarterLength >= ts.barDuration.quarterLength:
                s.append(measure)
                measure = stream.Measure()  # Start a new measure

        # Append any remaining notes in the last measure
        if len(measure.notes) > 0:
            s.append(measure)
        
        # Display total number of notes
        st.write(f"Total number of notes: {note_count}")
        
        # Save output as LilyPond file
        output_file = 'output.ly'
        s.write('lilypond', fp=output_file)
        
        # Convert LilyPond file to PDF sheet music
        subprocess.run([r'.\LilyPond\usr\bin\lilypond.exe', '--pdf', output_file])
        
        # Display download link for PDF
        pdf_file = output_file.replace('.ly', '.pdf')
        if os.path.exists(pdf_file):
            with open(pdf_file, "rb") as file:
                btn = st.download_button(
                    label="Download Sheet Music as PDF",
                    data=file,
                    file_name="sheet_music.pdf",
                    mime="application/pdf"
                )
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        # Clean up temporary files
        if os.path.exists(temp_audio_file):
            os.remove(temp_audio_file)
        if 'output_file' in locals() and os.path.exists(output_file):
            os.remove(output_file)
        if 'pdf_file' in locals() and os.path.exists(pdf_file):
            os.remove(pdf_file)
