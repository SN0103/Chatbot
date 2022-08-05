from nltk.chat.util import Chat, reflections
QA = [
    [r"Hi|Hello|Heyy",
      ["Hello How can I help you?","Hey there How can I help you?","Hii How can I help you?"]
    ],
    [r"college phone number",
      ["You can reach at us on 0250 233 8234"]
    ],
    [r"college address",
      ["9RMH+GFX, K.T. Marg, Vartak College Campus Vasai Road, Vasai-Virar, Maharashtra 401202"]
    ],
    [r"social media handles",
      ["Facebook: https://www.facebook.com/vidyavardhinicollege/, LinkedIn: https://www.linkedin.com/school/vcetvasai/, Youtube: https://www.youtube.com/channel/UCjBw5a7WU00GwkxaTjF9jqg"]
    ],
    [r"Who is the President of the college",
      ["Mr. Vikas Vartak is the President of the college"]
    ],
    [r"Who is the Principal of the college",
      ["Dr. Harish Vankudre is the Principal of the college"]
    ],
    [r"courses|departments|programs",
      ["Computer Engineering\n Computer Science Engineering (Data Science), Artificial Intelligence, Information Technology, Mechanical Engineering, Civil Engineering, Electronics and Telecommunication Engineering"]
    ],
    [r"How many courses|departments|programs does the College provides?",
      ["VCET provides 7 courses"]
    ],
    [r"(.*) fees (.*) FE|fe|first year|First Year (.*)",
      ["Fees for first year is 1,16,300"]
    ],
    [r"(.*) fees (.*) DSE|dse|direct second year|Direct Second Year (.*)",
      ["Fees for Direct Second Year is 1,16,100"]
    ],
    [r"scholarships",
     ["Scholarships such as Rajarshi Chhatrapati Shahu Maharaj Shikshan Shulkh Shishyavrutti Yojna(EBC)\n Dr. Panjabrao Deshmukh Vastigruh Nirvah Bhatta Yojna(DTE)\n Students from Minority Communities Pursuing Higher and Professional Courses.(DTE)\n AICTE SWANATH Scholarship Scheme for students (2021-22)\n AICTE Pragati Scholarship scheme (2021-22)\n AICTE Saksham Scholarship scheme(2021-22)"]
    ],
    [r"(.*) documents required (.*)",
      ["1. FINAL ALLOTMENT LETTER ISSUE BY COMPETENT AUTHORITY (TWO COPIES)\n 2. RECEIPT CUM ACKNOWLEGEMENT COPY ISSUED BY SCRUTINY CENTRE (SC COPY)\n 3. RECEIPT CUM ACKNOWLEGEMENT OF SEAT ACCEPTANCE FROM COMPETENT AUTHORITY\n 4. S.S.C. MARKSHEET\n 5. FINAL YEAR DIPLOMA (BOTH SEMESTER) / B.Sc. MARKSHEETS\n 6. DIPLOMA / B.Sc. LEAVING CERTIFICATE\n 7. PROVISIONAL PASSING CERTIFICATE\n 8. EQUIVALNACE CERTIFICATE (OTHER THAN MSBTE BOARD)\n 9. NATIONALITY CERTIFICATE (IF NATIONALITY NOT MENTIONED ON DIPLOMA LEAVING CERTIFICATE)\n 10.DOMICILE CERTIFICATE (IF BIRTH PLACE IS OUT OF MAHARASHTRA)\n 11.GAP CERTIFICATE (IF ANY)\n 12.CASTE CERTIFICATE (FOR ALL CATEGORIES EXCEPT “OPEN”)\n 13.NON-CREAMY LAYER CERTIFICATE (FOR ALL CATEGORY EXCEPT “OPEN”, “SC”, “ST”)\n 14.CASTE VALIDITY CERTIFICATE (FOR ALL CATEGORIES EXCEPT “OPEN”)\n 15.ELIGIBILITY CERTIFICATE FOR ECONOMICALLY WEAKER SECTION (EWS)\n 16. FINAL CERTIFICATE FOR COVID – 19 VACCINATION\n 17.THREE RECENT PASSPORT SIZE PHOTOGRAPHS"]
    ],
    [r"intake capacity ",
      ["Intake capacity for all branches is 60 except mechanical which is 90 and civil which is 30"]
    ],
    [r"objective",
      ["At VCET, our aim is to groom the students such that he/she should be employable/ Entrepreneur, good human being with self-confidence and self-respect. For dynamic teaching learning ICT tools are used to and make teaching learning process interactive. Regularly organise workshops, expert lectures, industrial visits etc… to fulfil the curriculum gap and to enhance their knowledge. Sometimes subject is very theoretical so to develop the interest we have to relate the subject with real life examples, design assignments which need some surveys, group discussions and exploring the internet. This develops students’ interest in the subject. "]
    ],
    [r"Library timings",
      ["Monday to Friday 8:00 am to 6:00 pm, Saturday and Sunday closed."]
    ],
    [r"name of librarian",
      ["Name of Librarian is Mr Dinesh Jadhav"]
    ],
    [r"ladies common room",
      ["Yes, VCET provides Ladies Common Room"]
    ],
    [r"(.) sports committee (.*)",
      ["The Sports Committee organizes its annual Sports fest AVAHAN, 11-day long Inter and Intra college event. We aim at culminating our eleven days of sports celebration (festivities) into a grandeur of enthusiasm and thrill, goosebumps, and the sounds of victory, strategy, and skill. The Committee also organizes the sports training program known as the Induction Programme to train students for the all-round growth development."]
    ],
    [r"What are the extra curricular activities held in vcet",
      ["Extra-Curricular activities such as Student's Council\n Sports Committee\n Literati\n NSS"]
    ],
    [r"What are the co curricular activities held in vcet",
      ["Co-Curricular activities such as IEEE\n SAE\n ISA\n CSI\n IETE\n ISHRAE\n VMEA\n HACKATHON"]
    ],
    [r"(.*) placements contacts (.*)",
      ["Mr. Prafulla Patil\n Placement Manager\n Email id: placements@vcet.edu.in\n Phone no: 7710070966","Mr. Sanket Patil\n training And Placement Officer\n Email id: placements@vcet.edu.in\n Phone no: 7710070970 / 9987173606"]
    ],
    [r"Associate Professor & Head Of Department of Computer Engineering department",
     ["Dr. Megha Trivedi is the Associate Professor & Head Of Department of Computer Engineering department"]
    ],
    [r"Deputy HOD & Asst. Prof of Computer Science Engineering(Data Science) department",
     ["Mr. Yogesh Pingle is the Deputy HOD & Asst. Prof of Computer Science Engineering(Data Science) department"]
    ],
    [r"Professor & Head Of Department Information Technology department",
     ["Dr. Thaksen Parvat is the Professor & Head Of Department Information Technology department"]
    ],
    [r"Deputy HOD & Asst. Prof. Artificial Intelligence and Data Science department",
     ["Ms. Sejal D’mello is the Deputy HOD & Asst. Prof. Artificial Intelligence and Data Science department"]
    ],
    [r"Head Of Department of Mechanical Engineering department",
     ["Dr. Uday Aswalekar is the Head Of Department of Mechanical Engineering department"]
    ],
    [r"Associate Professor  & Head of Department of Electronics and Telecommunication Engineering department",
     ["Dr. Amrita Ruperee is the Associate Professor & Head of Department of Electronics and Telecommunication Engineering department"]
    ],
    [r"Professor & HOD Civil department department",
     ["Dr. Ajay Radke is the Professor & HOD Civil department department"]
    ],
    [r"the FE Coordinator",
     ["Dr. Sunayana Jadhav is the FE Coordinator"]
    ],
    [r"Gymkhana Timings",
     ["Monday to Friday: 1.15 pm – 2.00 pm 4.00 pm – 6.00 pm"]
    ],
    [r"sports events",
     ["1. Overarm Cricket\n 2. Box Cricket\n 3. Kabaddi\n 4. Volleyball\n 5. Basketball\n 6. Throwball\n 7.Girls Cricket\n 8. Badminton\n 9. Footvolley\n 10. Chess\n 11. Carrom\n 12. Table Tennis\n 13. Tug of War\n 14. Arm-Wrestlingr\n 15. Athletics"]
    ],
    [r"about students council",
     ["The Students’ Council of Vidyavardhini’s College of Engineering and Technology cardinally aims on a holistic approach to enhance the students’ life at V.C.E.T, fostering the students to grow inside the classroom and outside of it too. We conduct and organize a multifarious array of events throughout the year thereby creating an ambience for building engineers to learn, hone their talents and showcase their competences on wider platform."]
    ],
    [r"various events are conducted by students council",
     ["Events like FE orientation, Freshers Party, Teachers Day, Garba Night, Zeal, BE farewell"]
    ],
    [r"incharge & co-ordinator of students council",
     ["Dr. Sunayana Jadhav is the incharge & co-ordinator of students council"]
    ],
    [r"incharge & coordinator of sports committee",
     ["Ms. Neha Gharat is the incharge & co-ordinator of sports committee"]
    ],
    [r"about literati",
     ["The magazine committee was remoulded and renamed and took its form as the LITERATI – THE LITERARY CLUB. The sole responsibility of this committee is to spread the light of knowledge about literature, art and display the outstanding work of our creative-minded vcetians through our annual college magazine ‘VISTA’. We begin each year by welcoming new talented members for our committee who put their heart and enthusiasm into making the year an insightful one."]
    ],
    [r"events conducted by literati",
     ["Events like Inaugraduation Of VISTA, VCET Podcast Powered By LITERATI, Unscripted – Extempore, Marathi and Hindi KIavi Sammelan, Faceoff, Faceoff – Intercollegiate, Lit Fest, Marathi Bhasha Diwas"]
    ],
    [r"staff incharge of literati",
     ["Ms. Swati Varma is the staff incharge of literati"]
    ],
    [r"about nss",
     ["The National Service Scheme (NSS) Government of India, Ministry of Youth Affairs & Sports provides an opportunity to the student youth of INDIA to take part in various government led community service activities & programs. The sole aim of the NSS is to provide hands-on experience to young students in delivering community service. UDAAN was founded in the academic year 2014-2015 at VCET. Now UDAAN comes under the NSS committee of VCET."]
    ],
    [r"various events conducted by nss",
     ["Events like Blood Donation Survey, Constitution Day Webinar, Donation Campaign, Meditation and Yoga Session, Tree Plantation in Society"]
    ],
    [r"co-ordinator or incharge of nss",
     ["Dr. Pradip Gulbhile (Humanity Department) is the co-ordinator(incharge) of nss"]
    ],
    [r"events conducted by IEEE, SAE, ISA, CSI, IETE, ISHRAE, VMEA, HACKATHON",
     ["VNPS (VCET National Level Project Showcase ), Seminars, Industrial Visit, Workshops, Industry Oriented Training, Quizmania, MECHEXPO"]
    ],
    [r"about solecthon",
     ["VCET SOLECTHON, official solar electric car team of Vidyavardhinis College Of Engineering & Technology, is an entirely student-run, non-profit organization fueled by its members passion for environmentally sustainable technology. All team members get unique opportunity to gain valuable hands-on engineering and business experience while raising community awareness of clean energy vehicles. For more info: https://vcet.edu.in/VcetSolecthon/'"]
    ],
    [r"placement companies",
     ["Infosys, TCS, BYJUS, CoCa-Cola, amazon, mahindra, IBM, Capgemini, Johnson Controls, HLS, Cognizant, Jio"]
    ],
    [r"about ecell",
     ["The entrepreneurship cell of V.C.E.T., known as ‘E-Cell’ is formed with an objective of fostering entrepreneurship skills amongst the students of V.C.E.T."]
    ],
    [r"events conducted by ecell",
     ["Events like E-Summit, Internship Fair, Bizmaster"]
    ],
    [r"co-ordinator or incharge of ecell",
     ["Mr. Chandan Kolvankar is the co-ordinator of E-cell"]
    ],
]
def clgbott():
    print("Hii, Let me know how can I help you?")
chat=Chat(QA,reflections)
if __name__=="__main__":
    clgbott()
    chat.converse()