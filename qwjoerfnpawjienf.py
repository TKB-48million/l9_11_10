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
    st.write("【第1問】空はどっち")  # 問題文
    if st.button("青い"):
        st.session_state.score += 1  # 正解
        st.session_state.message = "正解！"
        st.session_state.q = 2  # 次の問題へ
    if st.button("赤い"):
        st.session_state.message = "ちがうよ"
        st.session_state.q = 2  # 次の問題へ

# 2問目
elif st.session_state.q == 2:
    st.write("【第2問】ごはんを食べるのはどっち？")  # 問題文
    if st.button("口"):
        st.session_state.score += 1  # 正解
        st.session_state.message = "正解！"
        st.session_state.q = 3  # 終了画面へ
    if st.button("耳"):
        st.session_state.message = "ちがうよ"
        st.session_state.q = 3  # 終了画面へ

# 終了画面
else:
    st.write("ゲーム終了！")  # 終了メッセージ
    st.write("あなたの正解数:", st.session_state.score)  # 点数表示
    st.write(st.session_state.message)  # 最後の結果
    if st.button("もう一回"):
        st.session_state.q = 1  # 最初の問題に戻す
        st.session_state.score = 0  # 点数をリセット
        st.session_state.message = ""  # メッセージを消す