import pickle as pkl
import streamlit as st

# file_path = r'D:\Edu Path\ML\Practivce\NLP\df_new.pkl'

# try:
#     with open(file_path, 'rb') as file:
#         data = pkl.load(file)
# except Exception as e:
#     st.error(f"Error: {e}")

# st.dataframe(data)
# st.write("Working")


st.title("Movie Recommendation system")  #  title of the page

#   Write() << it's a general purpose function that shows the o/p


st.write("Page_1")
st.write(100)
st.write("Accuracy:", 0.9)

#  we can take inputs as well with text_input()
#  We can take numeric inputs as well with number_input()

age = st.number_input("Enter your:", min_value =1, max_value = 100)


name = st.text_input("Enter your input")
select_gender =st.selectbox("Select Gender", ['Male',"Female", "other"])
Experience = st.slider("YOE" , 1 , 10  )
isworking = st.checkbox("Is Working")

#  This createa a side bar 
st.sidebar.title('Filters')

name = st.sidebar.text_input("Fill the name ")

age = st.sidebar.slider("age", 10, 100)




#  Button() < returns true if pressed

if st.button("Show"):
    st.write(name)
    st.write(age)
    st.write(select_gender)
    st.write("Total Year of Experience : ",Experience)
    if isworking :
        st.write("Yes")
    else:
        st.write("No") 



#  Dividing the page in into sectins horizontally
col1, col2 = st.columns(2)

with col1:
    st.subheader("Personal Details")
    st.text_input("Name Please")

with col2:
    st.subheader("Profesional Details")
    st.slider("YOE", 1, 30)

        
tab1, tab2, tab3 = st.tabs(
    ["Overview", "Data", "Analysis"]
)

with tab1:
    st.write("Overview")
    col1, col2 = st.columns(2)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Revenue", "₹12.5 L")

    with col2:
        st.metric("Orders", "8,450")

    with col3:
        st.metric("Customers", "3,210")
    

with tab2:
    st.write("Data")

with tab3:
    st.write("Analysis")



    # Counter
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("count value"):
    st.session_state.count +=1
    st.write( st.session_state.count)

