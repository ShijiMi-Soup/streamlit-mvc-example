import streamlit as st
import model

ph = model.PostHandler()
posts = ph.read()

def add_post(content):
    """投稿を追加する"""

    global posts

    ph.add(content)
    posts = ph.read()

def update_post(post_id, new_content):
    """投稿を更新する"""

    global posts

    ph.update(
        post_id,
        new_content
    )
    posts = ph.read()

def delete_post(post_id):
    """投稿を削除する"""
    
    global posts

    ph.delete(
        post_id
    )
    posts = ph.read()