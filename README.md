

# 🎼 MelodyCraft: From Raw Audio to Symbolic Music Representation

## 🧭 Project Ideology

Most music processing tools focus on either:

* audio analysis
* or music notation

This project explores the connection between both:

> **Can raw audio signals be reliably transformed into structured musical notation?**

Music is not just sound—it contains:

* pitch (frequency)
* rhythm (timing)
* structure (measures, notes)

The goal of this project is to **bridge signal processing and symbolic music representation**.

---

## 🎯 Problem Statement

Converting audio into sheet music is difficult because:

* Audio signals are **continuous and noisy**
* Pitch detection is **uncertain and unstable**
* Rhythm detection depends on **accurate onset detection**
* Mapping signal → musical notation requires **discretization**

Goal:

> Build an end-to-end system that converts raw audio into readable sheet music.

---

## 🧠 System Overview

MelodyCraft is a **multi-stage audio processing pipeline**:

* 🎧 Audio ingestion
* 📊 Frequency analysis (STFT)
* 🎼 Pitch detection (pYIN)
* ⏱️ Rhythm detection (onsets)
* 🎵 Note mapping and structuring
* 📝 Sheet music generation (LilyPond)
* 🌐 Interactive UI (Streamlit)

---

## ⚙️ Processing Pipeline

```text
Audio → STFT → Pitch Detection → Pitch Filtering → Onset Detection
      → Note Mapping → Music21 Stream → LilyPond → Sheet Music PDF
```

---

## 🎧 Audio Processing Layer

* Input formats: MP3, WAV, FLAC
* Converted to mono for consistency
* Frequency analysis using **Short-Time Fourier Transform (STFT)**

---

## 🎼 Pitch Detection

Used:

* **pYIN algorithm (librosa)**

### Why pYIN?

* More robust than simple pitch trackers
* Provides **confidence scores**

### Key Step (your important logic):

* Low-confidence pitches are filtered
* Missing values are interpolated

👉 This is where your **data cleaning thinking** shows.

---

## ⏱️ Rhythm Detection

* Onset detection using `librosa.onset_detect`
* Converts frames → time intervals

### Duration Logic:

* Short interval → eighth note
* Medium → quarter / half
* Long → whole

👉 This is a **heuristic mapping**, not perfect—but practical.

---

## 🎵 Note Mapping

From your code ():

* Frequency → musical pitch (`music21.pitch`)
* Invalid values fallback → `C4`

### Insight:

> Real-world signals are messy → fallback strategies are necessary

---

## 🎼 Music Representation

Using **music21**:

* Notes grouped into measures
* Time signature: 4/4
* Notes assigned durations

---

## 📝 Sheet Music Generation

* Exported as `.ly` file
* Compiled using **LilyPond**
* Output: **high-quality PDF sheet music**

---

## 🖥️ UI Layer

Built with Streamlit:

* Upload audio file
* View spectrogram
* Adjust pitch confidence threshold
* See detected notes
* Download generated sheet music

---

## 📊 Key Insights

* Pitch detection is noisy → requires filtering
* Rhythm estimation is heuristic-based
* Audio → notation is inherently approximate
* Combining signal processing + symbolic tools enables usable output

---

## 📉 Limitations

This is where your project becomes **honest and strong**:

* Pitch detection errors propagate to final notation
* Fixed time signature (4/4) limits flexibility
* Rhythm mapping is heuristic, not learned
* Cannot handle polyphonic music well
* Sensitive to audio quality

---

## 🔭 Future Work

* Use deep learning for pitch estimation
* Support polyphonic transcription
* Adaptive rhythm modeling
* Automatic time signature detection
* Improve noise robustness

---

## 🛠️ Tech Stack

* Python
* Librosa (signal processing)
* Music21 (symbolic representation)
* LilyPond (notation rendering)
* Streamlit (UI)

---

## 🧪 How to Run

```bash
git clone https://github.com/sarvadutt/MelodyCraft
cd MelodyCraft

pip install -r requirements.txt
streamlit run Miniproject.py
```

---

## 👨‍💻 Author
GitHub: [https://github.com/sarvadutt](https://github.com/sarvadutt)
