import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Movie Portal", layout="centered")

# --- ၁။ Banner Ads ထည့်သွင်းခြင်း ---
# Adsterra ကရတဲ့ Banner Script Code ကို ဒီနေရာမှာ ထည့်ပါ
ad_banner_code = """
<div style="text-align:center;">
    <script type="text/javascript">
        atOptions = {
            'key' : 'သင့်ရဲ့_banner_key',
            'format' : 'iframe',
            'height' : 90,
            'width' : 720,
            'params' : {}
        };
    </script>
    <script type="text/javascript" src="//www.highperformanceformat.com/သင့်ရဲ့_key/invoke.js"></script>
    </div>
"""
components.html(ad_banner_code, height=100)

st.title("🔞 Premium Movie World")
st.image("https://via.placeholder.com/600x300?text=Premium+Movie+Thumbnail")

# --- ၂။ Link နှိပ်လျှင် Ads တက်ပြီး Video ဆီ တိုက်ရိုက်သွားမည့် ခလုတ် ---
# သင့်ရဲ့ Link များဖြင့် အစားထိုးပါ
ad_link = "https://သင့်ရဲ့_adsterra_smart_link"
video_link = "https://သင့်ရဲ့_video_link_အစစ်"

# JavaScript သုံးပြီး Tab နှစ်ခု တစ်ပြိုင်တည်း ဖွင့်နည်း
# Window.open ကို နှစ်ခါသုံးထားခြင်းဖြစ်သည်
js_code = f"""
<script>
function openLinks() {{
    window.open('{ad_link}', '_blank'); // ကြော်ငြာကို Tab အသစ်ဖြင့်ဖွင့်သည်
    window.location.href = '{video_link}'; // မူရင်း Tab ကို Video Link ဆီ ပို့သည်
}}
</script>
<button onclick="openLinks()" style="
    background-color: #ff4b4b;
    color: white;
    padding: 15px 32px;
    font-size: 20px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    width: 100%;
">
    🚀 Watch Full Movie Now (Server 1)
</button>
"""

components.html(js_code, height=100)

st.write("---")
st.info("မှတ်ချက် - ခလုတ်နှိပ်ပြီးနောက် ပွင့်လာသော ကြော်ငြာ Tab ကို ပိတ်၍ ရုပ်ရှင်ကို ကြည့်ရှုနိုင်ပါသည်။")
