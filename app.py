import streamlit as st

st.set_page_config(
    page_title="統合のお知らせ",
    layout="centered"
)

st.title("遅延損失単価設計ツール")

st.info(
    "本ツールは『物流デジタルツイン診断』内へ統合しました。"
)

st.markdown(
    """
    ### 新しいアクセス先

    https://logistics.victorconsulting.jp

    左メニューより  
    「遅延損失単価設計」  
    を選択してください。
    """
)

st.link_button(
    "物流デジタルツイン診断へ移動",
    "https://logistics.victorconsulting.jp"
)
