import streamlit as st
from Fruit_Guesser_Backend_model import feed_the_model

st.markdown(
    '<div style="display: flex; justify-content: center; color:#FF69B4">'
    '<h1 style="color:#FF69B4;">🍍🥑 Fruit Guesser 🍎🍌</h1>'
    '</div>',
    unsafe_allow_html=True
)
st.write("This is a simple Machine Learning Model used for guessing your fruit. Enjoy playing with the Fruit Guesser!!")

st.markdown(
    '''
    <div style="background-color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="color: #FF69B4;">How to play? 🎮</h2>
        <p style="color: #FF69B4;">
            Guess the Fruit Game Instructions:
        </p>
        <p>
            You will be presented with 5 different characteristics of a fruit that you need to select.
            For each characteristic, choose the option that best describes the fruit you're thinking of from the dropdown menu.
            Once you have selected all 5 characteristics, click the "Submit" button.
            The model will then guess the fruit based on your selected characteristics.
        </p>
        <p style="color: #FF69B4;">
            Characteristics:
        </p>
        <ul>
            <li>Color: Choose the color of the fruit.</li>
            <li>Texture: Select the texture of the fruit's skin or surface.</li>
            <li>Size: Choose the size category of the fruit.</li>
            <li>Taste: Select the taste profile of the fruit.</li>
            <li>Seed: Choose whether the fruit has seeds or is seedless.</li>
        </ul>
        <p style="color: #FF69B4;">
            Game Rules:
        </p>
        <ul>
            <li>You must select an option for each characteristic.</li>
            <li>Once you click "Submit," your choices are final, and the model will guess the fruit.</li>
        </ul>
        <p>
            Have fun playing the Guess the Fruit game!
        </p>
    </div>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div style="background-color: white; padding: 20px; border-radius: 10px;">
        <h2 style="color: #FF69B4;">Model-Structure</h2>
        <p>
            The model can recognize the following fruits:
        </p>
        <ul>
            <li>Orange 🍊</li>
            <li>Banana 🍌</li>
            <li>Mango 🥭</li>
            <li>Apple 🍎</li>
            <li>Pineapple 🍍</li>
            <li>Blue-Berry 🫐</li>
            <li>Cherry 🍒</li>
            <li>Kiwi 🥝</li>
            <li>Grape 🍇</li>
            <li>Strawberry 🍓</li>
        </ul>
    </div>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="display: flex; justify-content: center; color:#FF69B4">'
    '<h1 style="color:#FF69B4;">Lets Start</h1>'
    '</div>',
    unsafe_allow_html=True
)

color_selector = st.selectbox('Select your fruit\'s color :', ["orange", "yellow", "red", "blue", "brown", "purple",
                                                               "green"])

texture_selector = st.selectbox('Select your fruit\'s texture :', ['smooth', 'rough', 'bumpy', 'spikes'])

size_selector = st.selectbox('Select your fruit\'s size :', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
                                                             82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93,
                                                             94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104,
                                                             105, 106, 107, 108, 109, 110, 111, 112, 113, 114,
                                                             115, 116, 117, 118, 119, 120, 121, 122, 123, 124,
                                                             125, 126, 127, 128, 129, 130, 131, 132, 133, 134,
                                                             135, 136, 137, 138, 139, 140, 141, 142, 143, 144,
                                                             145, 146, 147, 148, 149, 150, 151, 152, 153, 154,
                                                             155, 156, 157, 158, 159, 160, 161, 162, 163, 164,
                                                             165, 166, 167, 168, 169, 170, 171, 172, 173, 174,
                                                             175, 176, 177, 178, 179, 180, 181, 182, 183, 184,
                                                             185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
                                                             195, 196, 197, 198, 199, 200])

taste_selector = st.selectbox('Select your fruit\'s taste :', ['sweet', 'pulpy', 'tangy', 'tart'])

seed_selector = st.selectbox('Select whether your fruit have seed or not :', ['yes', 'no'])

guess_button = st.button("Guess!")

if guess_button:
    answer = feed_the_model(color_selector, texture_selector, size_selector, taste_selector, seed_selector)
    if answer == 'Orange':
        st.write("The Fruit You Guessed Is An Orange 🍊")
    elif answer == 'Apple':
        st.write("The Fruit You Guessed Is An Apple 🍎")
    elif answer == 'Banana':
        st.write("The Fruit You Guessed Is An Banana 🍌")
    elif answer == 'Mango':
        st.write("The Fruit You Guessed Is An Mango 🥭")
    elif answer == 'Pineapple':
        st.write("The Fruit You Guessed Is An Pineapple 🍍")
    elif answer == 'Blue-Berry':
        st.write("The Fruit You Guessed Is An Blue-Berry 🫐")
    elif answer == 'Cherry':
        st.write("The Fruit You Guessed Is An Cherry 🍒")
    elif answer == 'Kiwi':
        st.write("The Fruit You Guessed Is An Kiwi 🥝")
    elif answer == 'Grape':
        st.write("The Fruit You Guessed Is An Grape 🍇")
    elif answer == 'Strawberry':
        st.write("The Fruit You Guessed Is An Strawberry 🍓")
    else:
        st.write("Sorry you might have entered the wrong values , Please do check again :)")

