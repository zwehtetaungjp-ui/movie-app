import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Premium Movie Portal", layout="centered")

# --- ၁။ Adsterra Social Bar & Push Ads (Screen အနှံ့ ပေါ်လာမည့် ကြော်ငြာများ) ---
# Adsterra မှရသော Social Bar သို့မဟုတ် In-Page Push ကုဒ်ကို ဒီမှာထည့်ပါ
social_push_ads = """
<script type='text/javascript' src='https://pl28540401.effectivegatecpm.com/8b/6c/e4/8b6ce4814b6f7909e97fddc0fc571e00.js'></script>
"""
components.html(social_push_ads, height=0)

st.title("Premium Movie World")

# --- ၂။ Banner Ads နှစ်ခုကို ဘေးချင်းယှဉ်ပြခြင်း (Side-by-Side) ---
# သင့်ရဲ့ Banner Key နှစ်ခုကို အောက်တွင် ထည့်ပါ
banner_ads_layout = """
<div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
    <div style="border: 1px solid #ddd; padding: 5px;">
        <script type="text/javascript">
            atOptions = {'key' : 'Banner_Key_1', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {}};
        </script>
        <script type="text/javascript" src="//www.highperformanceformat.com/key1/invoke.js"></script>
    </div>

    <div style="border: 1px solid #ddd; padding: 5px;">
        <script type="text/javascript">
            atOptions = {'key' : 'Banner_Key_2', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {}};
        </script>
        <script type="text/javascript" src="//www.highperformanceformat.com/key2/invoke.js"></script>
    </div>
</div>
"""
components.html(banner_ads_layout, height=280)

# --- ၃။ အောက်ကိုကြည့်ရန် မြှားလေးများ (Scroll Down Indicator) ---
st.markdown("<h3 style='text-align: center;'>⬇️ Scroll Down To Watch ⬇️</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>👇 👇 👇</h1>", unsafe_allow_html=True)

# နေရာလွတ်ဖြစ်အောင် spacer ထည့်ခြင်း
st.write("##")
st.write("##")

# --- ၄။ Countdown Timer နှင့် ပင်မခလုတ် ---
smart_link = "https://www.effectivegatecpm.com/qibbz5efk?key=5f2f2e515dea23a4c38d317bca6b11c7"
video_link = "https://sl1nk.com/wVO8S"

countdown_js = f"""
<div id="wrapper" style="text-align:center; font-family: sans-serif; padding: 20px; border: 2px dashed #E50914; border-radius: 10px;">
    <button id="startBtn" onclick="startProcess()" style="
        background-color: #E50914; color: white; padding: 20px 30px; 
        border: none; border-radius: 8px; cursor: pointer; font-size: 24px; width: 100%; font-weight: bold;">
        ▶️ WATCH FULL MOVIE NOW
    </button>

    <div id="timerContainer" style="display:none; margin-top: 20px;">
        <p style="font-size: 18px; color: #555;">Processing... <span id="seconds">5</span>s</p>
        <div style="width: 100%; background-color: #ddd; border-radius: 5px;">
            <div id="progressBar" style="width: 0%; height: 12px; background-color: #E50914; border-radius: 5px; transition: width 1s linear;"></div>
        </div>
    </div>

    <a id="videoBtn" href="{video_link}" target="_blank" style="
        display: none !important; background-color: #28a745; color: white; padding: 20px 30px; 
        text-decoration: none; border-radius: 8px; font-size: 24px; width: 95%; font-weight: bold; margin-top: 20px;">
        ✅ CLICK TO DOWNLOAD / WATCH
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
        progressBar.style.width = ((5 - timeLeft) * 20) + '%';
        if (timeLeft <= 0) {{
            clearInterval(countdown);
            document.getElementById('timerContainer').style.display = 'none';
            document.getElementById('videoBtn').style.setProperty('display', 'inline-block', 'important');
        }}
    }}, 1000);
}}
</script>
"""
components.html(countdown_js, height=300)

# --- ၅။ အောက်ခြေတွင် နောက်ထပ် In-Page Push သို့မဟုတ် Banner တစ်ခု ထပ်ထည့်ခြင်း ---
st.write("##")
components.html(banner_ads_layout, height=280) # အပေါ်က banner layout ကိုပဲ ပြန်သုံးထားပါတယ်
