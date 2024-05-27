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
            user_id=1
        ),
        JournalEntry(
            title='Introduction',
            content='Hello I am new. I hope I can share my experience and spread love and positive energy to members here. Good day!',
            date=datetime(2024, 2, 12),
            user_id=1
        ),
        JournalEntry(
            title='Journal Entry 3',
            content='Content for Journal Entry 3',
            date=datetime(2024, 3, 30),
            user_id=2
        ),
        JournalEntry(
            title='Journal Entry 4',
            content='Content for Journal Entry 4',
            date=datetime(2024, 4, 21),
            user_id=2
        ),

    ]
    for journal_entry in journal_entries:
        db.session.add(journal_entry)

    #Create Community Posts
    community_posts = [
        CommunityPost(
            title='Community Post 1',
            content='Content for Community Post 1',
            date=datetime(2021, 1, 1),
            user_id=1),
        CommunityPost(
            title='Community Post 2',
            content='Content for Community Post 2',
            date=datetime(2021, 1, 2),
            user_id=2
        ),
        CommunityPost(
            title='Community Post 3',
            content='Content for Community Post 3',
            date=datetime(2021, 1, 3),
            user_id=2
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










    