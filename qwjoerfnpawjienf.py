import streamlit as st

st.title("ogfmpae")

if "q" not in st.session_state:
    st.session_state.q = 1  
if "score" not in st.session_state:
    st.session_state.score = 0 
if "message" not in st.session_state:
    st.session_state.message = "" 

# 1問目
if st.session_state.q == 1:
    st.write("～前提～  遊ぶ？") 
    if st.button("遊ぶ"):
        st.session_state.score += 0  
        st.session_state.message = "正解！"
        st.session_state.q = 2  
    if st.button("遊ばない"):
        st.session_state.message = "え、あ、わかった"
        st.session_state.q = 9999  

# 2問目
elif st.session_state.q == 2:
    st.write("【利用規約読んだ？】") 
    if st.button("読んだ"):
        st.session_state.message = "正解！っておもった？ないよ"
        st.session_state.q = 99999  
    if st.button("読むわけがない"):
        st.session_state.score += 1
        st.session_state.message = "ないからあってるよ"
        st.session_state.q = 3  


elif st.session_state.q == 3:
    st.write("【ラスト】名前は藤本達也？") 
    if st.button("あってる"):
        st.session_state.score += 1  
        st.session_state.message = "ほんとに？まぁどっちにしろ先に進むけど"
        st.session_state.q = 4  
    if st.button("あってない"):
        st.session_state.score += 1  
        st.session_state.message = "だよね"
        st.session_state.q = 4  


elif st.session_state.q == 4:
    st.write("【車にタイヤは何個ある？】")  
    if st.button("4個"):
        st.session_state.score += 1 
        st.session_state.message = "正解！"
        st.session_state.q = 5  
    if st.button("5個"):
        st.session_state.score += 1 
        st.session_state.message = "スペアタイヤを数える発想はなかった"
        st.session_state.q = 5 


elif st.session_state.q == 5:
    st.write("???????????????")  
    if st.button("9"):
        st.session_state.score += 1 
        st.session_state.message = "正解！"
        st.session_state.q = 6 
    if st.button("広瀬すず"):
        st.session_state.score += 1  
        st.session_state.message = "あ、そう？そんな頭悪いん笑？"
        st.session_state.q = 9999  
    if st.button("マンション"):
        st.session_state.score += 1                 
        st.session_state.message = "あ、そう？そんな頭悪いん笑？"            
        st.session_state.q = 9999  
        
elif st.session_state.q == 6:
    st.write("???????????????")  
    if st.button("天然水"):
        st.session_state.score += 1 
        st.session_state.message = "あ、そう？そんな頭悪いん笑？"
        st.session_state.q = 7 
    if st.button("WI-FIルーター"):
        st.session_state.score += 1  
        st.session_state.message = "正解"
        st.session_state.q = 9999  
    if st.button("グッチ"):
        st.session_state.score += 1                 
        st.session_state.message = "あ、そう？そんな頭悪いん笑？"            
        st.session_state.q = 9999  


else:
    st.write("ゲーム終了！")      
    st.write("あなたの正解数:", st.session_state.score)
    st.write(st.session_state.message)
    if st.button("もう一回"):
        st.session_state.q = 1
        st.session_state.score = 0  
        st.session_state.message = ""  