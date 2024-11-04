import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# QUESTIONS FOR LIKELIHOOD OF FAILURE
Q1 = "What is your level of experience?"
Q2 = "How much of your time is supervised in your role?"
Q3 = "How frequently do you take part in lessons-learned exercises following the completion of a project?"
Q4 = "How much access to expertise in your areas of practice do you have?"
Q5 = "How familiar are you with the Code of Ethics and your obligations under it?"
Q6 = "How familiar are you with current codes, standards, and regulations in your technical areas of practice?"
Q7 = "What is your level of knowledge and skills in the technical aspects of your practice?"
Q8 = "How familiar are you with the regulations and standards governing you as a registrant of Engineers and Geoscientists BC (e.g., Professional Governance Act, regulations, Bylaws, standards of competence, quality management requirements, and professional practice guidelines)?"
Q9 = "What is the proficiency of your verbal and oral communication skills in relation to the needs of your role?"

# QUESTIONS FOR CONSEQUENCE OF FAILURE
Q10 = "How many people would be directly affected by a failure in your practice?"
Q11 = "How serious would the impacts be on those people from a failure in your practice?"
Q12 = "How serious/how large would the damage to the environment be if there was a failure in your practice?"
Q13 = "How serious/how large would the damage to property be if there was a failure in your practice?"

# ANSWERS FOR LIKELIHOOD OF FAILURE
A1 = ["N/A", "Senior", "Upper Level", "Intermediate", "Mid Level", "Junior"]
A2 = ["N/A", "Complete", "Moderate", "Partial", "Low", "None"]
A3 = ["N/A", "Frequently", "Regular", "Occasional", "Rare", "Never"]
A4 = ["N/A", "Frequent", "Regular", "Occasional", "Rare", "No access"]
A5 = ["N/A", "Very Familiar", "Familiar", "Somewhat Familiar", "Partially", "Not Familiar"]
A6 = ["N/A", "Very Familiar", "Familiar", "Somewhat Familiar", "Partially", "Not Familiar"]
A7 = ["N/A", "High Proficiency", "Proficient", "Medium Proficiency", "Low Proficiency", "Not Proficient"]
A8 = ["N/A", "Very Familiar", "Familiar", "Somewhat Familiar", "Partially", "Not Familiar"]
A9 = ["N/A", "High Proficiency", "Proficient", "Medium Proficiency", "Low Proficiency", "Not Proficient"]

# ANSWERS FOR CONSEQUENCE OF FAILURE
A10 = ["N/A", "None", "Small Number", "Some", "Large Number", "Many"]
A11 = ["N/A", "Not Serious", "Somewhat Serious", "Moderately Serious", "Serious", "Very Serious"]
A12 = ["N/A", "Not Serious", "Low Damage", "Some Damage", "Moderate Damage", "Major Damage"]
A13 = ["N/A", "Not Serious", "Low Damage", "Some Damage", "Moderate Damage", "Major Damage"]

# QUESTION AND ANSWER GROUPINGS
qlist_likelihood = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9]
alist_likelihood = [A1, A2, A3, A4, A5, A6, A7, A8, A9]
qlist_consequence = [Q10, Q11, Q12, Q13]
alist_consequence = [A10, A11, A12, A13]
    
with st.sidebar:
    st.header('Risk Factors Affecting the Likelihood of Failure')
    likelihood_total = 0
    likelihood_answers = 0
    for idx, question in enumerate(qlist_likelihood):
        ask = qlist_likelihood[idx]
        answer = alist_likelihood[idx]
        box = st.radio(ask, answer, index=3)
        user_answer = answer.index(box)
        likelihood_total = user_answer + likelihood_total
        if box == "N/A":
            likelihood_answers = 0 + likelihood_answers
        else:
            likelihood_answers = 1 + likelihood_answers
    
    st.divider()
    
    st.header('Risk Factors Affecting the Consequence of Failure')
    consequence_total = 0
    consequence_answers = 0
    for idx, question in enumerate(qlist_consequence):
        ask = qlist_consequence[idx]
        answer = alist_consequence[idx]
        box = st.select_slider(ask, answer, value=answer[3])
        user_answer = answer.index(box)
        consequence_total = user_answer + consequence_total
        if box == "N/A":
            consequence_answers = 0 + consequence_answers
        else:
            consequence_answers = 1 + consequence_answers
    st.divider()
    st.markdown('Version 0.0.2')
    st.markdown('Developed by D.M. Budd, P.Eng.')

if likelihood_answers == 0:
    likelihood_answers = 1

if consequence_answers == 0:
    consequence_answers = 1

# User risk score is reported based on the actual calculated number
# Axis have been switched as per EGBC Version 4.0
x_pt = consequence_total/consequence_answers
y_pt = likelihood_total/likelihood_answers

x_user = [x_pt]
y_user = [y_pt]

# Determine the risk assessment reporting
if x_pt >= 0:
    if y_pt <= 3:
        report_ra = "Low Risk"
    else:
        report_ra = "Moderate Risk"
