import streamlit as st
import controller as ctrl

# ページ設定
st.set_page_config(
    page_title="チャット", 
    page_icon="💬"
)

# タイトル
st.title("💬 チャット")
st.session_state.edit_post_id = None

# データベース
with st.expander("データベース"):
    ctrl.posts

# 1つの投稿
def show_post(post):
    # 投稿
    with st.chat_message("user"):
        post_id = post["PostId"]
        content = post["Content"]

        # 本文
        st.write(content)

        # 編集ボタン
        with st.popover("編集", icon=":material/edit:"):
            # フォーム
            with st.form(f"form_{index}", border=False):
                # テキスト入力
                new_content = st.text_area("本文を修正", value=content)
                
                # 更新ボタン
                if st.form_submit_button("更新"):
                    # 投稿を更新する
                    ctrl.update_post(post_id, new_content)

                    # 画面を更新
                    st.rerun()

        # 削除ボタン
        if st.button(
            "削除", 
            key=f"del_{index}", 
            icon=":material/delete:",
            # on_click=handle_delete
        ):
            # 投稿を削除する
            ctrl.delete_post(post_id)

            # 画面を更新
            st.rerun()

# 複数の投稿を表示
for index, post in ctrl.posts.sort_values(by=["PostId"], ascending=True).iterrows():
    show_post(post)

# チャット入力
if content := st.chat_input(key="post_input"):
    ctrl.add_post(content)
    st.rerun()