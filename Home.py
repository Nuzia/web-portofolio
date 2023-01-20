import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image
from bokeh.plotting import figure


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTING ---

PAGE_TITLE = "Portofolio Profile | Nuzia Rijki Madani "
PAGE_ICON = "random"
NAME = "Nuzia Rijki Madani"
DESCRIPTION = """
Velit Lorem exercitation esse eiusmod aliquip aliqua consequat irure.Amet officia ut anim mollit Lorem exercitation commodo.
"""
EMAIL = "202009100@uniku.ac.id"
SOCIAL_MEDIA = {
    "INSTAGRAM": "https://www.instagram.com/nuzzz24/",
    "GITHUB": "https://github.com/Nuzia",
    "DISCORD": "https://discord.gg/QcVhcNbuCw",
    "TELEGRAM": "https://t.me/kimilyo",
}
# PROJECT = {
#     "PROJECT 1": "http://",
#     "PROJECT 2": "http://",
#     "PROJECT 3": "http://",
#     "PROJECT 4": "http://",
# }


st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
)


# --- LOAD CSS,PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# ---HERO SECTION---
col1,col2 = st.columns(2,gap="small")
with col1:
      st.image(profile_pic,width=230)

with col2:
      st.title(NAME)
      st.write(DESCRIPTION)
      st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
      )

# ---SOCIAL LINK---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
      cols[index].write(f"[{platform}]({link})")


st.title("#")
st.markdown("---")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["SOFT SKILL","HARD SKILL","PROJECTS","CONTACTS","ABOUT ME"],)
with tab1:
    st.markdown("---")
    st.write("1.Time Management")

    st.caption("""Time management involves the ability to use your time wisely to work as efficiently as possible."""
    )
    st.write("2.Communication")

    st.caption("""Communication is the ability to convey or share ideas and feelings effectively and it’s among the top soft skills employers require across all fields."""
    )
    st.write("3.Adaptability")
        
    st.caption("""Your adaptability shows how well you can embrace change and adjust to it.Companies and work environments constantly change: new team members come in, old ones leave, companies get bought or sold, and so on.So, you need to be able to adapt to different situations at your workplace."""
    )
    st.write("4.Problems Solving")
        
    st.caption("""Being able to analytically and creatively solve problems will come in handy no matter your job. After all, there’s no job in the world where you won’t have any problems to deal with. That is why creative problem-solvers are always in high demand."""
    )
    st.write("5.Teamwork")
        
    st.caption("""Teamwork will never cease to be a must-have soft skill. It helps you work effectively in a group and accomplish tasks."""
    )
    st.write("6.Creativity")
        
    st.caption("""We’re used to linking creativity with fields like art, or design, but creativity is a broad term that involves several sub-skills from questioning to experimenting. As such, any professional can make just as much use of creative skills as artists."""
    )
    st.write("7.Leadership")

    st.caption("""Leadership refers to the ability to mentor, train, or guide. No matter the industry."""
    )
    st.write("8.Interpersonal Skill")

    st.caption("""Interpersonal Skills
        Interpersonal skills are all about how well you interact with others, tend after relationships, and make a positive impression on those around you."""
    )
    st.write("9.Work Ethic")

    st.caption("""Work ethic relates to valuing work and putting in the effort to yield results. It’s a soft skill that employers in literally every job you’ll ever apply for will appreciate."""
    )
    st.write("10.Attention to Details")

    st.caption("""Here’s another skill no employer will reject - the ability to be thorough and accurate in your work. Paying attention even to minor details is what sets apart dedicated employees from those who just want to get the job done and go home."""
    )
with tab2:
    st.markdown("---")
    st.bar_chart({
        "data": [1],
        "ahsi": [3],
        "bhbhb":[99],      
  })

    with st.expander("See explanation"):
        st.write("""
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        """)
with tab3:
     st.markdown("---")
with tab4:
     st.markdown("---")
with tab5:
    st.subheader("About Me")
    st.markdown("---")
    st.text("""Reprehenderit aliqua ipsum laborum qui sint nisi nulla consectetur esse fugiat. Pariatur minim ullamco consequat exercitation. Ut duis exercitation deserunt cillum laboris ea officia duis quis. Cupidatat tempor esse mollit enim cupidatat velit officia magna ut sunt. Enim cupidatat quis quis magna ut veniam dolore nisi cupidatat. Culpa incididunt fugiat sunt aliquip.
       Ex tempor eiusmod velit cillum veniam et ea enim occaecat. Veniam aute irure adipisicing occaecat nulla enim pariatur proident fugiat occaecat exercitation aute. Esse ea ipsum pariatur tempor id excepteur est. Qui non occaecat enim ea.
       Ipsum tempor officia est minim et aliqua id esse cupidatat nulla deserunt commodo adipisicing. Culpa reprehenderit exercitation aute ad. Reprehenderit pariatur eiusmod ad deserunt tempor. Velit aliqua dolore eu sunt pariatur proident dolor cillum nostrud occaecat labore cupidatat irure enim. Ad aliquip est reprehenderit qui cillum ipsum in in. Amet esse minim nostrud sunt mollit commodo dolore excepteur eu cupidatat excepteur esse aliqua. Pariatur irure do eiusmod dolor mollit sunt pariatur ullamco.
       Do eu dolor labore elit enim deserunt laboris elit officia nisi fugiat. Adipisicing do qui aute consequat. Voluptate veniam voluptate elit do esse qui ex do dolor et aute est. Voluptate irure commodo cupidatat incididunt consequat ullamco esse est eiusmod. Irure non do labore esse amet aute ad magna qui sunt sunt aliqua ea dolor. Minim deserunt sit nulla sint reprehenderit nostrud eu elit duis nostrud ullamco.
       Dolor laboris ex nisi veniam consectetur anim sint adipisicing. Reprehenderit sunt commodo laboris qui Lorem commodo laboris eu est excepteur proident aute exercitation anim. Adipisicing id nisi in aliquip fugiat dolore.
       Veniam enim nisi voluptate tempor fugiat veniam Lorem sunt culpa laboris aliquip aliquip. Veniam non est pariatur Lorem qui. Ullamco ipsum incididunt est incididunt duis tempor dolor velit. Et eu cupidatat enim sint commodo. Aute sit nisi enim et Lorem. Culpa sit elit commodo fugiat. Quis ut est culpa id dolor do nisi laborum elit dolor quis pariatur.
       Ea nisi quis excepteur enim veniam excepteur commodo voluptate velit dolore. Laboris ipsum Lorem pariatur elit culpa mollit anim excepteur. Tempor irure nostrud non cupidatat anim sunt mollit. Labore commodo proident ut id.
       Cillum sit dolor cillum consequat laborum. Magna veniam dolor mollit proident ad ex qui ea in minim aute et excepteur. Non ipsum ipsum dolor cillum."""
       )