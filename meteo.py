from bs4 import BeautifulSoup
import requests
import re
import streamlit as st

def requete(city):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = requests.get(f'https://www.google.com/search?q=meteo+{city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    return req

def d_p_h_w(soup,idl):    
    final = []
    labels = ["Day and hour","Weather","Temperature","Rainfall","Humidity","Wind"]
    result = ""
    for ids in idl :
        span = soup.find(id=ids)
        nums = ((str(span).split(">"))[1].split("<"))[0]
        final.append(nums)
    final[2] = final[2] + "°C"
    for c in range(len(final)):
        st.write("="*30)
        st.write(labels[c]+" : "+final[c])
    
def main():
    st.title("Weather application")
    city = st.text_input("Which place ?")
    if(city!=""):
        soup = BeautifulSoup(requete(city).text, "html.parser")
        d_p_h_w(soup,["wob_dts","wob_dc","wob_tm","wob_pp","wob_hm","wob_ws"])
        
    
main()
