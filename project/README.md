# ICSEPal
#### Video Demo:  https://youtu.be/yPLZ2a9pNe0
#### Description:
ICSEPal is a website for students studying in grade 10 in the ICSE syllabus. The website has three main parts : There's a part to access and practice multiple choice questions, the second part to  plan your day out, in a to-do list, and the third part being a section to view a motivational quote, along with some tips and study memes.

For the website as a whole, I decided to take a dark theme style, that looks clean, as I had notice that there aren't many websites which provide an interface like this to stuff, usually it's filled with ads, hard to access, and just too busy.

I've kind of cd prbased this off of the finance project layout, and I've used a layout file to use as the standard. I did use AI sometimes to help me with some stuff. So the mcqs option when clicked opens an html file called subjects. Now all the mcqs are from a db which had its information transferred from a csv file which i converted over from excel. Basically there's an excel file with the subjects, chapter names, questions and whatever other information that's needed. Then sql is used to query that database and when the mcqs option is clicked, each subject in the database is shown, and how many chapters there are.

Next , the user can select one of the subjects, and a new html file called chapters is loaded. This shows each separate chapter for the selected subject, with how many questions are available for that chapter. There's also an option to practice the whole subject , termed 'All' if the user wants a complete subject revision.

Once the user chooses a chapter, we load the mcqs.html file, for this, I actually took some code I found online to implement the whole quiz system, though I did customize and modify it as per my needs. This quiz system asks the users question with a time limit, and then based on what marks they get, gives a custom message, (positive is high marks, or encouraging if lower marks).

The next part is a plan section. This actually is probably the most interactive along side the quiz part. there's an option for the user to input a task they have to do, and it's displayed as a to-do list item. The user can press the tick to strike off the task, and press the delete button to remove it. The fun thing about this is the task is stored in the local storage of the device, so even if the user leaves, reloads the page, the tasks will still be there. I thought the only way to store the tasks was to require the user to make an account, but luckily I found out local storage exists.

The next and final part was the motivation part. I found an embed link which displays motivational quotes in a neat style, so I used that. These quotes are related to knowledge and learning. Below that, I used a carousel from bootstrap to have pictures of tips for different subjects.

And finally I have another carousel to display memes that are still related to the subjects the students are learning.

My aim with this website, is to create something to which new questions, subjects, classes can easily be added, so that rather than being a website for just grade 10 icse students, it's a student hub for all students. So I've created the mcqs part and everything to be ask scalable as possible.


The project as a whole was a huge learning experience. I did have to use ChatGPT a couple time for some parts, but I don't know whether it's right or wrong to do that, although the course allow sit. It did help me focus on the bigger picture a lot, and it's only because of AI I was able to make this website with the same aesthetic  imagined in my mind. And I feel like some things done like the Javascript were too difficult for me to just learn then. As this is only my first proper project I decided to use AI as well. I feel like because of this I was able to at least do this and not give up because all my ideas were too difficult for a beginner like me to implement. Anyway, I'll be continuing on with this hobby, so I think I'll be learning Javascript and the other hard things with time, with other project. I've been chasing progress, not perfection.

Finally, I know CS50 does refer to the Office a lot, so I'll end of with an iconic quote, that kind of symbolizes my whole journey with CS50.

> "I knew exactly what to do. But in a much more real sense, I had no idea what to do." — Michael Scott

Thanks for everything, bye!
