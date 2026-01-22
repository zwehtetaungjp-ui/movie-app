import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Premium Movie Portal", layout="centered")

# --- ၁။ Banner Ads ---
# Adsterra မှ ရလာသော Banner Code ကို ဤနေရာတွင် ထည့်ပါ
ad_banner_code = """
<div style="text-align:center;">
    <script type="text/javascript">
        atOptions = {
            'key' : '6edd15a0ba83c13d90e58d064b3f416f',
            'format' : 'iframe',
            'height' : 90,
            'width' : 728,
            'params' : {}
        };
    </script>
    <script type="text/javascript" src="//www.highperformanceformat.com/6edd15a0ba83c13d90e58d064b3f416f/invoke.js"></script>
</div>
"""
components.html(ad_banner_code, height=100)

st.title("🔞 Premium Movie World")

# --- ၂။ Link များ သတ်မှတ်ခြင်း ---
smart_link = "https://www.effectivegatecpm.com/qibbz5efk?key=5f2f2e515dea23a4c38d317bca6b11c7"
video_link = "https://sl1nk.com/wVO8S"

st.warning("⚠️ ဗီဒီယိုကြည့်ရန် အောက်ကခလုတ်ကို နှိပ်ပါ။ ကြော်ငြာ Tab ပွင့်လာပြီး ၅ စက္ကန့်အကြာတွင် Video Link ပေါ်လာပါမည်။")

# --- ၃။ Countdown Timer နှင့် Button ပေါ်လာစေမည့် JavaScript ---
countdown_js = f"""
<div style="text-align:center; font-family: sans-serif;">
    
    <button id="startBtn" onclick="startProcess()" style="
        background-color: #E50914; color: white; padding: 18px 30px; 
        border: none; border-radius: 8px; cursor: pointer; font-size: 22px; width: 100%; font-weight: bold;">
        ▶️ WATCH MOVIE
    </button>

    <div id="timerContainer" style="display:none; margin-top: 20px;">
        <p style="font-size: 18px; color: #555;">Please wait <span id="seconds">5</span> seconds...</p>
        <div style="width: 100%; background-color: #ddd; border-radius: 5px;">
            <div id="progressBar" style="width: 0%; height: 10px; background-color: #E50914; border-radius: 5px; transition: width 1s linear;"></div>
        </div>
    </div>

    <a id="videoBtn" href="{video_link}" target="_blank" style="
        display:none; background-color: #28a745; color: white; padding: 18px 30px; 
        text-decoration: none; border-radius: 8px; font-size: 22px; width: 90%; font-weight: bold; margin-top: 20px; display: inline-block;">
        ✅ CLICK HERE TO WATCH VIDEO
    </a>
</div>

<script>
function startProcess() {{
    // ၁။ Ads ကို New Tab မှာဖွင့်မယ်
    window.open('{smart_link}', '_blank');

    // ၂။ ပင်မစာမျက်နှာမှာ ခလုတ်ကိုဖျောက်ပြီး Countdown ကိုပြမယ်
    document.getElementById('startBtn').style.display = 'none';
    document.getElementById('timerContainer').style.display = 'block';

    let timeLeft = 5;
    let timerElement = document.getElementById('seconds');
    let progressBar = document.getElementById('progressBar');

    let countdown = setInterval(function() {{
        timeLeft--;
        timerElement.textContent = timeLeft;
        progressBar.style.width = ((5 - timeLeft) * 20) + '%';

        if (timeLeft <= 0) {{
            clearInterval(countdown);
            document.getElementById('timerContainer').style.display = 'none';
            document.getElementById('videoBtn').style.display = 'inline-block';
        }}
    }}, 1000);
}}
</script>
"""

components.html(countdown_js, height=250)

st.write("---")
st.caption("How to watch: Click Watch Movie -> Wait 5s -> Click the Green Button.")

