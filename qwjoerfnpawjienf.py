import streamlit as st

st.title("ogfmpae")

if "q" not in st.session_state:
    st.session_state.q = 1  
if "score" not in st.session_state:
    st.session_state.score = 0 
if "message" not in st.session_state:
    st.session_state.message = "" 


if st.session_state.q == 1:
    st.write("～前提～ 遊ぶ？")
    if st.button("遊ぶ"):
        st.session_state.message = "正解！"
        st.session_state.score += 0
        st.session_state.q = 2
    if st.button("遊ばない"):
        st.session_state.message = "え、あ、わかった"
        st.session_state.q = 9999

elif st.session_state.q == 2:
    st.write(st.session_state.message)
    st.write("続けますか？")
    if st.button("はい"):
        st.session_state.q = 3

elif st.session_state.q == 3:
    st.write("【利用規約読んだ？】")
    if st.button("読んだ"):
        st.session_state.q = 9999
    if st.button("読むわけがない"):
        st.session_state.message = "ないからあってるよ"
        st.session_state.score += 1
        st.session_state.q = 4

elif st.session_state.q == 4:
    st.write(st.session_state.message)
    st.write("続けますか？")
    if st.button("はい"):
        st.session_state.q = 5

elif st.session_state.q == 5:
    st.write("【ラスト】名前は藤本達也？")
    if st.button("あってる"):
        st.session_state.message = "ほんとにそう？まあどっちみち続けるけど…"
        st.session_state.score += 1
        st.session_state.q = 123456789
    if st.button("あってない"):
        st.session_state.score += 1
        st.session_state.message = "まぁそうだわな"
        st.session_state.q = 6

elif st.session_state.q == 123456789:
    st.write(st.session_state.message)
    st.write("続けますか？")
    if st.button("はい"):
        st.session_state.q = 7

elif st.session_state.q == 6:
    st.write(st.session_state.message)
    st.write("続けますか？")
    if st.button("はい"):
        st.session_state.q = 7

elif st.session_state.q == 7:
    st.write("【車にタイヤは何個ある？】")
    if st.button("4個"):
        st.session_state.message = "特殊な車は考えない場合正解"
        st.session_state.score += 1
        st.session_state.q = 1234567890
    if st.button("5個"):
        st.session_state.message = "スペアタイヤ入れるとはその発想はなかった"
        st.session_state.score += 1
        st.session_state.q = 8


elif st.session_state.q == 1234567890:
    st.write(st.session_state.message)
    st.write("続けますか？")
    if st.button("はい"):
        st.session_state.q = 9

elif st.session_state.q == 8:
    st.write(st.session_state.message)
    st.write("続けますか？")
    if st.button("はい"):
        st.session_state.q = 9

elif st.session_state.q == 9:
    st.write("???????????????")
    if st.button("9"):
        st.session_state.message = "すごい！とか書きたいけど普通に三択だからね。別にすごくない"
        st.session_state.score += 1
        st.session_state.q = 10
    if st.button("広瀬すず"):
        st.session_state.message = "あ、そう？そんな頭悪いん笑？"
        st.session_state.q = 9999
    if st.button("マンション"):
        st.session_state.message = "あ、そう？そんな頭悪いん笑？"
        st.session_state.q = 9999

elif st.session_state.q == 10:
    st.write(st.session_state.message)
    st.write("続けますか？")
    if st.button("はい"):
        st.session_state.q = 11

elif st.session_state.q == 11:
    st.write("???????????????")
    if st.button("天然水"):
        st.session_state.score += 1
        st.session_state.message = "2回連続でも11%ほどだからな"
        st.session_state.q = 12
    if st.button("WI-FIルーター"):
        st.session_state.message = "正解"
        st.session_state.q = 9999
    if st.button("グッチ"):
        st.session_state.message = "あ、そう？そんな頭悪いん笑？"
        st.session_state.q = 9999

elif st.session_state.q == 12:
    st.write(st.session_state.message)
    st.write("続けますか？")
    if st.button("はい"):
        st.session_state.q = 13

else:
    st.write("ゲーム終了！")
    st.write("あなたの正解数:", st.session_state.score)
    st.write(st.session_state.message)
    if st.button("もう一回"):
        st.session_state.q = 1
        st.session_state.score = 0
        st.session_state.message = ""