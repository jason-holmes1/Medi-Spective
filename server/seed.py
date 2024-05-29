# Standard library imports
from random import randint, choice as rc
from app import app
from models import db, User, JournalEntry, CommunityPost
from datetime import datetime
from datetime import datetime
# Remote library imports
with app.app_context():
    db.drop_all()
    db.create_all()
    #~Create Users that take a password from the console and hash it

    
    #Create Journal Entries
    journal_entries = [
        JournalEntry(
            title='Starting bootcamp',
            content='I am starting the bootcamp today. I am excited to learn new things and meet new people. Definitely a bit nervous, but I am ready to take on the challenge!',
            date=datetime(2024, 1, 29),
            
        ),
        JournalEntry(
            title='Introduction',
            content='Hello I am new. I hope I can share my experience and spread love and positive energy to members here. Good day!',
            date=datetime(2024, 2, 12),
            
        ),
        JournalEntry(
            title='Stressed Out',
            content='Ugh Flatiron has me feeling extremelt stressed out. I am not sure if I can keep up with the pace. I am going to try my best to stay positive and keep pushing through!',
            date=datetime(2024, 3, 30),
            
        ),
        JournalEntry(
            title='Project mode',
            content='So excited to see the culmination of all my work in project mode. I am so proud of myself for making it this far. I am going to give it my all and make sure I finish strong!',
            date=datetime(2024, 4, 21),
            
        ),

    ]
    for journal_entry in journal_entries:
        db.session.add(journal_entry)

    #Create Community Posts
    community_posts = [
        CommunityPost(
            title='Anyone Else Struggle with ADHD?',
            content='Hello everyone! I am new to the community and I am looking to connect with others who struggle with ADHD. I am looking for advice on how to stay focused and manage my time better. Any tips?',
            date=datetime(2024, 1, 2),
            ),
        CommunityPost(
            title='Anxiety is taking over :()',
            content='Hey guys, lately, I have been feeling extremely anxious and I am not sure how to cope. I have tried meditating and exercising, but nothing seems to work. Any advice on how to manage anxiety?',
            date=datetime(2024, 2, 22),
           
        ),
        CommunityPost(
            title='Feel free to talk to me!',
            content='New to the site and was reading through some posts. If anyone needs someone to talk to, I am here for you. Feel free to reach out to me anytime. We are all in this together!',
            date=datetime(2021, 5, 12),
           
        )
    ]
    for community_post in community_posts:
        db.session.add(community_post)
    db.session.commit()

    #Commit changes





    #Print results
    print('Users:')
    for user in User.query.all():
        print(user)
    print('\nJournal Entries:')
    for journal_entry in JournalEntry.query.all():
        print(journal_entry)
    print('\nCommunity Posts:')
    for community_post in CommunityPost.query.all():
        print(community_post)
    print('\nDatabase seeded.')










    