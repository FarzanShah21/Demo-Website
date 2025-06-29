import streamlit as st

marks = st.number_input('Enter obtained marks: ')
total = st.number_input('Enter total marks: ')

# Avoid division by zero
if total != 0:
    percent = marks / total * 100
    st.subheader(f'Your percentage: :blue[{percent:.2f} %]')

    if percent >= 80:
        st.success('Excellent')
    elif percent >= 50 and percent < 80:
        st.info('Good')
    else:
        st.warning('Fail')
else:
    st.error('Total marks must be greater than 0.')