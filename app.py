import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

def get_video_link(v_id):
    SHEET_URL = "https://docs.google.com/spreadsheets/d/1l4WfVPjS-waC0zpzwMswKbzdOBv28P_RcG1R5WGTPYs/export?format=csv"
    try:
        df = pd.read_csv(SHEET_URL)
        result = df[df['id'].astype(str) == str(v_id)]
        if not result.empty:
            return result.iloc[0]['video_url']
    except Exception as e:
        st.error(f"Error reading sheet: {e}")
    return "https://example.com/default"   # Replace adult link

# Page config
st.set_page_config(page_title="Premium Movie Portal", layout="centered")

# Main CSS
st.markdown("""
<style>
.block-container { padding-top: 2rem; padding-bottom: 0rem; max-width: 75%; }
div.stButton > button { width: 100%; }
iframe { max-width: 100%; }

/* Pop-up Window */
.modal-overlay {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.8);
    z-index: 9999;
}
.modal-content {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    background: white;
    padding: 20px;
    width: 90%;
    height: 80%;
    border-radius: 10px;
}
.close-btn {
    float: right;
    font-size: 25px;
    cursor: pointer;
    color: red;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Ads
ads_scripts = """
<script type='text/javascript' src='//pl28540401.effectivegatecpm.com/8b/6c/e4/8b6ce4814b6f7909e97fddc0fc571e00.js'></script>
<script type='text/javascript' src='//pl28541110.effectivegatecpm.com/61/73/00/6173009a89d5198b3e1211b7d30b25be.js'></script>
"""
components.html(ads_scripts, height=0)

# Titles
st.markdown("<h3 style='text-align: center;'>MURASAKI</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Premium Movie World</h3>", unsafe_allow_html=True)

# Banner layout
banner_layout = """
<div style="display: flex; justify-content: center; gap: 5px; flex-wrap: wrap; margin-top: 5px;">
    <div style="flex: 1; min-width: 300px; max-width: 30%;">
        <script type="text/javascript">
            atOptions = {'key':'2f19140b5278570ad28374e5e4a7260d','format':'iframe','height':250,'width':600,'params':{}};
        </script>
        <script type="text/javascript" src="//www.highperformanceformat.com/2f19140b5278570ad28374e5e4a7260d/invoke.js"></script>
    </div>
</div>
"""
components.html(banner_layout, height=270)

# Scroll text
st.markdown("<p style='text-align:center;font-weight:bold;'>⬇️ Scroll Down To Watch ⬇️</p>", unsafe_allow_html=True)

# Countdown
smart_link = "https://www.effectivegatecpm.com/qibbz5efk?key=5f2f2e515dea23a4c38d317bca6b11c7"

query_params = st.query_params
video_id = query_params.get("id", "1")
video_link = get_video_link(video_id)

countdown_js = f"""
<div id="wrapper" style="text-align:center; font-family: sans-serif; padding: 10px; border: 2px dashed #E50914; border-radius: 10px; max-width: 95%; margin: auto;">
    <button id="startBtn" onclick="startProcess()" style="
        background-color: #E50914; color: white; padding: 15px;
        border: none; border-radius: 8px; cursor: pointer; font-size: 20px; width: 100%; font-weight: bold;">
        ▶️ WATCH FULL MOVIE NOW
    </button>

<div id="adModal" class="modal-overlay">
    <div class="modal-content">
        <span class="close-btn" onclick="closeModal()">× CLOSE</span>
        <iframe id="adFrame" src="" style="width:100%; height:90%; border:none;"></iframe>
    </div>
</div>

<div id="timerContainer" style="display:none; margin-top: 10px;">
    <p style="font-size: 16px; margin-bottom: 5px;">Loading Video... <span id="seconds">10</span>s</p>
    <div style="width: 100%; background-color: #ddd; border-radius: 5px;">
        <div id="progressBar" style="width: 0%; height: 10px; background-color: #E50914; border-radius: 5px; transition: width 1s linear;"></div>
    </div>
</div>

<a id="videoBtn" href="{video_link}" target="_blank" style="
    display: none !important; background-color: #28a745; color: white; padding: 15px;
    text-decoration: none; border-radius: 8px; font-size: 20px; width: 100%; font-weight: bold; margin-top: 10px;">
    ✅ CLICK HERE TO WATCH VIDEO
</a>
</div>

<script>
function startProcess() {
    document.getElementById('adFrame').src = {smart_link};
    document.getElementById('adModal').style.display = 'block';
    document.getElementById('startBtn').style.setProperty('display', 'none', 'important');
}

function closeModal() {
    document.getElementById('adModal').style.display = 'none';
    document.getElementById('adFrame').src = '';
    document.getElementById('timerContainer').style.display = 'block';
    startTimer();
}

function startTimer() {{
    let timeLeft = 10;
    let timerElement = document.getElementById('seconds');
    let progressBar = document.getElementById('progressBar');

    let countdown = setInterval(function() {
        timeLeft--;
        timerElement.textContent = timeLeft;
        progressBar.style.width = ((10 - timeLeft) * 10) + '%';

        if (timeLeft <= 0) {
            clearInterval(countdown);
            document.getElementById('videoBtn').style.setProperty('display', 'block', 'important');
            document.getElementById('timerContainer').style.display = 'none';
        }
    }, 1000);
}}
</script>
"""

components.html(countdown_js, height=260)
components.html(banner_layout, height=270)


























































