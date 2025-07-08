import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")
st.title("📉 미적분 기반 경사하강법 시뮬레이터")
st.markdown("""
- 함수: $f(x) = (x - 3)^2 + 1$
- 목표: 경사하강법으로 **최솟값(x=3)**을 찾기
- 미분: $f'(x) = 2(x - 3)$
""")

# 사용자 입력
init_x = st.slider("🎯 시작 위치 x₀", -5.0, 5.0, 0.0, step=0.1)
lr = st.slider("📉 학습률 (Learning Rate)", 0.001, 1.0, 0.1)
epochs = st.slider("🔁 반복 횟수 (Epoch)", 1, 50, 25)
run = st.button("🚀 시뮬레이션 실행")

# 함수 및 도함수
def f(x):
    return (x - 3)**2 + 1

def df(x):
    return 2 * (x - 3)

if run:
    x = init_x
    x_history = [x]
    y_history = [f(x)]

    for _ in range(epochs):
        x -= lr * df(x)
        x_history.append(x)
        y_history.append(f(x))

    # 시각화
    x_vals = np.linspace(-5, 8, 400)
    y_vals = f(x_vals)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x_vals, y_vals, label="f(x) = (x - 3)^2 + 1", color='blue')
    ax.plot(x_history, y_history, linestyle="--", color="gray")
    ax.scatter(x_history, y_history, color="red", label="경사하강법 경로")
    ax.set_title("경사하강법을 통한 최소값 탐색")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    st.success(f"✅ 최종 최소값에 수렴한 x ≈ {x_history[-1]:.4f}")
    st.info(f"🧠 실제 최소값은 x = 3이며, 함수값 f(x) = 1 입니다.")
