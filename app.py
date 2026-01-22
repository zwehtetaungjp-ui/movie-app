import streamlit as st

st.set_page_config(page_title="Movie World", layout="centered")

st.title("🔞 Premium Movie Portal")
st.write("ရုပ်ရှင်ကြည့်ရန် အောက်က 'Watch Now' ခလုတ်ကို နှိပ်ပါ။")

# ၁။ Adsterra Smart Link (ဒီမှာ သင့်ရဲ့ Smart Link ကို ထည့်ပါ)
ad_link = "https://www.effectivegatecpm.com/qibbz5efk?key=5f2f2e515dea23a4c38d317bca6b11c7"

# ၂။ မူရင်း Video Link (ဒီမှာ ရုပ်ရှင် Link အစစ်ကို ထည့်ပါ)
video_link = "https://sl1nk.com/wVO8S"

st.image("https://via.placeholder.com/600x350?text=Click+To+Watch+Movie")

# ခလုတ်ကို နှိပ်လိုက်တဲ့အခါ
if st.button("🚀 Watch Full Movie Now"):
    # ဤနေရာတွင် User ကို ကြော်ငြာ Link အရင်ပြပါမည်
    st.markdown(f"### [၁။ ဒီနေရာကိုနှိပ်ပြီး ကြော်ငြာကျော်ပါ]({ad_link})")
    
    # ကြော်ငြာကျော်ပြီးမှ ဗီဒီယိုကြည့်နိုင်ရန် Link ကို အောက်တွင် ပြပေးထားပါ
    st.success("ကြော်ငြာကြည့်ပြီးပါက အောက်က Link တွင် ဗီဒီယိုကြည့်နိုင်ပါပြီ 👇")
    st.markdown(f"*[၂။ ရုပ်ရှင်ကြည့်ရန် ဤနေရာကိုနှိပ်ပါ]({video_link})*")
    
    st.info("မှတ်ချက် - ကြော်ငြာ tab ကို ပိတ်ပြီး မူရင်း page သို့ ပြန်လာပေးပါ။")


