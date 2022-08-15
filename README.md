# LiveExams

## Project idea:
- At present, many students and teachers suffer from the process of correcting paper test scores. For 
example, the course teacher may delay publishing the test scores because correcting test papers requires 
a lot of time and effort, and after that comes the process of verifying the correction process and then 
publishing it to the students. We will build an Online Student Evaluation System site, which is a site where 
the traditional process of paper-based tests is transferred to a website that is easy to deal with, by 
enabling the course teacher to put various questions to test students, and after the test is completed, the 
answers will be corrected automatically and immediately, and this will contribute by facilitating the 
correction process for teachers and speeding up the presentation of results to students.

## The problems faced during the construction of the project:
- We faced many problems during the development process of the project, and among those problems is 
the process of linking the database with the website, as well as we faced difficulty separating the nature 
of the work of teachers' and students' accounts and how we will be implementing them. In addition, we 
faced difficulty with saving images on the server and displaying them with questions consistently. Finally,
after making sure that the project works on our local devices, we faced the problem of uploading the 
project to one of the web hosts to enable access to the project from all devices at any time.

## The solutions we made:
- One of the solutions we have done to solve the problem of linking the database with a website is to use 
the Django framework, which is in the Python language. This framework helped us easily link between the 
database and the website and helped us fetch information from the database clearly and simply.

- The problem of separating the characteristics of the student and the teacher, we have created different 
registration pages to facilitate the differentiation between them. We also added certain characteristics to 
the teacher, such as adding, deleting, and modifying the exam, and enabling the student to perform those 
exams, and in the end, we created a relationship table that links teachers to students.

- As for the problem of saving and displaying images, we used Amazon S3 to enable the feature to store 
images on Amazon servers and then display them correctly.

- Finally, concerning the process of uploading our project to one of the hosts, we tried a lot of hosts and 
platforms, but most of them did not handle our project correctly until we saw a site called Heroku and 
uploaded our project to it, and this was done clearly and effectively, because of the ease of dealing with 
the site settings and the availability of various options for uploading The project, and also provides a 
database that can be used free of charge.
