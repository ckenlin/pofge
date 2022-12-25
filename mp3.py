import streamlit as st
from PIL import Image
year_list={'2022','2021','2020','2019','2018'}
option_year=st.sidebar.selectbox("選擇年度",year_list)

if option_year=='2022':
           type_list={'抒情歌曲':{'抒情1','抒情2'},
                      '流行歌曲':{'流行1'},
                      '搖滾歌曲':{'搖滾1'},
                      '饒舌歌曲':{'饒舌1'},
                      '民謠歌曲':{'民謠1'}}
if option_year=='2021':
           type_list={'抒情歌曲':{'抒情1'},
                      '流行歌曲':{'流行1'},
                      '搖滾歌曲':{'搖滾1'},
                      '饒舌歌曲':{'饒舌1'},
                      '民謠歌曲':{'民謠1'}}
if option_year=='2020':
           type_list={'抒情歌曲':{'抒情1'},
                      '流行歌曲':{'流行1'},
                      '搖滾歌曲':{'搖滾1'},
                      '饒舌歌曲':{'饒舌1'},
                      '民謠歌曲':{'民謠1'}} 
if option_year=='2019':
           type_list={'抒情歌曲':{'抒情1'},
                      '流行歌曲':{'流行1'},
                      '搖滾歌曲':{'搖滾1'},
                      '饒舌歌曲':{'饒舌1'},
                      '民謠歌曲':{'民謠1'}}
if option_year=='2018':
           type_list={'抒情歌曲':{'抒情1'},
                      '流行歌曲':{'流行1'},
                      '搖滾歌曲':{'搖滾1'},
                      '饒舌歌曲':{'饒舌1'},
                      '民謠歌曲':{'民謠1'}}           

option_musiclist=st.sidebar.selectbox("選擇類型",type_list)  
option_music=st.selectbox("選擇音樂",type_list[option_musiclist])

 
audio_file = open(option_year+'/'+option_music+'.mp3', "rb")           
#audio_file = open(音樂+'/'option_year+'/'+option_music+'.mp3', "rb")
st.audio(audio_file.read())


