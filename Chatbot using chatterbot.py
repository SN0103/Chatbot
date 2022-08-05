from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

vcetbot = ChatBot('Buddy', storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///database.sqlite3')

trainer = ListTrainer(vcetbot)

trainer.train([
 'Hi',
 'Hello',
 'How are you',
 'I am good, Thank you! How are you?',
 'college phone number',
 'You can reach at us on 0250 233 8234',
 'college address',
 '9RMH+GFX, K.T. Marg, Vartak College Campus Vasai Road, Vasai-Virar, Maharashtra 401202',
 'social media handles',
 'Facebook: https://www.facebook.com/vidyavardhinicollege/, LinkedIn: https://www.linkedin.com/school/vcetvasai/, Youtube: https://www.youtube.com/channel/UCjBw5a7WU00GwkxaTjF9jqg',
 'Who is the President of the college',
 'Mr. Vikas Vartak is the President of the college',
 'Who is the Principal of the college',
 'Dr. Harish Vankudre is the Principal of the college',
 'courses available in VCET',
 'The following courses are provided: Computer Engineering, Computer Science Engineering (Data Science), Artificial Intelligence, Information Technology, Mechanical Engineering, Civil Engineering, Electronics and Telecommunication Engineerings',
 'the intake capacity or seats for each courses',
 'The intake capacity for Computer Engineering, Computer Science Engineering (Data Science), Artificial Intelligence, Information Technology, Electronics and Telecommunication Engineerings are 60, Mechanical Engineering is 90 and Civil Engineering is 30',
 'fee structure of FE',
 'The fee structure for First year is 116225.00',
 'fee structure of DSE',
 'The fee structure for Direct Second year is 116278.00',
 'what are the scholarships provided',
 'Scholarships such as Rajarshi Chhatrapati Shahu Maharaj Shikshan Shulkh Shishyavrutti Yojna(EBC), Dr. Panjabrao Deshmukh Vastigruh Nirvah Bhatta Yojna(DTE), Students from Minority Communities Pursuing Higher and Professional Courses.(DTE), AICTE SWANATH Scholarship Scheme for students (2021-22), AICTE Pragati Scholarship scheme (2021-22), AICTE Saksham Scholarship scheme(2021-22)',
 'the Associate Professor & Head Of Department of Computer Engineering department',
 'Dr. Megha Trivedi is the Associate Professor & Head Of Department of Computer Engineering department',
 'the Deputy HOD & Asst. Prof of Computer Science Engineering(Data Science) departemnt',
 'Mr. Yogesh Pingle is the Deputy HOD & Asst. Prof of Computer Science Engineering(Data Science) department',
 'the Professor & Head Of Department Information Technology department',
 'Dr. Thaksen Parvat is the Professor & Head Of Department Information Technology department',
 'the Deputy HOD & Asst. Prof. Artificial Intelligence and Data Science department',
 'Ms. Sejal D’mello is the Deputy HOD & Asst. Prof. Artificial Intelligence and Data Science department',
 'the Head Of Department of Mechanical Engineering department',
 'Dr. Uday Aswalekar is the Head Of Department of Mechanical Engineering department',
 'the Associate Professor  & Head of Department of Electronics and Telecommunication Engineering department',
 'Dr. Amrita Ruperee is the Associate Professor & Head of Department of Electronics and Telecommunication Engineering department',
 'the Professor & HOD Civil department department',
 'Dr. Ajay Radke is the Professor & HOD Civil department department',
 'the FE Coordinator',
 'Dr. Sunayana Jadhav is the FE Coordinator',
 'what are the library timing of the college',
 'Monday to Friday: 8.30 a.m. to 6.00 pm, Closed on Saturday and Sunday',
 'who is the chairman of the Library',
 'Mr. Vishal Pande, Asst. Prof. , Instrumentation Engineering is the chairman of the Library',
 'Does the college has Ladies common room',
 'Yes the college has Ladies common room',
 'about vcet sports committee',
 'The sports committee hosts its annual Sports Festival called Avahan which means – ‘A call to the champions‘. It is an intra and intercollegiate sports event where all the students get to bring up their inner sportsmanship and keeping hustling towards victory. The atmosphere is filled with zest, cheers, and fun',
 'what is the Gymkhana Timings',
 'Monday to Friday: 1.15 pm – 2.00 pm 4.00 pm – 6.00 pm',
 'sports events',
 '1. Overarm Cricket, 2. Box Cricket, 3. Kabaddi, 4. Volleyball, 5. Basketball, 6. Throwball, 7.Girls Cricket, 8. Badminton, 9. Footvolley, 10. Chess, 11. Carrom, 12. Table Tennis, 13. Tug of War, 14. Arm-Wrestlingr, 15. Athletics',
 'what are the extra curricular activities held in VCET',
 'Extra-curricular activities such as : Students Council, Sports Committee, Literati, NSS',
 'what are the co curricular activities held in VCET',
 'Co-curricular activities such as: IEEE, SAE, ISA, CSI, IETE, ISHRAE, VMEA, HACKATHON',
 'about students council',
 'The Students’ Council of Vidyavardhini’s College of Engineering and Technology cardinally aims on a holistic approach to enhance the students’ life at V.C.E.T, fostering the students to grow inside the classroom and outside of it too. We conduct and organize a multifarious array of events throughout the year thereby creating an ambience for building engineers to learn, hone their talents and showcase their competences on wider platform.',
 'various events are conducted by students council',
 'Events like FE orientation, Freshers Party, Teachers Day, Garba Night, Zeal, BE farewell',
 'incharge & co-ordinator of students council',
 'Dr. Sunayana Jadhav is the incharge & co-ordinator of students council',
 'incharge & coordinator of sports committee',
 'Ms. Neha Gharat is the incharge & co-ordinator of sports committee',
 'about literati',
 'The magazine committee was remoulded and renamed and took its form as the LITERATI – THE LITERARY CLUB. The sole responsibility of this committee is to spread the light of knowledge about literature, art and display the outstanding work of our creative-minded vcetians through our annual college magazine ‘VISTA’. We begin each year by welcoming new talented members for our committee who put their heart and enthusiasm into making the year an insightful one.',
 'events conducted by literati',
 'Events like Inaugraduation Of VISTA, VCET Podcast Powered By LITERATI, Unscripted – Extempore, Marathi and Hindi KIavi Sammelan, Faceoff, Faceoff – Intercollegiate, Lit Fest, Marathi Bhasha Diwas',
 'staff incharge of literati',
 'Ms. Swati Varma is the staff incharge of literati',
 'about nss',
 'The National Service Scheme (NSS) Government of India, Ministry of Youth Affairs & Sports provides an opportunity to the student youth of INDIA to take part in various government led community service activities & programs. The sole aim of the NSS is to provide hands-on experience to young students in delivering community service. UDAAN was founded in the academic year 2014-2015 at VCET. Now UDAAN comes under the NSS committee of VCET.',
 'which various events are conducted by nss',
 'Events like Blood Donation Survey, Constitution Day Webinar, Donation Campaign, Meditation and Yoga Session, Tree Plantation in Society',
 'co-ordinator or incharge of nss',
 'Dr. Pradip Gulbhile (Humanity Department) is the co-ordinator(incharge) of nss',
 'what are the events conducted by IEEE, SAE, ISA, CSI, IETE, ISHRAE, VMEA, HACKATHON',
 'VNPS (VCET National Level Project Showcase ), Seminars, Industrial Visit, Workshops, Industry Oriented Training, Quizmania, MECHEXPO',
 'about solecthon',
 'VCET SOLECTHON, official solar electric car team of Vidyavardhinis College Of Engineering & Technology, is an entirely student-run, non-profit organization fueled by its members passion for environmentally sustainable technology. All team members get unique opportunity to gain valuable hands-on engineering and business experience while raising community awareness of clean energy vehicles. For more info: https://vcet.edu.in/VcetSolecthon/',
 'who is the placement manager',
 'Mr. Prafulla Patil is the placement manager',
 'placement companies',
 'Infosys, TCS, BYJUS, CoCa-Cola, amazon, mahindra, IBM, Capgemini, Johnson Controls, HLS, Cognizant, Jio',
 'about ecell',
 'The entrepreneurship cell of V.C.E.T., known as ‘E-Cell’ is formed with an objective of fostering entrepreneurship skills amongst the students of V.C.E.T.',
 'events conducted by ecell',
 'Events like E-Summit, Internship Fair, Bizmaster',
 'co-ordinator or incharge of ecell',
 'Mr. Chandan Kolvankar is the co-ordinator of E-cell',
])

name = input("Enter Your Name: ")

print("Hi, I am Bot!!")
print("Let me know how can I help you?")

while True:
    request = input(name+':')
    if request == 'Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        response=vcetbot.get_response(request)
        print('Bot:', response)
