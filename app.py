import streamlit as st

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

st.title("遅延損失単価設計ツール")

# --- 第1層 ---
st.header("① 直接追加コスト")

time_option = st.selectbox(
    "追加作業時間",
    ["0〜2分", "3〜5分", "6〜10分", "10分以上", "自由入力"]
)

custom_time = 0
if time_option == "自由入力":
    custom_time = st.number_input("追加作業時間（分）", min_value=0.0)

time_map = {
    "0〜2分": 1,
    "3〜5分": 4,
    "6〜10分": 8,
    "10分以上": 12
}

additional_minutes = custom_time if time_option == "自由入力" else time_map.get(time_option, 0)

hourly_wage = st.number_input("現場担当者の時給（円）", min_value=0.0)
external_cost = st.number_input("外部追加実費（円）", min_value=0.0)

direct_labor_cost = (additional_minutes / 60) * hourly_wage
direct_cost = direct_labor_cost + external_cost

# --- 第2層 ---
st.header("② 間接オペレーション負荷")

indirect_time_option = st.selectbox(
    "問い合わせ・社内調整時間",
    ["0〜2分", "3〜5分", "6〜10分", "10分以上", "自由入力"]
)

custom_indirect = 0
if indirect_time_option == "自由入力":
    custom_indirect = st.number_input("調整時間（分）", min_value=0.0)

indirect_minutes = custom_indirect if indirect_time_option == "自由入力" else time_map.get(indirect_time_option, 0)

staff_wage = st.number_input("対応担当者の時給（円）", min_value=0.0)

manager_ratio = st.selectbox("上長確認発生割合",
    ["0%", "10%", "50%", "80%", "自由入力"]
)

ratio_map = {"0%": 0, "10%": 0.1, "50%": 0.5, "80%": 0.8}
custom_ratio = 0
if manager_ratio == "自由入力":
    custom_ratio = st.number_input("発生割合（%）", min_value=0.0) / 100

ratio = custom_ratio if manager_ratio == "自由入力" else ratio_map.get(manager_ratio, 0)

manager_time = st.number_input("上長対応時間（分）", min_value=0.0)
manager_wage = st.number_input("上長時給（円）", min_value=0.0)

indirect_cost = ((indirect_minutes / 60) * staff_wage) + \
                ((manager_time / 60) * manager_wage * ratio)

# --- 第3層 ---
st.header("③ 顧客価値毀損（期待値）")

gross_profit = st.number_input("平均粗利（円）", min_value=0.0)

rate_option = st.selectbox(
    "リピート低下率",
    ["0%", "0.5%", "1%", "2%", "5%", "自由入力"]
)

rate_map = {"0%": 0, "0.5%": 0.005, "1%": 0.01, "2%": 0.02, "5%": 0.05}

custom_rate = 0
if rate_option == "自由入力":
    custom_rate = st.number_input("低下率（%）", min_value=0.0) / 100

rate = custom_rate if rate_option == "自由入力" else rate_map.get(rate_option, 0)

value_loss = gross_profit * rate

# --- 合計 ---
total_loss = direct_cost + indirect_cost + value_loss

st.markdown("---")
st.write(f"直接追加コスト：{direct_cost:,.0f}円")
st.write(f"間接オペレーション負荷：{indirect_cost:,.0f}円")
st.write(f"顧客価値毀損（期待値）：{value_loss:,.0f}円")
st.markdown("---")
st.write(f"遅延1件あたり損失単価：{total_loss:,.0f}円")
st.markdown("---")
st.caption("※本結果は入力値に基づく設計値です。")
