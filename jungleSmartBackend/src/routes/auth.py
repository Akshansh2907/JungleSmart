from fastapi import APIRouter, HTTPException
from sqlmodel import select
from src.models import User
from src.database import SessionDep
from src.schemas import UserSignup, UserLogin, UserResponse
from src.utils import get_password_hash, verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup")
def signup(user: UserSignup, session: SessionDep): 
    user_exists = session.exec(select(User).where(User.username == user.username)).one_or_none()
    email_exists = session.exec(select(User).where(User.email == user.email)).one_or_none()
    contact_exists = session.exec(select(User).where(User.contact_no == user.contact_no)).one_or_none()

    if user_exists:
        return HTTPException(status_code=400, detail="Username already exists")
    elif email_exists:
        return HTTPException(status_code=400, detail="Email already exists")
    elif contact_exists:
        return HTTPException(status_code=400, detail="Contact No already exists")

    hashed_password = get_password_hash(user.password)

    new_user = User(
        full_name=user.full_name,
        username=user.username,
        contact_no=user.contact_no,
        email=user.email,
        password=hashed_password,  # Store the hashed password
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    response_user = UserResponse(
        id=new_user.id,
        full_name=new_user.full_name,
        username=new_user.username,
        contact_no=new_user.contact_no,
        email=new_user.email,
        store=new_user.store
    )
    print(response_user)

    return {"message": "Signed Up Successfully", "user": response_user }

@router.post("/login")
def login(user: UserLogin, session: SessionDep):
    existing_user = session.exec(select(User).where(User.username == user.username)).one_or_none()

    if not existing_user: 
        return HTTPException(status_code=401, detail="Invalid Credentials")
    
    if not verify_password(user.password, existing_user.password):
        return HTTPException(status_code=401, detail="Invalid Credentials")
    
    response_user = UserResponse(
        id=existing_user.id,
        full_name=existing_user.full_name,
        username=existing_user.username,
        contact_no=existing_user.contact_no,
        email=existing_user.email,
        store=existing_user.store,
    )

    return { "message": "Logged In Successfully", "user": response_user }
 
