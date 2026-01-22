import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Premium Movie World", layout="centered")

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
# သင့်ရဲ့ Adsterra Smart Link နှင့် Video Link များကို အောက်တွင် အစားထိုးပါ
smart_link = "https://www.effectivegatecpm.com/qibbz5efk?key=5f2f2e515dea23a4c38d317bca6b11c7"
video_link = "https://sl1nk.com/wVO8S"

st.info("အောက်ကခလုတ်ကို နှိပ်လိုက်လျှင် ကြော်ငြာနှင့် ဗီဒီယိုတို့သည် Tab အသစ်များတွင် ပွင့်လာပါလိမ့်မည်။")

# --- ၃။ Tab အသစ် (New Tab) များဖြင့် ပွင့်စေမည့် ခလုတ် ---
js_button = f"""
<script>
function playMovie() {{
    // Ads ကို Tab အသစ်မှာ ဖွင့်သည်
    window.open('{smart_link}', '_blank'); 
    
    // Video ကိုလည်း နောက်ထပ် Tab အသစ်တစ်ခုဖြင့် ဖွင့်သည်
    window.open('{video_link}', '_blank');
}}
</script>

<div style="text-align:center;">
    <button onclick="playMovie()" style="
        background-color: #E50914; 
        color: white; 
        padding: 20px 40px; 
        border: none; 
        border-radius: 10px; 
        cursor: pointer; 
        font-size: 24px; 
        width: 100%; 
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    ">
        ▶️ CLICK TO WATCH NOW (NEW TAB)
    </button>
</div>
"""
components.html(js_button, height=150)

st.write("---")
st.caption("ကိုယ်တိုင်စမ်းသပ်ကြည့်ရန် ခလုတ်ကို တစ်ချက်နှိပ်လိုက်ပါ။")
