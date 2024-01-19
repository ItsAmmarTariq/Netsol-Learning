from sqlalchemy import create_engine, ForeignKey, String, Integer, Column
from sqlalchemy.orm import declarative_base, sessionmaker

import uuid

Base = declarative_base()


def genrate_uuid():
    return uuid.uuid4


class Users(Base):
    __tablename__ = 'users'
    userid = Column(String, primary_key=True, default=genrate_uuid())
    firstname = Column(String)
    lastname = Column(String)
    profilename = Column(String)
    email = Column(String)

    def __init__(self, firstname, lastname, profilename, email):
        self.firstname = firstname
        self.lastname = lastname
        self.profilename = profilename
        self.email = email


class Posts(Base):
    __tablename__ = 'posts'
    postId = Column(String, primary_key=True, default=genrate_uuid())
    userId = Column(String, ForeignKey('users.userid'))
    postContent = Column(String)

    def __init__(self, userId, postContent):
        self.userId = userId
        self.postContent = postContent


class Likes(Base):
    __tablename__ = 'likes'
    likeId = Column(String, primary_key=True, default=genrate_uuid())
    userId = Column(String, ForeignKey('users.userid'))
    postId = Column(String, ForeignKey('posts.postId'))

    def __init__(self, userId, postId):
        self.userId = userId
        self.postId = postId


db = 'postgresql://postgres:admin@localhost:5432/social_media'

engine = create_engine(db,echo=False)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


def addUser(session, firstname, lastname, profilename, email):
    exits = session.query(Users).filter(Users.email == email).all()
    if len(exits) > 0:
        print('this email already exists')
    else:
        user = Users(firstname, lastname, profilename, email)
        session.add(user)
        session.commit()
        print('user added to the database')


# create a user
firstname = 'alba'
lastname = 'balla'
profilename = 'balla_11'
email = 'alba@gmail.com'

addUser(session, firstname, lastname, profilename, email)


def addPost(session, userId, postContent):
    newpost = Posts(userId, postContent)
    session.add(newpost)
    session.commit()
    print('a new post has added')


# create a post
userId = '0d00279b-a078-4838-acd0-7ed7c1065b44'
# postContent = 'leaning sql alchemy'
# addPost(session, userId, postContent)
allposts = session.query(Posts).filter(Posts.userId == userId).all()
for post in allposts:
    print(post.postContent)



def addLike(userId,postId):
    like=Likes(userId,postId)
    session.add(like)
    session.commit()
    print(f'{userId} likes post {postId}')



# addLike("0a2b53c1-89a2-4715-9839-ac2b60056a04",'012d73c6-a467-4013-b92c-c55cbeec5b98')


# counting the likes
postId='012d73c6-a467-4013-b92c-c55cbeec5b98'

countlikes=session.query(Likes).filter(Likes.postId==postId).all()

print(len(countlikes))

# fetching the users who has liked the specific post

# UsersLikedPost = session.query(Users,Likes).join(Likes,Users.userid==Likes.userId).filter(Likes.postId==postId).all()
UsersLikedPost=session.query(Users,Likes).filter(Likes.postId==postId).all()


unique_users = set()

for user, like in UsersLikedPost:
    user_info = (user.firstname, user.lastname)
    unique_users.add(user_info)

for firstname, lastname in unique_users:
    print(f"{firstname} {lastname} liked the post.")