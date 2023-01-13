import streamlit as st

# Create a list of questions and answers
questions = [
    {
        "question": "流通情報工学科は何学部？",
        "answers": ["海洋工学部", "海洋資源環境学部", "海洋生命科学部"],
        "correct": "海洋工学部"
    },
    {
        "question": "海洋環境学科は何学部？",
        "answers": ["海洋工学部", "海洋資源環境学部", "海洋生命科学部"],
        "correct": "海洋資源環境学部"
    },
    {
        "question": "海洋政策文化学科は何学部？",
        "answers": ["海洋工学部", "海洋資源環境学部", "海洋生命科学部"],
        "correct": "海洋生命科学部"
    }
]

# Create a variable to keep track of the score
score_count = 0

# Create a function to display the quiz
score_count = 0
def quiz():
    for q in questions:
        st.write(q["question"])
        user_answer = st.radio("", q["answers"], key=q["question"])
        if user_answer == q["correct"]:
            st.write("Correct!")
            global score_count
            score_count += 1
        else:
            st.write("Incorrect.")
    if score_count == len(questions):
        st.success("Congratulations! You got all the questions correct.")
        st.balloons()
    else:
        st.error("you got only {} of {} correct". format(score_count, len(questions)))

# Create a function to display the score
def score():
    st.write("You got", score_count, "out of", len(questions), "correct.")

# Create the Streamlit app
def app():
    st.set_page_config(page_title="Qiuz app", page_icon=":guardsman:", layout="wide")
    st.title("海洋大のクイズ")
    quiz()
    score()

if __name__ == '__main__':
    app()

