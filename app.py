import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

def get_video_link(v_id):
    # သင့်ရဲ့ Google Sheet CSV URL ကို ဒီမှာ အစားထိုးပါ
    SHEET_URL = "https://docs.google.com/spreadsheets/d/1l4WfVPjS-waC0zpzwMswKbzdOBv28P_RcG1R5WGTPYs/export?format=csv"
    try:
        df = pd.read_csv(SHEET_URL)
        # Sheet ထဲက id နဲ့ တူတာကို ရှာတာပါ
        result = df[df['id'].astype(str) == str(v_id)]
        if not result.empty:
            return result.iloc[0]['video_url']
    except Exception as e:
        st.error(f"Error reading sheet: {e}")
    return "https://www4.javhdporn.net/video/ongp-087/" # ရှာမတွေ့ရင် ပြမယ့် Default Link
# Layout အကွာအဝေးများကို ချုံ့ရန် CSS
st.set_page_config(page_title="Premium Movie Portal", layout="centered")
st.markdown("""
<style>
    .block-container { padding-top: 2rem; padding-bottom: 0rem; max-width: 75%; }
    div.stButton > button { width: 100%; }
    iframe { max-width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- ၁။ Adsterra Social Bar & Popunder ---
ads_scripts = """
<script type='text/javascript' src='//pl28540401.effectivegatecpm.com/8b/6c/e4/8b6ce4814b6f7909e97fddc0fc571e00.js'></script>
<script type='text/javascript' src='//pl28541110.effectivegatecpm.com/61/73/00/6173009a89d5198b3e1211b7d30b25be.js'></script>
"""
components.html(ads_scripts, height=0)

# --- ၂။ Title နှင့် Banner Ads (Responsive Layout) ---
st.markdown("<h3 style='text-align: center; margin-bottom: 0px;'> MURASAKI</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; margin-bottom: 0px;'> Premium Movie World</h3>", unsafe_allow_html=True)

# Banner များကို ဘောင်မကျော်အောင် width: 100% နှင့် flex-wrap သုံးထားသည်
banner_layout = """
<div style="display: flex; justify-content: center; gap: 5px; flex-wrap: wrap; margin-top: 5px;">
    <div style="flex: 1; min-width: 300px; max-width: 30%;">
        <script type="text/javascript">
            atOptions = {'key' : '2f19140b5278570ad28374e5e4a7260d', 'format' : 'iframe', 'height' : 250, 'width' : 600, 'params' : {}};
        </script>
        <script type="text/javascript" src="//www.highperformanceformat.com/2f19140b5278570ad28374e5e4a7260d/invoke.js"></script>
    </div>
    <div style="flex: 1; min-width: 300px; max-width: 320px;">
        <script type="text/javascript">
            atOptions = {'key' : '2f19140b5278570ad28374e5e4a7260d', 'format' : 'iframe', 'height' : 250, 'width' : 600, 'params' : {}};
        </script>
        <script type="text/javascript" src="//www.highperformanceformat.com/2f19140b5278570ad28374e5e4a7260d/invoke.js"></script>
    </div>
    <div style="flex: 1; min-width: 300px; max-width: 320px;">
        <script type="text/javascript">
            atOptions = {'key' : '2f19140b5278570ad28374e5e4a7260d', 'format' : 'iframe', 'height' : 250, 'width' : 600, 'params' : {}};
        </script>
        <script type="text/javascript" src="//www.highperformanceformat.com/2f19140b5278570ad28374e5e4a7260d/invoke.js"></script>
    </div>
</div>
"""
components.html(banner_layout, height=270)

# --- ၃။ Scroll Indicator (နေရာလွတ်လျှော့ချထားသည်) ---
st.markdown("<p style='text-align: center; font-weight: bold; margin: 0px;'>⬇️ Scroll Down To Watch ⬇️<br>👇 👇 👇<br>👇 👇 👇<br>⬇️ Scroll Down To Watch ⬇️<br>👇 👇 👇<br>👇 👇 👇<br>⬇️ Scroll Down To Watch ⬇️<br>👇 👇 👇<br>👇 👇 👇<br>⬇️ Scroll Down To Watch ⬇️<br>👇 👇 👇<br>👇 👇 👇</p>", unsafe_allow_html=True)
# --- ၄။ Countdown Timer (၁၀ စက္ကန့် စောင့်ခိုင်းရန် ပြင်ဆင်ထားသည်) ---
smart_link = "https://www.effectivegatecpm.com/qibbz5efk?key=5f2f2e515dea23a4c38d317bca6b11c7"

# URL ကနေ ?id=... ဆိုတာကို ဖတ်ခိုင်းတာပါ
query_params = st.query_params
video_id = query_params.get("id", "1") # id မပါရင် အမှတ် ၁ ကို ပြမယ်

# Google Sheet ထဲကနေ အဲ့ဒီ id ရဲ့ Link ကို သွားရှာခိုင်းတဲ့ ကုဒ်ပါ
video_link = get_video_link(video_id)

# ခလုတ်ကို ဘောင်အတွင်းထဲပဲရှိနေစေရန် width ကို 90% ဝန်းကျင်ထားထားသည်
countdown_js = f"""
<div id="wrapper" style="text-align:center; font-family: sans-serif; padding: 10px; border: 2px dashed #E50914; border-radius: 10px; max-width: 95%; margin: auto;">
    <button id="startBtn" onclick="startProcess()" style="
        background-color: #E50914; color: white; padding: 15px; 
        border: none; border-radius: 8px; cursor: pointer; font-size: 20px; width: 100%; font-weight: bold;">
        ▶️ WATCH FULL MOVIE NOW
    </button>

    <div id="timerContainer" style="display:none; margin-top: 10px;">
        <p style="font-size: 16px; margin-bottom: 5px;">Loading Video... <span id="seconds">10</span>s</p>
        <div style="width: 100%; background-color: #ddd; border-radius: 5px;">
            <div id="progressBar" style="width: 0%; height: 10px; background-color: #E50914; border-radius: 5px; transition: width 1s linear;"></div>
        </div>
    </div>

    <a id="videoBtn" href="{video_link}" target="_blank" style="
        display: none !important; background-color: #28a745; color: white; padding: 15px; 
        text-decoration: none; border-radius: 8px; font-size: 20px; width: 100%; font-weight: bold; margin-top: 10px; box-sizing: border-box;">
        ✅ CLICK HERE TO WATCH VIDEO
    </a>
</div>
<script>
function startProcess() {{
let adWindow; # Window ကို သိမ်းရန် variable

function startProcess() {
    #Window အသစ်ဖွင့်ပြီး variable ထဲသိမ်းထားမယ်
    adWindow = window.open('{smart_link}', '_blank');
    
    document.getElementById('startBtn').style.setProperty('display', 'none', 'important');
    document.getElementById('timerContainer').style.display = 'block';
    
    # ... ကျန်တဲ့ timer code များ ...
     let timeLeft = 10; # ဒီမှာ ၁၀ စက္ကန့်သို့ ပြောင်းထားသည်
    let timerElement = document.getElementById('seconds');
    let progressBar = document.getElementById('progressBar');
    
    let countdown = setInterval(function() {{
        timeLeft--;
        timerElement.textContent = timeLeft;
        progressBar.style.width = ((10 - timeLeft) * 10) + '%';
        
        if (timeLeft <= 0) {{
            clearInterval(countdown);
            document.getElementById('timerContainer').style.display = 'none';
            document.getElementById('videoBtn').style.setProperty('display', 'block', 'important');
        }}
    }}, 1000);
}

# ပိတ်မယ့် function (ဒီ function ကို ခလုတ်အသစ်မှာ ချိတ်ပါ)
function closeAdAndReturn() {
    if (adWindow) {
        adWindow.close(); # ပွင့်နေတဲ့ tab ကို ပိတ်မယ်
    }
}
    
   
}}
</script>
"""
components.html(countdown_js, height=260)
components.html(banner_layout, height=270)
















































