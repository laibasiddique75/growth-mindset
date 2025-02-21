import streamlit as st

st.set_page_config(page_title="Growth Mindset Project" , page_icon="★")
st.title("Growth Mindset Challenge:Web App With Streamlit")

st.header("🚀Welcome to your Growth Journey!")

st.write("A Growth Mindset Challenge web app built with Streamlit that provides daily challenges and insights to help users develop a positive, growth-oriented mindset. It encourages self-improvement through interactive exercises and motivational content.")

st.header("💡Today's Growth Mindset Quote")
st.write("Success is not final,failure is not fatal:It is courage to continue that counts.""-Winston Churchill")

st.header("🔧What's Your Challenge Today?")

user_input=st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 you're facing: {user_input}.keep pushing forward towards your goal!🚀")
else:
    st.warning("Tell us about your challenge to get started!")

    st.header("Reflect on Your Learning")

    reflection=st.text_area("Write your reflections here:")

    if reflection:
        st.success(f"Great Insight ! Your reflection: {reflection}")

    else:
        st.info("Reflecting on past experience help you grow! Share your difficulties")

        st.header("🏆Celebrate your Wins!")

        achivement=st.text_input("Share something you're recently accomplished:")

        if achivement:
            st.success(f"🎉Amazing! you achieved : {achivement}")

        else:
            st.info("Big or small,every achievement counts!share one now 😍")

            st.write("- - -")

            st.write("🚀Keep believing in your self.Growth is a journey,not a destination!🌟")

            st.write("** Created by Laiba Siddique **")