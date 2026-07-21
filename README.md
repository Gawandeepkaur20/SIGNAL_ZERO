# 🛰️ SIGNAL ZERO – AI-Powered Multi-Modal Visual Novel

An interactive AI-powered visual novel built with **Streamlit**, where every decision shapes the story. Explore a mysterious abandoned spaceship, recover lost human memories, unlock hidden artifacts, and uncover the truth behind **SIGNAL ZERO**.

Unlike traditional visual novels, every chapter is generated in real time using a Large Language Model, accompanied by AI-generated artwork and narrated using Text-to-Speech.

---

## ✨ Features

- 🤖 **AI-Generated Storytelling**
  - Dynamic story generation powered by Groq Llama.
  - Every choice leads to a unique continuation.

- 🎨 **AI Image Generation**
  - Generates cinematic visuals for every scene using Pollinations AI.

- 🎧 **Text-to-Speech Narration**
  - Every memory fragment is converted into speech for an immersive experience.

- 🧠 **Memory Archive**
  - Stores all recovered memories chapter-wise.
  - Allows players to revisit previous discoveries.

- 🎒 **Inventory System**
  - Collect important items during exploration.
  - Some story paths require specific recovered items.

- 🛰️ **Mission Dashboard**
  - Track:
    - Power
    - Signal Strength
    - Mission Progress
    - AI Core Status

- 📖 **Dynamic Chapter Progression**
  - Story progresses chapter by chapter based on player decisions.

- 🔀 **Branching Narrative**
  - AI generates multiple choices dynamically for every scene.

- 💾 **State Persistence**
  - Uses Streamlit Session State to preserve:
    - Story history
    - Images
    - Audio
    - Inventory
    - Memory Archive
    - Mission progress

- 🛡️ **Graceful Error Handling**
  - Prevents crashes when AI or image services are unavailable.

---



---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Streamlit | Interactive Web Application |
| Groq Llama 3.3 70B | Story Generation |
| Pollinations AI | Image Generation |
| gTTS | Text-to-Speech |
| HTML + CSS | Custom UI Styling |
| JSON | Structured AI Responses |
| Streamlit Session State | Stateful Gameplay |

---

# 🧠 AI Workflow

```text
Player Choice
      │
      ▼
Groq LLM
      │
Returns Structured JSON
      │
 ┌──────────────┬──────────────┬─────────────┐
 │              │              │
 ▼              ▼              ▼
Story Text   Image Prompt   Choices
 │              │              │
 ▼              ▼              ▼
TTS       Pollinations AI   Dynamic Buttons
 │              │              │
 └──────────────┴──────────────┘
              │
              ▼
      Streamlit Interface
```

---

# 📂 Project Structure

```
SIGNAL_ZERO/
│
├── app.py
├── prompts.py
├── groq_service.py
├── image_service.py
├── tts_service.py
├── utils.py
├── styles.css
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/SIGNAL_ZERO.git

cd SIGNAL_ZERO
```

---

### Create virtual environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

### Run the application

```bash
streamlit run app.py
```

---

# 🎮 Gameplay

1. Select your preferred Story Genre.
2. Select an Art Style.
3. Start the mission.
4. Read the AI-generated story.
5. Listen to the narration.
6. View the generated artwork.
7. Choose your next action.
8. Recover memories and collect items.
9. Complete the mission.

---

# 💡 Concepts Demonstrated

- Prompt Engineering
- Structured JSON Parsing
- Dynamic UI Generation
- Session State Management
- Multi-Modal AI Applications
- AI Image Generation
- Text-to-Speech Integration
- Conditional Story Progression
- Interactive Game Design
- Error Handling

---

# 🎯 Learning Outcomes

This project demonstrates:

- Building stateful AI applications
- Integrating multiple AI services
- Designing interactive user experiences
- Managing complex application state
- Creating dynamic interfaces with Streamlit
- Engineering structured prompts for LLMs

---

# 📸 Future Improvements

- Multiple story endings
- Achievement system
- Dynamic AI Core health
- Mission event logs
- Save/Load game
- Background ambient music
- Character portraits
- Animated scene transitions

---

# 🙌 Acknowledgements

- **MirAI School of Technology** – AI Builder Virtual Summer Internship 2026
- **Groq** – Llama 3.3 70B Inference API
- **Pollinations AI** – AI Image Generation
- **Streamlit** – Interactive Python Apps
- **gTTS** – Text-to-Speech

---



---

## ⭐ If you found this project interesting, consider giving it a star!