if x_pt >= 1:
    if y_pt <= 2:
        report_ra = "Low Risk"
    elif y_pt <= 4:
        report_ra = "Moderate Risk"
    else:
        report_ra = "High Risk"
if x_pt >= 2:
    if y_pt <= 1:
        report_ra = "Low Risk"
    elif y_pt <= 3:
        report_ra = "Moderate Risk"
    else:
        report_ra = "High Risk"
if x_pt >= 3:
    if y_pt <= 2:
        report_ra = "Moderate Risk"
    elif y_pt <= 4:
        report_ra = "High Risk"
    else:
        report_ra = "Very High Risk"
if x_pt >= 4:
    if y_pt <= 1:
        report_ra = "Moderate Risk"
    elif y_pt <= 3:
        report_ra = "High Risk"
    else:
        report_ra = "Very High Risk"


# Normalized score is based on rounding to the nearest whole number
x_pt_norm = round(x_pt,0)
y_pt_norm = round(y_pt,0)

x_user_norm = [x_pt_norm]
y_user_norm = [y_pt_norm]


# SET DEFAULT APPEARANCE OF MATRIX PLOT
fig, ax = plt.subplots()
ax.set_xlabel('Consequence of Failure')
ax.set_ylabel('Likelihood of Failure')
plt.xlim([1,5])
plt.ylim([1,5])
plt.xticks([0,1,2,3,4,5])
plt.yticks([0,1,2,3,4,5])
plt.grid(linestyle='--', linewidth=0.5)

# SET BASE VALUES AS PER TABLE B-1 RISK ASSESSMENT MATRIX
x = np.array([0,1,1,2,2,3,3,4,4,5])
y_low = np.array([3,3,2,2,1,1,0,0,0,0])
y_mod = np.array([5,5,4,4,3,3,2,2,1,1])
y_high = np.array([5,5,5,5,5,5,4,4,3,3])
y_vhigh = np.array([5,5,5,5,5,5,5,5,5,5])

if x_pt >= 3:
    x_text_offset = -25
else:
    x_text_offset = 25

if y_pt >= 3:
    y_text_offset = -25
else:
    y_text_offset = 25


# PLOTTING
ax.set_title('Table B-1 Risk Assessment Matrix (EGBC)')
ax.plot(x_user, y_user, color='black', marker='o', markersize=8)
# Removed normalized score from being plotted
# ax.plot(x_user_norm, y_user_norm, marker='s', color='blue', markersize=8, markerfacecolor='none', markeredgecolor='blue')
ax.annotate(
    'Risk Score', 
    xy=(x_pt,y_pt), xycoords='data', 
    xytext=(x_pt + x_text_offset, y_pt + y_text_offset), textcoords='offset points', 
    arrowprops=dict(arrowstyle='->',
                    connectionstyle='arc3, rad=.2'))
ax.stackplot(x, y_vhigh, color='red')
ax.stackplot(x, y_high, color='orange')
ax.stackplot(x, y_mod, color='yellow')
ax.stackplot(x, y_low, color='green')

red_patch = mpatches.Patch(color='red', label='Very High')
orange_patch = mpatches.Patch(color='orange', label='High')
yellow_patch = mpatches.Patch(color='yellow', label='Moderate')
green_patch = mpatches.Patch(color='green', label='Low')
black_circle = mlines.Line2D([], [], marker='o', color='black', markersize=8, linestyle='None', label='Risk Score')
# Removed normalized score from being plotted
# blue_square = mlines.Line2D([], [], marker='s', color='blue', markersize=8, 
#                            markerfacecolor='none', markeredgecolor='blue', 
#                            linestyle='None', label='Normalized Score')
plt.legend(handles=[red_patch, orange_patch, yellow_patch, green_patch, black_circle], bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)
my_fig = plt.show()


# TEXT OUTPUT
st.pyplot(fig)
st.markdown(f"Consequence of Failure = **{round(x_pt,1)}**")
st.markdown(f"Likelihood of Failure = **{round(y_pt,1)}**")
st.markdown(f"Normalized Risk Assessment score is **{x_pt_norm}, {u_pt_norm}** or **{report_ra}**")


# DESCRIPTION
header = st.container()
with header:
    st.title('Practice Risk Assessment Tool')
    st.markdown('Answer the questions in the sidebar by sliding the bar to the appropriate position. There are two \
    sections to complete. If a question does not apply to the practice, answer "N/A".')
    st.markdown('The risk assessment score is calculated by dividing the sum of each section by the number \
    of questions answered.')
    st.markdown('The normalized risk assessment score has been rounded to the nearest whole number.')
    st.markdown('This is a webapp based on the Engineers & Geoscientists BC Practice Risk Assessment Tool found \
    in the Appendix to the ["Guide to the Continuing Education Program" version 3.0](https://www.egbc.ca/getmedia/86710280-a428-4035-b596-e495bf36249d/EGBC-Guide-to-the-CEP.pdf). This tool has been developed \
    independently as an exercise in Python and webapp development. This tool is not endorsed by EGBC.')
    st.markdown('Email info@cavvystructural.ca for any feedback or inquiries.')
    st.divider()