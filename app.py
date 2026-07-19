import streamlit as st
from groq_service import get_client
from prompts import SYSTEM_PROMPT
from utils import clean_json
from image_service import generate_image
from tts_service import generate_audio
st.set_page_config(
    page_title="SIGNAL ZERO",
    page_icon="🛰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CSS
# -----------------------------
try:
    with open("styles.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass



client = get_client()

# -----------------------------
# Session State
# -----------------------------
defaults = {
    "story_history": [],
    "current_story": None,
    "current_image": None,
    "current_audio": None,
    "chapter": 1,
    "signal_strength": 100,
    "power": 100,
    "recovered_memories": 0,
    "mission_target": 10,
    "game_over": False,
    "memory_archive": [],
    "inventory": []
    
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v
def get_ai_status():

    power = st.session_state.power
    signal = st.session_state.signal_strength

    score = (power + signal) / 2

    if score >= 85:
        return "🟢 STABLE", "#22c55e"

    elif score >= 65:
        return "🟡 ACTIVE", "#facc15"

    elif score >= 40:
        return "🟠 WARNING", "#fb923c"

    elif score >= 20:
        return "🔴 CRITICAL", "#ef4444"

    else:
        return "⚫ OFFLINE", "#6b7280"
# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("Mission Settings")

    genre = st.selectbox(
        "Genre",
        [
            "Sci-Fi",
            "Mystery",
            "Adventure",
            "Fantasy",
            "Horror"
        ]
    )

    art_style = st.selectbox(
        "Art Style",
        [
            "Realistic",
            "Cinematic",
            "Anime",
            "Cyberpunk"
        ]
    )

    st.divider()

    if st.button("Restart Mission"):

        st.session_state.story_history = []
        st.session_state.current_story = None
        st.session_state.chapter = 1
        st.session_state.signal_strength = 100
        st.session_state.power = 100
        st.session_state.recovered_memories = 0
        st.session_state.game_over = False
        st.session_state.memory_archive = []
        st.session_state.inventory = []
        st.session_state.current_image = None
        st.session_state.current_audio = None

        st.rerun()
    st.divider()

    st.subheader("🧠 Memory Archive")    
    
    for memory in st.session_state.memory_archive:

        with st.expander(
             f"Chapter {memory['chapter']} - {memory['title']}"
    ):

             st.caption(memory["type"])

             st.write(memory["story"])
    st.divider()

    st.subheader("🎒 Inventory")

    if st.session_state.inventory:

       for item in st.session_state.inventory:

           icons = {
    "Medical Scanner":"🔬",
    "Navigation Chip":"💾",
    "Captain Keycard":"🔑",
    "Alien DNA":"🧬",
    "AI Core Fragment":"🤖"
}

           icon = icons.get(item,"📦")

           st.write(f"{icon} {item}")

    else:

       st.caption("Inventory Empty")        
        
st.markdown(
"""
<div class='main-title'>
SIGNAL ZERO
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='subtitle'>
Autonomous Memory Recovery System
</div>
""",
unsafe_allow_html=True
)

progress = (
    st.session_state.recovered_memories
    / st.session_state.mission_target
)

progress = min(progress, 1.0)
status, color = get_ai_status()
# -----------------------------
# Dashboard
# -----------------------------
st.markdown(f"""
<div class="hud-card">

<div class="hud-title">
MISSION STATUS
</div>

<div class="hud-grid">

<div>

Power

<div class="bar">

<div style="width:{st.session_state.power}%"></div>

</div>

</div>

<div>

Signal

<div class="bar">

<div style="width:{st.session_state.signal_strength}%"></div>

</div>

</div>

<div>

Mission

<div class="bar">

<div style="width:{progress*100}%"></div>

</div>

<div style="margin-top:8px">

{st.session_state.recovered_memories}/{st.session_state.mission_target}

</div>

</div>


<div>

AI CORE

<div style="
margin-top:8px;
font-weight:bold;
color:{color};
">
{status}
</div>

</div>

</div>

</div>
""", unsafe_allow_html=True)




# -----------------------------
# Gemini Function
# -----------------------------
def generate_story(choice):

    if st.session_state.story_history:

        history = "\n\n".join(st.session_state.story_history)

        prompt = f"""
{SYSTEM_PROMPT}

Previous Story:

{history}

Player Choice:

{choice}

Generate the next chapter.
"""

    else:

        prompt = f"""
{SYSTEM_PROMPT}

Story Genre: {genre}

Art Style: {art_style}

Start Chapter 1.
"""

    response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.8,
)

    return clean_json(
       response.choices[0].message.content
)

# -----------------------------
# Start Button
# -----------------------------
if st.session_state.current_story is None:

    if st.button(
        "🚀 START MISSION",
        use_container_width=True
    ):

        try:

            with st.spinner("Receiving Deep Space Signal..."):

                story = generate_story("Start")

                st.session_state.current_story = story
                
                st.session_state.current_image = generate_image(
                  story["image_prompt"]
                )
                exists = any(
                    m["chapter"] == story["chapter"]
                    and m["title"] == story["memory_title"]
                    for m in st.session_state.memory_archive
                )

                if not exists:
                    st.session_state.memory_archive.append({
                        "chapter": story["chapter"],
                        "title": story["memory_title"],
                        "type": story["memory_type"],
                        "story": story["story_text"]
                    })
                st.session_state.story_history.append(
                    story["story_text"]
                )

                st.rerun()

        except Exception as e:

            st.error(f"AI Transmission Failed\n\n{e}")

# -----------------------------
# Game Over
# -----------------------------
if st.session_state.game_over:

    st.success("🎉 MISSION COMPLETE")

    st.balloons()

    st.markdown("""
# SIGNAL ZERO

## Mission Successful

You recovered all human memories aboard SIGNAL ZERO.

### Final Report

✅ Mission Status: COMPLETE

🧠 Memories Recovered: 10/10

⚡ Power Remaining: {}%

📡 Signal Strength: {}%

Thank you, E.C.H.O.
""".format(
        st.session_state.power,
        st.session_state.signal_strength
    ))

    if st.button("🔄 Play Again"):

        for key in [
            "story_history",
            "current_story",
            "current_image"
        ]:
            st.session_state[key] = [] if key == "story_history" else None

        st.session_state.chapter = 1
        st.session_state.power = 100
        st.session_state.signal_strength = 100
        st.session_state.recovered_memories = 0
        st.session_state.game_over = False

        st.rerun()

    st.stop()
# -----------------------------
# Story
# -----------------------------
if st.session_state.current_story:
    
   
    story = st.session_state.current_story
    st.markdown(f"""
<div class="chapter-banner">

CHAPTER {st.session_state.chapter}

<div class="chapter-name">

{story["memory_title"]}

</div>

</div>
""", unsafe_allow_html=True)
    if st.session_state.current_audio is None:
       st.session_state.current_audio = generate_audio(
        story["story_text"]
    
    )

    left,right = st.columns([1,2])
    with left:
      if st.session_state.current_image:
        st.image(
            st.session_state.current_image,
            use_container_width=True
        )
        
      else:
        st.warning("No image available.")
    with right:
        st.markdown("## Memory Information")

        st.write(f"**Memory:** {story['memory_title']}")
        st.write(f"**Type:** {story['memory_type']}")
        st.write(f"**Recovered Item:** {story.get('item_found','None')}")
        st.write("**Threat:** HIGH")
        st.write("**AI CORE:** ONLINE")
    
    st.markdown("""
<div class="audio-header">

🎧 MEMORY PLAYBACK

</div>
""", unsafe_allow_html=True)

    st.audio(st.session_state.current_audio)


    st.markdown(f"""
<div class="story-terminal">

<div class="terminal-header">

Recovered Memory

</div>

<div class="terminal-body">

{story["story_text"]}

</div>

</div>
""", unsafe_allow_html=True)
    st.divider()

    st.markdown("### Choose Your Action")

    for option in story["options"]:

        disabled = (
           option["requires"] != "None"
            and option["requires"] not in st.session_state.inventory
        )

        if st.button(
            f"▶ {option['text']}",
            key=option["text"],
            use_container_width=True
    ):
          

         try:

                with st.spinner("""

🧠 Decrypting Memory Fragment...



"""):

                    next_story = generate_story(option["text"])

                    st.session_state.current_story = next_story
                    
                    if next_story["item_found"] != "None":

                      if next_story["item_found"] not in st.session_state.inventory:

                        st.session_state.inventory.append(
                            next_story["item_found"]
                         )

                        st.success(
                           f"🧰 Item Recovered: {next_story['item_found']}"
                        )
                    
                    st.session_state.memory_archive.append({
                      "chapter": st.session_state.chapter + 1,
                      "title": next_story["memory_title"],
                      "type": next_story["memory_type"],
                      "story": next_story["story_text"]
                     })
                    st.session_state.current_audio = generate_audio(
                       next_story["story_text"]
                    )
                    
                    try:
                      st.session_state.current_image = generate_image(
                      story["image_prompt"]
                     )
                    except Exception:
                        st.toast("🖼️ Image server is busy. Continuing without visuals...")
                        st.session_state.current_image = None
                    
                    if st.session_state.current_image:
                       st.image(
                           st.session_state.current_image,
                           use_container_width=True
                         )
                    else:
                       st.info("No image available for this scene.")

                    st.session_state.story_history.append(
                        next_story["story_text"]
                    )

                    st.session_state.chapter += 1

                    st.session_state.recovered_memories += 1
                    
                    if (
                       st.session_state.recovered_memories
                       >= st.session_state.mission_target
                    ):

                       st.session_state.game_over = True

                       st.rerun()
                    st.session_state.signal_strength = max(
                        0,
                        st.session_state.signal_strength - 3
                    )

                    st.session_state.power = max(
                        0,
                        st.session_state.power - 2
                    )

                    st.rerun()

         except Exception as e:

                st.error(f"AI Transmission Failed\n\n{e}")