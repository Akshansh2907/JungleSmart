from src.models import User
from src.schemas import UserSignup
from sqlmodel import Session, select

class UserService: 
    def get_all_users(self, session: Session):
        return session.exec(select(User)).all()
    
    def get_user_by_id(self, id: int, session: Session):
        return session.exec(select(User).where(User.id == id)).one_or_none()

    def create_user(self, user_data: UserSignup, session: Session):
        user = User(**user_data)
        session.add(user)
        session.commit()
        return user

