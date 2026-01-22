import streamlit as st
import streamlit.components.v1 as components

# Layout ကို ကျစ်ကျစ်လျစ်လျစ် ဖြစ်အောင် CSS ထည့်ခြင်း
st.set_page_config(page_title="Premium Movie Portal", layout="centered")

st.markdown("""
    <style>
    .block-container { padding-top: 1rem; padding-bottom: 0rem; }
    .stMarkdown { margin-bottom: -1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- ၁။ Social Bar & Popunder (ဝင်ငွေအကောင်းဆုံး ads များ) ---
# Adsterra မှရသော ကုဒ်များကို ဒီမှာ စုထည့်ပါ
ads_scripts = """
<script type='text/javascript' src='//pl28540401.effectivegatecpm.com/8b/6c/e4/8b6ce4814b6f7909e97fddc0fc571e00.js'></script>
<script type='text/javascript' src='//pl28541110.effectivegatecpm.com/61/73/00/6173009a89d5198b3e1211b7d30b25be.js'></script>
"""
components.html(ads_scripts, height=0)

# --- ၂။ Title နှင့် Banner Ads (ဘေးချင်းယှဉ်) ---
st.markdown("<h2 style='text-align: center; margin-bottom: 0px;'>🔞 Premium Movie World</h2>", unsafe_allow_html=True)

# Banner 300x250 နှစ်ခုကို ဘေးချင်းယှဉ်ပြရန်
banner_layout = """
<div style="display: flex; justify-content: center; gap: 5px; margin-top: 10px;">
    <div>
        <script type="text/javascript">
            atOptions = {'key' : '6edd15a0ba83c13d90e58d064b3f416f', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {}};
        </script>
        <script type="text/javascript" src="//www.highperformanceformat.com/6edd15a0ba83c13d90e58d064b3f416f/invoke.js"></script>
    </div>
    <div>
        <script type="text/javascript">
            atOptions = {'key' : '6edd15a0ba83c13d90e58d064b3f416f', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {}};
        </script>
        <script type="text/javascript" src="//www.highperformanceformat.com/6edd15a0ba83c13d90e58d064b3f416f/invoke.js"></script>
    </div>
</div>
"""
components.html(banner_layout, height=260)

# --- ၃။ Scroll Indicator (မြှားလေးများ) ---
st.markdown("<p style='text-align: center; font-size: 20px; font-weight: bold; margin-top: 0px;'>⬇️ Scroll Down To Watch ⬇️<br>👇 👇 👇</p>", unsafe_allow_html=True)

# အောက်ကို scroll ဆွဲစေချင်ရင် နေရာလွတ်အနည်းငယ်ပဲ ထားပါ
st.write("") 

# --- ၄။ Countdown Timer နှင့် Button ---
smart_link = "https://www.effectivegatecpm.com/qibbz5efk?key=5f2f2e515dea23a4c38d317bca6b11c7"
video_link = "https://sl1nk.com/wVO8S"

countdown_js = f"""
<div id="wrapper" style="text-align:center; font-family: sans-serif; padding: 15px; border: 2px dashed #E50914; border-radius: 10px;">
    <button id="startBtn" onclick="startProcess()" style="
        background-color: #E50914; color: white; padding: 18px 30px; 
        border: none; border-radius: 8px; cursor: pointer; font-size: 22px; width: 100%; font-weight: bold;">
        ▶️ WATCH FULL MOVIE NOW
    </button>

    <div id="timerContainer" style="display:none; margin-top: 15px;">
        <p style="font-size: 16px;">Processing... <span id="seconds">5</span>s</p>
        <div style="width: 100%; background-color: #ddd; border-radius: 5px;">
            <div id="progressBar" style="width: 0%; height: 10px; background-color: #E50914; border-radius: 5px; transition: width 1s linear;"></div>
        </div>
    </div>

    <a id="videoBtn" href="{video_link}" target="_blank" style="
        display: none !important; background-color: #28a745; color: white; padding: 18px 30px; 
        text-decoration: none; border-radius: 8px; font-size: 22px; width: 95%; font-weight: bold; margin-top: 15px; display: inline-block;">
        ✅ CLICK TO WATCH VIDEO
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
components.html(countdown_js, height=280)

# --- ၅။ အောက်ခြေတွင် Push Ads ပြရန်နေရာ ---
st.markdown("<p style='text-align: center; color: gray;'>ADVERTISEMENT</p>", unsafe_allow_html=True)
components.html(banner_layout, height=260)
