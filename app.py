import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Premium Movie Portal", layout="centered")

# --- ၁။ Social Bar & Video Ads (နေရာလွတ်တွေမှာ ပေါ်လာမည့် ကြော်ငြာ) ---
# Adsterra ကရလာတဲ့ Social Bar ကုဒ်ကို ဒီမှာ ထည့်ပါ
social_bar_code = """
<script type='text/javascript' src="https://pl28540401.effectivegatecpm.com/8b/6c/e4/8b6ce4814b6f7909e97fddc0fc571e00.js"></script>
"""
# ဤနေရာတွင် Social Bar သည် screen ရဲ့ ဘေး သို့မဟုတ် အောက်ခြေတွင် အလိုအလျောက် ပေါ်နေမည်ဖြစ်သည်
components.html(social_bar_code, height=0) 

# --- ၂။ Banner Ads (ထိပ်ဆုံးမှာပြရန်) ---
ad_banner_code = """
<div style="text-align:center;">
    <script type="text/javascript">
        atOptions = {
            'key' : '6edd15a0ba83c13d90e58d064b3f416f',
            'format' : 'iframe',
            'height' : 250,
            'width' : 300,
            'params' : {}
        };
    </script>
    <script type="text/javascript" src="//www.highperformanceformat.com/6edd15a0ba83c13d90e58d064b3f416f/invoke.js"></script>
</div>
"""
components.html(social_bar_code, height=260)

st.title(" Premium Movie World")

# --- ၃။ Countdown Timer Logic (ယခင်အတိုင်း) ---
smart_link = "https://www.effectivegatecpm.com/qibbz5efk?key=5f2f2e515dea23a4c38d317bca6b11c7"
video_link = "https://sl1nk.com/wVO8S"

st.warning("⚠️ ဗီဒီယိုကြည့်ရန် 'WATCH MOVIE' ကိုနှိပ်ပါ။ ကြော်ငြာကျော်ပြီး ၅ စက္ကန့်အကြာတွင် Video Link ပေါ်လာပါမည်။")

countdown_js = f"""
<div id="wrapper" style="text-align:center; font-family: sans-serif;">
    <button id="startBtn" onclick="startProcess()" style="
        background-color: #E50914; color: white; padding: 18px 30px; 
        border: none; border-radius: 8px; cursor: pointer; font-size: 22px; width: 100%; font-weight: bold; display: block;">
        ▶️ WATCH MOVIE
    </button>

    <div id="timerContainer" style="display:none; margin-top: 20px;">
        <p style="font-size: 18px; color: #555;">Please wait <span id="seconds">5</span> seconds...</p>
        <div style="width: 100%; background-color: #ddd; border-radius: 5px;">
            <div id="progressBar" style="width: 0%; height: 10px; background-color: #E50914; border-radius: 5px; transition: width 1s linear;"></div>
        </div>
    </div>

    <a id="videoBtn" href="{video_link}" target="_blank" style="
        display: none !important; background-color: #28a745; color: white; padding: 18px 30px; 
        text-decoration: none; border-radius: 8px; font-size: 22px; width: 90%; font-weight: bold; margin-top: 20px;">
        ✅ CLICK HERE TO WATCH VIDEO
    </a>
</div>

<script>
function startProcess() {{
    window.open('{smart_link}', '_blank');
    document.getElementById('startBtn').style.setProperty('display', 'none', 'important');
    document.getElementById('timerContainer').style.display = 'block';

    let timeLeft = 5;
    let timerElement = document.getElementById('seconds');
    let progressBar = document.getElementById('progressBar');

    let countdown = setInterval(function() {{
        timeLeft--;
        timerElement.textContent = timeLeft;
        progressBar.style.width = ((9 - timeLeft) * 20) + '%';
        if (timeLeft <= 0) {{
            clearInterval(countdown);
            document.getElementById('timerContainer').style.display = 'none';
            document.getElementById('videoBtn').style.setProperty('display', 'inline-block', 'important');
        }}
    }}, 1000);
}}
</script>
"""
components.html(countdown_js, height=250)

# --- ၄။ အောက်ခြေနေရာလွတ်တွင် Banner တစ်ခု ထပ်ထည့်ခြင်း ---
components.html(ad_banner_code, height=260)



