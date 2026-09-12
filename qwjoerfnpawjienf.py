import streamlit as st

st.title("ogfmpae")

st.header("このゲームを遊びますか?")

# 進行状況を覚える箱を作る
if "q" not in st.session_state:
    st.session_state.q = 1  # 今は1問目
if "score" not in st.session_state:
    st.session_state.score = 0  # 正解数
if "message" not in st.session_state:
    st.session_state.message = ""  # 結果メッセージ

# 1問目
if st.session_state.q == 1:
    st.write("～前提～  遊ぶ？")  # 問題文
    if st.button("遊ぶ"):
        st.session_state.score += 0  # 正解
        st.session_state.message = "正解！"
        st.session_state.q = 2  # 次の問題へ
    if st.button("遊ばない"):
        st.session_state.message = "え、あ、わかった"
        st.session_state.q = 5  # 次の問題へ

# 2問目
elif st.session_state.q == 2:
    st.write("【利用規約読んだ？】")  # 問題文
    if st.button("読んだ"):
        st.session_state.score += 1  # 正解
        st.session_state.message = "正解！っておもった？ないよ"
        st.session_state.q = 3  
    if st.button("読むわけがない"):
        st.session_state.message = "ないからあってるよ"
        st.session_state.q = 3  


elif st.session_state.q == 3:
    st.write("【ラスト】名前は藤本達也？")  # 問題文
    if st.button("あってる"):
        st.session_state.score += 1  # 正解
        st.session_state.message = "ほんとに？まぁどっちにしろ先に進むけど"
        st.session_state.q = 4  # 終了画面へ
    if st.button("あってない"):
        st.session_state.message = "だよね"
        st.session_state.q = 4  # 終了画面へ


elif st.session_state.q == 4:
    st.write("【車にタイヤは何個ある？】")  # 問題文
    if st.button("4個"):
        st.session_state.score += 1  # 正解
        st.session_state.message = "正解！"
        st.session_state.q = 6  # 終了画面へ
    if st.button("5個"):
        st.session_state.message = "スペアタイヤを数える発想はなかった"
        st.session_state.q = 6  # 終了画面へ

# 終了画面
else:
    st.write("ゲーム終了！")  # 終了メッセージ
    st.write("あなたの正解数:", st.session_state.score)  # 点数表示
    st.write(st.session_state.message)  # 最後の結果
    if st.button("もう一回"):
        st.session_state.q = 1  # 最初の問題に戻す
        st.session_state.score = 0  # 点数をリセット
        st.session_state.message = ""  # メッセージを消す