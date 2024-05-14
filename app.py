import streamlit as st
import pickle

hangouts = pickle.load(open("cafe_list.pkl", 'rb'))
similarity_matrix = pickle.load(open("similarity_matrix.pkl", 'rb'))


st.header("Hangout Place Recommender System")

select_value = st.selectbox("Pilih Tempat Nongkrong", hangouts)

def recommend_cafe(cafe_name, similarity_matrix, n=5):
    idx = hangouts[hangouts['name'] == cafe_name].index[0]
    similar_cafes = sorted(list(enumerate(similarity_matrix[idx])), key=lambda x: x[1], reverse=True)[1:n+1]
    recommended_cafes = [hangouts.iloc[i[0]]['name'] for i in similar_cafes]
    return recommended_cafes




if st.button("Rekomendasi Tempat Serupa"):
    st.write("Berikut adalah Rekomendasi tempat yang sesuai dengan kriteria yang anda pilih")
    hangout_name = recommend_cafe(select_value, similarity_matrix, n=5)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(hangout_name[0])
    with col2:
        st.text(hangout_name[1])
    with col3:
        st.text(hangout_name[2])
    with col4:
        st.text(hangout_name[3])
    with col5:
        st.text(hangout_name[4])
            


