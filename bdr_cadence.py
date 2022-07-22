import streamlit as st

st.title("BDR Cadence")
cadence = ['e l c   ', '', 'e   ',
           'c   ', '', '',
           '', 'l   ', '',
           'c   ', '', '',
          '','e   ','c   ',
          'c   ','','',
          '','l   ','e   ',
           '','c   ','',
          '','','e   ',]


prospectsPerDay = st.number_input("How many new prospects per day? ",
        step=1,
        value=5)

st.write("\n")
daysForecasted = st.number_input("How many days should we forecast? ",
        step=1,
        min_value=30)


emailCount=0
linkedinCount=0
callCount=0

st.write("📧 = Email, 📞 =  Call")
for day in range(1, daysForecasted + 1):

    for i in range(0, day): #add everything up do the day
        emailCount += cadence[i].count('e')
        linkedinCount += cadence[i].count('l')
        callCount += cadence[i].count('c')


    st.write(f"Day {day} ~~ {emailCount * int(prospectsPerDay)} 📧, ---- {callCount * int(prospectsPerDay)} 📞, ----- {linkedinCount* int(prospectsPerDay)} Linkedin\n")

    cadence.append('') #make sure the list does not end
    emailCount=0
    linkedinCount=0
    callCount=0
